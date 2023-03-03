from pymysql import connect, cursors

class MysqlDB:
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
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


if __name__ == '__main__':
    with MysqlDB(host="192.168.56.210", user="root", passwd="123456", db="test") as db:
        try:
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
        except Exception as e:
            print(e)
