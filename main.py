#Classe que vai iniciar os "processos"
from file_manipulation.Directory import Directory
from file_manipulation.Controller import Controller
from file_manipulation.Writer import Writer
from os import pipe
from file_manipulation.Reader import Reader
import threading

class main:
        
    #Iniciando threads
    #semaphore_reader = threading.Semaphore(1) #Semáforo de leitura
    #semaphore_whiter = threading.Semaphore(1) #Semáforo de escrita 
    #readers = 0
    directory = Directory(); 
    archive = ""
    controller = Controller()
    contador = 0
    controle = True

    #Criação das threads - Escolha do tipo de processo e o arquivo

    #Escritores
    #writer1 = threading.Thread(target = Writer.write,name = "1", args=(1, semaphore_whiter,archive))
    #writer2 = threading.Thread(target = Writer.write,name = "2", args=(2, semaphore_whiter,archive))
    #writer3 = threading.Thread(target = Writer.write,name = "3", args=(3, semaphore_whiter,archive))

    #Leitores
    #reader1 = threading.Thread(target = Reader.read,name = "1", args=(1,archive,semaphore_reader,semaphore_whiter,readers))
    #reader2 = threading.Thread(target = Reader.read,name = "2", args=(2,archive,semaphore_reader,semaphore_whiter,readers))
    #reader3 = threading.Thread(target = Reader.read,name = "3", args=(3,archive,semaphore_reader,semaphore_whiter,readers))
    #reader4 = threading.Thread(target = Reader.read,name = "4", args=(4,archive,semaphore_reader,semaphore_whiter,readers))
    #reader5 = threading.Thread(target = Reader.read,name = "5", args=(5,archive,semaphore_reader,semaphore_whiter,readers))

    #Escritores
    writer1 = threading.Thread(target = Writer.write,name = "1", args=(controller,archive,directory))
    writer2 = threading.Thread(target = Writer.write,name = "2", args=(controller,archive,directory))
    writer3 = threading.Thread(target = Writer.write,name = "3", args=(controller,archive,directory))

    #Leitores
    reader1 = threading.Thread(target = Reader.read,name = "1", args=(controller,archive,directory))
    reader2 = threading.Thread(target = Reader.read,name = "2", args=(controller,archive,directory))
    reader3 = threading.Thread(target = Reader.read,name = "3", args=(controller,archive,directory))
    reader4 = threading.Thread(target = Reader.read,name = "4", args=(controller,archive,directory))
    reader5 = threading.Thread(target = Reader.read,name = "5", args=(controller,archive,directory))


    #Iniciando as threads
    writer1.start()
    reader1.start()
    writer2.start()
    writer3.start()
    reader2.start()
    reader3.start()
    reader4.start()
    reader5.start()

    #Criando processos aleatorios
    #while(controle):
    #    contador +=1
    #    if(contador > 50):
    #        controle = False

    