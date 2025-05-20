import socket
import random

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAdress = ('0.0.0.0', 9090)  
serverSocket.bind(serverAdress)
serverSocket.listen(1)

nb_magique = random.randint(1, 100)
print("Nombre magique choisi :", nb_magique)

connection, clientAdress = serverSocket.accept()
print(f"Connexion de {clientAdress}")

while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    try:
        nb_joueur = int(data)
    except ValueError:
        connection.sendall("Erreur: entrez un nombre valide.".encode())
        continue

    if nb_joueur < nb_magique:
        msg = "0"  # trop petit
    elif nb_joueur > nb_magique:
        msg = "1"  # trop grand
    else:
        msg = "2"  # gagné
        connection.sendall(msg.encode())
        break

    connection.sendall(msg.encode())

connection.close()
print("Le joueur a trouvé le nombre magique :", nb_magique)
