#coding=utf-8
# sqlserver的连接
import pymssql
# 打开数据库连接 这里的host='.'也可用本机ip或ip+端口号(sqlserver默认端口号：1433)
conn = pymssql.connect(host="localhost",server = 'DESKTOP-ZBX\SQLEXPRESS',user= "sa",password= "asd.1234", database="transcation", charset='utf8',port='62053' )
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# SQL 查询语句
sql = "SELECT @@VERSION"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchone()
   print(results)
except:
   print(results)
# 关闭数据库连接
conn.close()
