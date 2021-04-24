'''直接访问已有数据库'''

import mysql.connector

# 连接数据库
mydb = mysql.connector.connect(host='localhost',user='root',password='',database='jy39')

# 获取游标
cursor = mydb.cursor()

# 创建user表
# cursor.execute('''CREATE TABLE USER(
#                     id INT PRIMARY KEY AUTO_INCREMENT,
#                     NAME VARCHAR(20) UNIQUE,
#                     addr VARCHAR(50)
#                 )''')

# 添加记录
# cursor.execute('insert into user(name,addr) values("tom","中国-陕西")')
# cursor.execute('insert into user(name,addr) values(%s,%s)',("mike","中国-陕西"))

# 插入多条记录
# data = [
#     ('julia','西安'),
#     ('henry','宝鸡'),
#     ('hank','渭南'),
#     ('mary','汉中'),
#     ('stella','潼关')
# ]
# cursor.executemany('insert into user(name,addr) values(%s,%s)',data)

# 提交
# mydb.commit()


# 查询
# cursor.execute('select * from user')
# 获取结果集
# result = cursor.fetchall()
# print(result)
# for row in result:
#     print(row)

# 查询 addr西安的人
cursor.execute('select * from user where addr=%s',('西安',))
result = cursor.fetchone()
print(result)

# 修改

# 删除