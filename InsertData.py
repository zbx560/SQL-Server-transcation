#coding=utf-8
# sqlserver的连接
import pymssql
import random
from sql_test import make_sql
import hashlib
# 打开数据库连接 这里的host='.'也可用本机ip或ip+端口号(sqlserver默认端口号：1433)
conn = pymssql.connect(host="localhost",server = 'DESKTOP-ZBX\SQLEXPRESS',user= "sa",password= "asd.1234", database="transcation", charset='utf8',port='62053' )
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# SQL 查询语句
sql_start = "SELECT @@VERSION"
sql_common = ""
# try:
# 执行SQL语句
cursor.execute(sql_start)
# 获取所有记录列表
results = cursor.fetchone()
print(results)
print("connected successfully!")
for i in range(0,50):
   float_data = random.uniform(0.0,50.8)
   val = chr(random.randint(0x4e00, 0x9fbf))
   string_data = str(i) + str(val) + str(float_data)
   md5_data = hashlib.md5(string_data.encode(encoding='utf-8')).hexdigest()
   cursor.execute(make_sql(float_data,md5_data,i))
   conn.commit()
      #
      # sql_result = cursor.fetchone()
      # print(sql_result)
# except:
print(results)
# 关闭数据库连接
conn.close()
