import socket

def start_mitm():
    # Step 1: Listen as a server for Bob's messages
    mitm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mitm_socket.bind(('localhost', 8888))
    mitm_socket.listen(1)
    print("Eve (MITM) is listening on port 8888...")

    conn, addr = mitm_socket.accept()
    print(f"Connected by {addr}")

    # Step 2: Intercept message from Bob
    data = conn.recv(1024)
    if data:
        print("Eve intercepted:", data.decode())

        # Modify message if desired
        modified_message = data.decode().replace("Bob", "Eve")

        # Step 3: Forward message to Alice
        forward_to_alice(modified_message)

    conn.close()
    mitm_socket.close()

def forward_to_alice(message):
    alice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    alice_socket.connect(('localhost', 9999))
    alice_socket.sendall(message.encode())
    alice_socket.close()

start_mitm()
