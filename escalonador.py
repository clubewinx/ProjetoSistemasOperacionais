import time
import os

dados_dict={}

try:
    for files in os.listdir("./"):
        if files.endswith(".txt"):
            arquivo=(os.path.join("./", files))
except:
    print("Houve um erro ao recuperar o arquivo.")

try:
    arquivo_aberto = open(arquivo,'r')
    linhas=arquivo_aberto.readlines()
    for indice in range(len(linhas)):
        processos_e_valores=linhas[indice].strip().replace(","," ").split(" ")
        dados_dict[processos_e_valores[0]] = processos_e_valores[1::]
except Exception as e:
    print(e)


quantum=4
controle=True
contador=0
data={}
duracao={}
comeco_processo={}
tempo_IO={}
tempo=0
fila=None
cpu=None
for key, value in dados_dict.items():
  duracao[key]=value[0]
  comeco_processo[key]=value[1]
  tempo_IO[key]=value[2::]

print("***********************************")
print("***** ESCALONADOR ROUND ROBIN *****")
print("-----------------------------------")
print("------- INICIANDO SIMULACAO -------")
print("-----------------------------------")

#verificar se o tempo é 
while (controle):
    if tempo==0:
        fila="Não há processos na fila"
        cpu=

    
#ordenar os tempos de entrada em ordem crescente 


