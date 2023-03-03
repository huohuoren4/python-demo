from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOSTNAME = "192.168.56.210"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "test"

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"

db = SQLAlchemy(app)


class User(db.Model):
    """创建用户表"""
    __tablename__ = 'blog_user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer(), nullable=False, server_default="20")
    price = db.Column(db.Numeric("10,2"), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    group_id = db.Column(db.String(20), nullable=False, comment="用户组ID")


# 创建用户组
class UserGroup(db.Model):
    """创建用户组"""
    __tablename__ = 'blog_group'
    id = db.Column(db.Integer(), primary_key=True)
    group_name = db.Column(db.String(20), server_default="小学组", unique=True, nullable=False, comment="用户组名")


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
