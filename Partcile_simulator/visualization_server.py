import socket
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_from_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))  # Use the same port as in C++
    server_socket.listen()

    print("Waiting for connection from C++...")

    client_socket, _ = server_socket.accept()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        position_str = data.decode('utf-8')
        position = [float(coord) for coord in position_str.split(",")]

        ax.scatter(position[0], position[1], position[2], c='r', marker='o')
        plt.pause(0.001)

    client_socket.close()
    server_socket.close()

    plt.show()

if __name__ == "__main__":
    visualize_from_socket()
