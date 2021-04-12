import socket,os
 
# Enter IP address and port
HOST = 'Enter.IP.Address.Here'
PORT = 4420
# Configure socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('\nHowdy!\nEOFX'.encode())
 
while True:
    # Receive data
    data = s.recv(1024)
    # Check for end of command
    if data.decode().endswith("EOFX") == True:
        # Print data without 'EOFX'
        print(data[:-4].decode())
        # Get next command
        nextcmd = input(": ")
        # Send that $hit
        if nextcmd == 'quit':
            s.send(nextcmd.encode())
            break
        else: s.send(nextcmd.encode())
    # If we haven't reach end of command, print
    else:
        print(data.decode())
