def make_sql(data1_data,md5_data,num_data,sql_origin= "insert into transcation_data(data1,md5,num)values({data1},'{md5}',{num})"):
    # id_data = input('请输入你的名字：')
    # data1_data = input('请输入发送内容：')
    # md5_data = input('请输入ip：')
    # num_data = 2425
    # chat_socket.sendto('1:123456:发送者的名称:{my_name}:32:{my_data}'.format(my_name=name,my_data=data).encode('gbk'),(dest_ip,dest_port))
    sql_origin = sql_origin
    sql_common = sql_origin.format(data1 = data1_data,md5=md5_data,num=num_data)
    print("sql = "+ str(sql_common))
    return sql_common