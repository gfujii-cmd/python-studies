import socket
import threading

# configurar host e port

bind_ip = "0.0.0.0"
bind_port = 9999

# servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind

server.bind((bind_ip, bind_port))

# colocar o servidor para ouvir limitando a 5 conexoes simultaneas

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# thread para tratamento de clientes
def handle_client(client_socket):

    # exibe o que o cliente enviar
    request = client_socket.recv(1024)

    print "[*] Received %s" % request

    # envia um pacote de volta
    client_socket.send("ACK!")

    client_socket.close

while True:
    
    client, addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    # coloca a thread de cliente em acao
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
