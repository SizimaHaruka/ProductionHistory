from posixpath import split
import socket

#サムチェック用関数
def sumcheck(data):
    length = len(data)
    sumdata = 0
    for c in data[0:length-3]:
        sumdata += c
    sumdata = sumdata % 0x100
    if sumdata == data[length-3]:
        return 1
    else:
        return 0

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
        num_ng = nums[1]
        print(num_ok,num_ng)
    else:
        print("NG")
    #print(data.decode("ASCII"))
    # クライアントのソケットを閉じる
    socket_client.close()