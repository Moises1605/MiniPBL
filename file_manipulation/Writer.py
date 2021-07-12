#Classe responsável por escrver algum dado no arquivo
import threading
import time
class Writer:

    #Construtor
    #name - nome do arquivo no qual será escrito
    #def __init__(self,name):
    #    #adiciona ao diretorio a pasta que os arquivos estão guardados
    #    self.name = "./archives/" + name

    #Método responsável por escrever dados no arquivo destinado
    def write(controller,archive):#name,semaphore_writer,archive):
       # semaphore_writer.acquire()
        controller.block_writers()
        #Processo de escrita
        print("Executando escritor ",threading.current_thread().name)
        archive = archive + 1
        time.sleep(1)
        controller.release_writers()
      #  archive = open(name,"a")
      #  #Escrevendo dados no arquivo
      #  archive.write("content")
      #  archive.close 

        #semaphore_writer.release()