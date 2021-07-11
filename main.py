#Classe que vai iniciar os processos

# Isso aqui é pra testar o que eu fiz 
from file_manipulation.Writer import Writer
from os import pipe
from file_manipulation.Reader import Reader

#teste = Reader("teste.txt")
#teste.read()

teste = Writer("teste.txt")
teste.write("\nDaniel")