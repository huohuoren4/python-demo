from typing import Optional

import pymysql
from dbutils.pooled_db import PooledDB
from pymysql import cursors


class MysqlConnectionPool:
    __pool: Optional[PooledDB] = None

    def __init__(self, host, passwd, db, setsession=None, reset=True, port=3306,
                 user='root', charset='utf8', maxconnections=100, blocking=True,
                 creator=pymysql, mincached =0, maxcached=0, maxshared=0, maxusage=None):
        """数据库连接池初始化

        :param mincached: 连接池中空闲连接的初始数量
        :param maxcached: 共享连接的最大数量
        :param maxshared: 创建连接池的最大数量
        :param maxusage: 单个连接的最大重复使用次数
        :param passwd: 数据库密码
        :param db: 数据库名字
        :param host: 数据库 IP 地址
        :param setsession: 可选的SQL命令列表, 可以用于准备会话, 例如 ["set datestyle to…", "set time zone…"]
        :param reset: 当连接返回到连接池时, 应该如何重置连接 (reset为False或None时, 回滚begin()开始的事务;
                reset为True时, 为安全起见, 总是发出回滚)
        :param port: 数据库的端口, 默认 3306
        :param user: 数据库登录用户, 默认 root
        :param maxconnections: 连接池的最大连接数
        :param blocking: 超过最大连接数量时候的表现，为True等待连接数量下降，为false直接报错处理
        :param creator: 数据库连接第三方包, 默认 pymysql
        """
        if not self.__pool:
            self.__class__.__pool = PooledDB(creator=creator, mincached=mincached, maxcached=maxcached,
                                             maxshared=maxshared, maxconnections=maxconnections, blocking=blocking,
                                             maxusage=maxusage, setsession=setsession, reset=reset,
                                             host=host, port=port, db=db, user=user, passwd=passwd,
                                             charset=charset)
        self.conn = self.__pool.connection()
        self.cur = self.conn.cursor(cursor=cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 执行sql语句失败回滚
        self.conn.rollback()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == "__main__":
    with MysqlConnectionPool(host="192.168.56.210", user="root", passwd="123456", db="test") as db :
        db.cur.execute("select * from blog_user;")
        # 提交事务
        db.conn.commit()
        # 获取单条查询结果
        # result = db.fetchone()
        # 结果: {'id': 1, 'username': '小王', 'password': '123456', 'address': '威客网访贫问苦服务'}
        # 获取所有查询结果
        result = db.cur.fetchall()
        # 结果: [{'id': 1, 'username': '小王', 'password': '123456', 'address': '威客网访贫问苦服务'}, ... ]
        print(result)
