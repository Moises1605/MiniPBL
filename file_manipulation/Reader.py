#Classe responsável por ler um arquivo
class Reader:

    #Construtor
    #name - Nome do arquivo que será lido
    def __init__(self, name):
        #adiciona ao diretorio a pasta que os arquivos estão guardados
        self.name = "./archives/" + name 

    #Método responsável por ler e printar o conteúdo do arquivo.
    def read(self):
        archive = open(self.name,"r")
        #Ler os dados do arquivo
        content = archive.readlines()
        archive.close
        for line in content:
            #Retira os \n para melhorar a visualização
            print(line.replace("\n",""))
        return content
