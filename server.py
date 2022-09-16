from datetime import datetime
import datetime
from posixpath import split
import socket
import pymysql.cursors
from sumcheck import sumcheck
from timetostr import time_to_str

# 接続情報を入力そのうち可変とする
IPADDR = "10.0.140.22"
PORT = 10007
# AF_INET：IPv4形式でソケット作成
socket_server = socket.socket(socket.AF_INET)
socket_server.bind((IPADDR, PORT))
socket_server.listen()
print("server_start")
# 接続・受信の無限ループ
while True:
    # クライアントの接続受付
    socket_client, addr = socket_server.accept()
    # ソケットから byte 形式でデータ受信
    data = socket_client.recv(1024)
    print(data)
    if sumcheck(data) == 1:
        print("OK")
        socket_client.send("OK".encode("ascii"))
        strdata = data[0:len(data) - 4]
        text = strdata.decode("ascii", errors='ignore')
        print(text)
        print(text.split(','))
        nums = [int(str) for str in text.split(',')]
        print(nums)
        num_ok = nums[0]
        num_totalng = nums[1]
        str_uptime = time_to_str(nums[2] * 60) 
        nums_ng = nums[3:len(nums)]
        print(num_ok,num_totalng,str_uptime,nums_ng)
        
        connection = pymysql.connect(host="localhost",user="yuto",password="",database="gh_db",cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `production_historys` (`machine_id`,`product_id`,`OK`,`NG`,`uptime`,`date`) VALUES (%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (1,1,num_ok,num_totalng,str_uptime,datetime.date.today()))

            connection.commit()
    else:
        print("NG")
        socket_client.send("OK".encode("ascii"))
    #print(data.decode("ASCII"))
    # クライアントのソケットを閉じる
    socket_client.close()