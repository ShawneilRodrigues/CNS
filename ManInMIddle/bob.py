import socket

def send_message_to_eve():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))  # Connects to Eve instead of Alice
    message = "Hello Alice, this is Bob!"
    client_socket.sendall(message.encode())
    client_socket.close()

send_message_to_eve()
