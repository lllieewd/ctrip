# -*- coding: UTF-8 -*-

import MySQLdb


db = MySQLdb.connect("47.99.91.152", "root", "123456", "hotel", charset='utf8')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()



