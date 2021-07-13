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
    def write(controller,archive,directory):#name,semaphore_writer,archive):
       # semaphore_writer.acquire()
        controller.block_writers()
    
        #Processo de escrita
        print("------Executando escritor " + threading.current_thread().name)
        directory_root = "./archives/" + directory.get_directory()
        archive = open(directory_root,"a")
        #Escrevendo dados no arquivo
        content = "\n ->" + threading.current_thread().name
        archive.write(content)
        archive.close
        #print("opa")
        time.sleep(1)
        controller.release_writers()
        #semaphore_writer.release()