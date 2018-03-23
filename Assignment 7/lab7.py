#Aiden Sun
#Gautam Mehta
"""
Extra Credit:
Use 2 queues because each queue has a locking mechanism so when transfering data between the parent to child 
and back we establish a producer/consumer relationship that is blocking.
It is also possible to accomplish the same goal by using one queue but also with event flags. 
"""
import queue
import time
import os
import platform
import threading
import multiprocessing as mp
import socket
import pickle

HOST = 'localhost'
PORT = 5550

def childIntegerQueue(q1, q2):
    data = q1.get()
    while data != 0:
        data += 1
        q2.put(data)
        data = q1.get()
        
def childListQueue(q1, q2):
    data = q1.get()
    while data != []:
        data.append(1)
        q2.put(data)
        data = q1.get()
        
def childIntegerSocket():
    with socket.socket() as s:
        s.bind((HOST, PORT))
        
        s.listen()
        (conn, addr) = s.accept()

        while True:
            fromClient = int(conn.recv(1024).decode('utf-8'))
            
            if fromClient == 0:
                break
            
            fromClient += 1
            
            conn.send(str(fromClient).encode('utf-8'))

def childListSocket():
    with socket.socket() as s:
        s.bind((HOST, PORT))
        
        s.listen()
        (conn, addr) = s.accept()
        
        while True:
            fromClient = pickle.loads(conn.recv(4096))
            if fromClient == []:
                break
            
            fromClient.append(1)
            conn.send(pickle.dumps(fromClient))
                
def threadWithQueueInteger():
    q1 = queue.Queue()
    q2 = queue.Queue()    
    t = threading.Thread(target=childIntegerQueue, args=(q1,q2))
   
    t.start()
   
    q1.put(1)
    data = q2.get()
   
    if data != 2:
        raise Exception('Unexpected Data')
 
    data = 0
    start = time.time()
   
    for i in range(10000):
        data += 1
        q1.put(data)
        data = q2.get()
       
       
    end = time.time()
    q1.put(0)
   
    t.join()
   
    if data != 20000:
        raise Exception('Unexpected data')
   
    difference = end - start
    
    return 20000/difference

def threadWithQueueList():
    q1 = queue.Queue()
    q2 = queue.Queue()  
    t = threading.Thread(target=childListQueue, args=(q1,q2))
   
    t.start()
   
    q1.put([0])
    data = q2.get()
    if data != [0,1]:
        raise Exception('Unexpected Data')
 
    data = []
    start = time.time()
   
    for i in range(300):
        data.append(0)
        q1.put(data)
        data = q2.get()
       
    end = time.time()
    q1.put([])
   
    t.join()
   
    if len(data) != 600:
        raise Exception('Unexpected data')
   
    difference = end - start
    
    return 600/difference

def threadWithSocketsInteger():
    t = threading.Thread(target=childIntegerSocket)
    
    t.start()
    with socket.socket() as s:
        s.connect((HOST, PORT))
        
        data = str(1)
        s.send(str(1).encode('utf-8'))
        fromServer = int(s.recv(1024).decode('utf-8'))
        if fromServer != 2:
            raise Exception('Unexpected data')
        
        data = 0
        start = time.time()
        
        for i in range(10000):
            data += 1
            s.send(str(data).encode('utf-8'))
            data = int(s.recv(1024).decode('utf-8'))
           
        end = time.time()
        s.send(str(0).encode('utf-8'))
    
    t.join()
    
    if data != 20000:
        raise Exception('Unexpected data')    
    
    difference = end - start
    
    return 20000/difference

def threadWithSocketsList():
    t = threading.Thread(target=childListSocket)
    
    t.start()
    with socket.socket() as s:
        s.connect((HOST, PORT))
        data = [0]
        data_byte_string = pickle.dumps(data)
        s.send(data_byte_string)
        fromServer = pickle.loads(s.recv(4096))
        if fromServer != [0, 1]:
            raise Exception('Unexpected data')
        
        data = []
        start = time.time()
        
        for i in range(300):
            data.append(0)
            data_byte_string = pickle.dumps(data)
            s.send(data_byte_string)
            data = pickle.loads(s.recv(4096))
        
        end = time.time()

        data_byte_string = pickle.dumps([])
        s.send(data_byte_string)
        
    t.join()
    
    if len(data) != 600:
        raise Exception('Unexpected data')
    
    difference = end - start
    
    return 600/difference

