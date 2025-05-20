import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 9090)  
clientSocket.connect(serverAddress)

while True:
    send_msg = input("Entrer un nombre : ")
    clientSocket.sendall(send_msg.encode())

    rec_msg = clientSocket.recv(1024).decode()

    if rec_msg == "0":
        print("Trop petit ! Essayez encore.")
    elif rec_msg == "1":
        print("Trop grand ! Essayez encore.")
    elif rec_msg == "2":
        print("Bravo ! Vous avez trouvé le nombre magique 🎉")
        break
    else:
        print("Réponse inattendue du serveur :", rec_msg)
        break

clientSocket.close()
print("Fin du jeu.")
