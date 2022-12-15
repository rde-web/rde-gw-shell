import socket

class Client:
    
    def __init__(self, local_connection=True, time_out=None):
        
        if not local_connection:
            self.HOST = input('input host: ')
            self.PORT = int(input('input port: '))
        else:
            self.HOST = '127.0.0.1'
            self.PORT = 5555
        
        self.client_socket = socket.socket() # instantiate
        self.client_socket.connect((self.HOST, self.PORT))  # connect to the server
        
        self.connect()
  
    def connect(self, ):
        message = input(' => ') # take input
        while message.lower().strip() not in ['quit', 'exit', 'q']:
            self.client_socket.send(message.encode()) # send message
            response = self.client_socket.recv(1024).decode()  # receive response
            print(f'Received from server: \n{response}')  # show in terminal
            
            message = input(' => ')
            if message.lower().strip() in ['quit', 'exit', 'q']:
                break 
        self.client_socket.close()
        
if __name__ == '__main__':
    client = Client(local_connection=False)
    client.connect()
    
            
            
            
                
        