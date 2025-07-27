import socket

ziel = ''
ports = [21, 22, 80, 443] #oder weitere Ports

for port in ports:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(1)
    ergebnis = client_socket.connect_ex((ziel, port))
    if ergebnis == 0:
        print(f"Port {port} ist offen!")
        client_socket.send(b"Hallo Server")
    else:
        print(f"Port {port} ist geschlossen.")
    client_socket.close()