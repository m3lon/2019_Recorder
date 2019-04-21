import socket
import threading
import subprocess
import getopt
import sys

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print("BHP Net Tool")
    print()
    print("Usage bhpnet.py -t target -p port")
    print('-l --listen                      - listen on [host]:[port] for incoming connections')
    print('-u --upload=destination          - upon receving connections upload a file and write to [destination]')
    print('-e --execute=file_to_run         - execute the given file upon receving a connection')
    print('-c --command                     - initialize a command shell')
    print()
    print()
    print("Examples:")
    print("bhpnet.py -t 192.168.1.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.1.1 -p 5555 -l -u='c:\\target.exe")
    print('bhpnet.py -t 192.168.1.1 -p 5555 -l -e="cat /etc/passwd"')
    sys.exit(0)


def main():

    #每个函数都将创建一个局部作用域
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    try:
        opts,args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
        print(opts)
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o in ('-h','--help'):
            usage()
        elif o in ('-l', '--listen'):
            listen = True
        elif o in ('-e', '--execute'):
            execute = True
        elif o in ('-c', '--command'):
            command = True
        elif o in ('-u', '--upload'):
            upload_destination = a
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False,"Unhandled Option"


    # 是要监听还是仅从标准输入发送内容
    if not listen and len(target) and port>0:

        # 从命令行读取内存内容
        # 结束 Ctrl+D
        buffer = sys.stdin.read()
        client_sender(buffer)

    if listen:
        server_loop()

# 1. 将服务器的输入发送给客户端
# 2. 将客户端发送过来的内容打印
# 3. 类似于nc ip port
def client_sender(buffer):
    global target
    global port
 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, port))
    print('[*] connect to %s:%d' % (target,port))

    if len(buffer):
        client.send(bytes(buffer,encoding='utf-8'))
    
    while True:
        recv_len = 1
        response = ""

        while recv_len:
            data = client.recv(4096)
            recv_len = len(data)
            response += str(data)

            if recv_len < 4096:
                break
        print(str(response))

        buffer = raw_input("")
        buffer += '\n'

        client.send(bytes(buffer, encoding='utf-8'))

# 如果没有定义目标 则监听所有端口 这是常用的nc -lvvp port
def server_loop():
    print('server_loop')
    global target
    global port


    if not target:
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    print('[*] listening from %s:%d' % (target,port))

    server.listen(5)

    while True:
        client_socket, data = server.accept()

        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

def run_command(command):
    command = command.rstrip()
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute command.\r\n"

    return output

def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):

        while True:

            # 读取所有字符并写入文件
            data = client_socket.recv(4096)

            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(upload_destination, 'wb')
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send('Successfully saved file to %s\r\n' % upload_destination)
        except:
            client_socket.send('Failed to save file to %s\r\n' % upload_destination)
        
    if len(execute):
        output = run_command(execute)
        client_socket.send(ouput)

    if command:

        print("123")

        while True:
            client_socket.send(b'<BHP:#> ')
            
            cmd_buffer = client_socket.recv(1024)
            # 接收文件直到发现换行

            response = run_command(cmd_buffer)

            client_socket.send(response)



main()
