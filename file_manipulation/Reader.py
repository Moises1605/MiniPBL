#Classe responsável por ler um arquivo
import threading
import time
class Reader:

    #Construtor
    #name - Nome do arquivo que será lido
    #def __init__(self, name):
    #    #adiciona ao diretorio a pasta que os arquivos estão guardados
    #    self.name = "./archives/" + name 

    #Método responsável por ler e printar o conteúdo do arquivo.
    def read(controller,archive,directory):#name,archive,semaphore_reader,semaphore_writer,readers):

        #semaphore_reader.acquire() # bloqueia os leitores
        #readers = readers + 1 #soma a quantidade de leitores
        #if readers == 1:
        #    semaphore_writer.acquire() #bloqueia os escritores
        #semaphore_reader.release() # desbloqueia os leitores
        
        controller.block_readers()

        #Processo de leitura
        print("------Executando leitor ",threading.current_thread().name,archive)
        directory_root = "./archives/" + directory.get_directory()
        archive = open(directory_root,"r")
        #Ler os dados do arquivo
        content = archive.readlines()
        archive.close
        #for line in content:
        #    #Retira os \n para melhorar a visualização
        #    print(line.replace("\n",""))
        print(content)
        time.sleep(0.5)
        
        controller.release_readers()

        #Finaliza a execução do "processo"
        #semaphore_reader.acquire()
        #readers = readers - 1 #soma a quantidade de leitores
        #if readers == 0:
        #   semaphore_writer.release() # desbloqueia os escritores
        #semaphore_reader.release() # desbloqueia os leitores
