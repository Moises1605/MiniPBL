#Classe responsável por escrver algum dado no arquivo
class Writer:

    #Construtor
    #name - nome do arquivo no qual será escrito
    def __init__(self,name):
        #adiciona ao diretorio a pasta que os arquivos estão guardados
        self.name = "./archives/" + name

    #Método responsável por escrever dados no arquivo destinado
    def write(self,content):
        archive = open(self.name,"a")
        #Escrevendo dados no arquivo
        archive.write(content)
        archive.close