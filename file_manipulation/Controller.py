
import threading
import time
class Controller:

    def __init__(self):
        self.semaphore_reader = threading.Semaphore(1) #Semáforo de leitura
        self.semaphore_writer = threading.Semaphore(1) #Semáforo de escrita 
        self.readers = 0
        self.directiry = "./archives/"; 
        self.archive = 0
    
    def block_readers(self):
        self.semaphore_reader.acquire() # bloqueia os leitores
        self.readers += 1 #soma a quantidade de leitores
        if self.readers == 1:
            self.semaphore_writer.acquire() #bloqueia os escritores
        self.semaphore_reader.release() # desbloqueia os leitores

    def block_writers(self):
         self.semaphore_writer.acquire()

    def release_readers(self):
        self.semaphore_reader.acquire()
        self.readers -= 1 #subtrai a quantidade de leitores
        if self.readers == 0:
            self.semaphore_writer.release() # desbloqueia os escritores
        self.semaphore_reader.release() # desbloqueia os leitores

    def release_writers(self):
        self.semaphore_writer.release()