def processWithQueueInteger():
    q1 = mp.Queue()
    q2 = mp.Queue()  
    p = mp.Process(target=childIntegerQueue, args=(q1,q2))
   
    p.start()
   
    q1.put(1)
    data = q2.get()
    if data != 2:
        raise Exception('Unexpected Data')
 
    data = 0
    start = time.time()
   
    for i in range(10000):
        data += 1
        q1.put(data)
        data = q2.get()
       
    end = time.time()
    q1.put(0)
   
    p.join()
   
    if data != 20000:
        raise Exception('Unexpected data')
   
    difference = end - start
    
    return 20000/difference

def processWithQueueList():
    q1 = mp.Queue()
    q2 = mp.Queue()
    p = mp.Process(target=childListQueue, args=(q1,q2))
   
    p.start()
   
    q1.put([0])
    data = q2.get()
    if data != [0,1]:
        raise Exception('Unexpected Data') 
 
    data = []
    start = time.time()
   
    for i in range(300):
        data.append(0)
        q1.put(data)
        data = q2.get()
       
    end = time.time()
    q1.put([])
   
    p.join()
   
    if len(data) != 600:
        raise Exception('Unexpected data')
   
    difference = end - start

    return 600/difference

def processWithSocketsInteger():
    p = mp.Process(target=childIntegerSocket)
    
    p.start()
    with socket.socket() as s:
        s.connect((HOST, PORT))
        
        
        s.send(str(1).encode('utf-8'))
        fromServer = int(s.recv(1024).decode('utf-8'))
        if fromServer != 2:
            raise Exception('Unexpected data')
        
        data = 0
        start = time.time()
        
        for i in range(10000):
            data += 1
            s.send(str(data).encode('utf-8'))
            data = int(s.recv(1024).decode('utf-8'))
           
        end = time.time()
        s.send(str(0).encode('utf-8'))
    
    p.join()
    
    if data != 20000:
        raise Exception('Unexpected data')    
    
    difference = end - start
    
    return 20000/difference

def processWithSocketsList():
    p = mp.Process(target=childListSocket)

    p.start()
    with socket.socket() as s:
        s.connect((HOST, PORT))
        data = [0]
        data_string = pickle.dumps(data)
        s.send(data_string) 
        fromServer = pickle.loads(s.recv(4096))
        if fromServer != [0, 1]:
            raise Exception('Unexpected data')

        data = []
        start = time.time()

        for i in range(300):
            data.append(0)
            data_string = pickle.dumps(data)
            s.send(data_string)
            data = pickle.loads(s.recv(4096))        
        
        end = time.time()
            
        data_string = pickle.dumps([])
        s.send(data_string)

    p.join()
    
    if len(data) != 600:
        raise Exception('Unexpected data')
    
    difference = end - start
    
    return 600/difference   

if __name__ == '__main__':
    QIT = threadWithQueueInteger()
    QIP = processWithQueueInteger()
    QLT = threadWithQueueList()
    QLP = processWithQueueList()
    
    SIT = threadWithSocketsInteger()
    SIP = processWithSocketsInteger()
    SLT = threadWithSocketsList()
    SLP = processWithSocketsList()

    print('\tOS: {}'.format(platform.system()))
    print('\tProcessor: {}'.format(platform.processor()))
    print('\tNum of cores: {}'.format(mp.cpu_count()))
    print('\t\t\t\tThreads\tProcess')
    print('\tQueue\tInteger\t\t{}\t{}'.format(int(QIT), int(QIP)))
    print('\tQueue\tList\t\t{}\t{}'.format(int(QLT), int(QLP)))
    print('\tSocket\tInteger\t\t{}\t{}'.format(int(SIT), int(SIP)))
    print('\tSocket\tList\t\t{}\t{}'.format(int(SLT), int(SLP)))
    

#run out of inputs with 1024 byte size
"""
(Conclusion)
After reviewing the data I notice that:
There is a difference in using threads vs. processes and threads is the clear winner in these tests. 
There is not a difference in using a queue vs. a socket and the data is inconsistent between the threads/processes when using a socket.
Sometimes processes have a higher ratio than threads and other times threads will have a higher ratio than processes when using a socket. 
The difference in using a small data size (integer) and a larger data size (a growing list) is that the smaller data size (integer)
has a higher ratio of one-way transfers to the time difference. Overall integers are faster than lists in all cases.
With sockets, the prerequisites is that it only takes in byte strings so it takes time to convert the data into byte strings and then back
into the original data again. 
"""