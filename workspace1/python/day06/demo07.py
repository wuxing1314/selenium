'''python访问数据库'''

import mysql.connector

# 连接数据库
mydb = mysql.connector.connect(host='localhost',port=3306,user='root',password='')

# 获取游标
cursor = mydb.cursor()

# 创建数据库
cursor.execute('create database jy39 charset="utf8"')
