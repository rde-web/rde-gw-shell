import sys
import socket
import time
import subprocess
from termcolor import colored



class Server:
    
    def __init__(self, local_connection=True, 
                time_out=None, queue_size=1):
                
        if not local_connection:
            self.HOST = str(input('input host: '))
            self.PORT = input('input port: ')
        else:
            self.HOST = '127.0.0.1'
            self.PORT = 5555

        self.queue_size = queue_size        
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))
        if time_out is not None:
            self.socket.settimeout(time_out)

    def start_server_print(self):
        print(f'Server started with:')
        print(f'HOST: {self.HOST}\nPORT: {self.PORT}')
        
    
    def run_server(self):
        self.start_server_print()
        print(f'[*] server listening')
        
        # configure how many client the server can listen simultaneously
        self.socket.listen(self.queue_size) # accept new connection
        client_socket, address = self.socket.accept()
        print(f'Connection from {address} has been established')
        
        while True:
            try:
                client_command = client_socket.recv(1024).decode()
                
                
                # if str(client_command) in ['quit', 'exit', 'q']:
                #     client_socket.disconnect()
                
                print(f'received command: {str(client_command)}')
                
                shell_call_result = subprocess.check_output(
                    client_command, stderr=subprocess.STDOUT, shell=True)
                
                # print(f'shell result: {shell_call_result.decode()}')

                client_socket.send(shell_call_result)
            except Exception as exc:
                print(f'corrupted with:\n{exc}')
        client_socket.close()
    
    
    
        


if __name__ == '__main__':
    shell_remote = Server(time_out=100, queue_size=3)
    shell_remote.run_server()
    
    
    print('\n')
    print('==='*10)
    print('The End')
    
    