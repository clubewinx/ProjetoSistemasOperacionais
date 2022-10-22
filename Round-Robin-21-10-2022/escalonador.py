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
fila=[]
cpu=None
tempo=0
quantidade_executadas={}
quantidade_decrementada={}
quantum_processo={}
for key, value in dados_dict.items():
  duracao[key]=value[0]
  comeco_processo[value[1]]=key
  tempo_IO[key]=value[2::]
  quantidade_executadas[key]=0
  quantidade_decrementada[key]=0

def ComecarProcesso():
    print("***********************************")
    print("***** ESCALONADOR ROUND ROBIN *****")
    print("-----------------------------------")
    print("------- INICIANDO SIMULACAO -------")
    print("-----------------------------------")

def FinalizarProcesso():
    print("ACABARAM OS PROCESSOS!!!")
    print("-----------------------------------")
    print("------- Encerrando simulacao ------")
    print("-----------------------------------")

def DecrementarValor(nome_processo):
    global tempo
    pegar_duracao_processo=duracao.get(nome_processo)
    valor_analisado=quantidade_decrementada[nome_processo]
    valor_analisado=valor_analisado+1
    quantidade_decrementada[nome_processo]=valor_analisado
    nova_cpu=int(pegar_duracao_processo)-valor_analisado
    return nova_cpu

def AlterarQuantidadeExecucao(cpu_nome):
    qntd_exe=quantidade_executadas[cpu_nome]
    qntd_exe=qntd_exe+1
    quantidade_executadas[cpu_nome]=qntd_exe

def VerificacaoIO(cpu_nome_copia,cpu_valor_copia):
    global fila
    global cpu_valor
    global cpu_nome
    global tempo
    checar_qntd_exec=quantidade_executadas[cpu_nome_copia]
    if str(checar_qntd_exec) in tempo_IO[cpu_nome_copia]:
        tempo_IO[cpu_nome_copia].remove(str(checar_qntd_exec))
        cpu_aux=fila[0].replace("("," ").replace(")"," ").split(" ")
        cpu_nome=cpu_aux[0]
        cpu_valor=cpu_aux[1]
        cpu_antiga=cpu_nome_copia+"("+str(cpu_valor_copia)+")"
        cpu_nova=cpu_nome+"("+str(cpu_valor)+")"
        fila.pop(0)
        fila.append(cpu_antiga)
        resposta="#[evento] OPERACAO I/O: "+ cpu_nome_copia
        print(resposta)
        print("FILA: ",fila)
        print("CPU: ",cpu_nova)
        AlterarQuantidadeExecucao(cpu_nome)
        cpu_valor=DecrementarValor(cpu_nome)
        return "OK"

def VerificarEncerrarProcesso(cpu_nome_copia):
    global fila
    global cpu_valor
    global cpu_nome
    checar_qntd_exec=quantidade_executadas[cpu_nome_copia]
    duracao_processo=duracao.get(cpu_nome_copia)
    if str(checar_qntd_exec)==str(duracao_processo):
        cpu_aux=fila[0].replace("("," ").replace(")"," ").split(" ")
        cpu_nome=cpu_aux[0]
        cpu_valor=cpu_aux[1]
        cpu_nova=cpu_nome+"("+str(cpu_valor)+")"
        fila.pop(0)
        resposta="#[evento] ENCERRANDO OPERAÇÃO: "+ cpu_nome_copia
        print(resposta)
        print("FILA: ",fila)
        print("CPU: ",cpu_nova)
        AlterarQuantidadeExecucao(cpu_nome)
        cpu_valor=DecrementarValor(cpu_nome)
        return "OK"

#def calculaQuantum(cpu_nome):
    #global quantum_processo
    #procuro o valor de chave e recebo o valor do quantum atual
    #adiciona +1 na chave 

#def LimparQuantum()
    #recebe o nome do processo como param
    #procuro na fila o nome/valor cpu que se encaixa e retiro
    #coloco o dict o valor de none na chave e valor


#pegar o valor do quantum via input    


def checaQuantum(cpu_nome_copia)
    global quantum_processo
    global quantum
    global quantidade_executadas
    global duracao
    
    valor_atual=quantum_processo.get(cpu_nome_copia,None)
    if valor_atual <= quantum:
        CalcularQuantum()
    elif valor_atual==quantum:
        resposta="#[evento] FIM DE QUANTUM: "+ cpu_nome_copia
        cpu_nova=fila[0]
        fila.pop(0)
        pegar_duracao_processo=duracao.get(cpu_nome_copia)
        qtd_exe=quantidade_executadas.get(cpu_nome_copia,None) 
        if qtd_exe<=pegar_duracao_processo
            fila.append(cpu_nome_copia)
        print(resposta)
        print("FILA: ",fila)
        print("CPU: ",cpu_nova)
        #LimparQuantum()
    
#def EncerramentoEscalonamento():


        


def ProcurarProcessoChegada(tempo):
    pegar_nome_processo=comeco_processo.get(str(tempo),None)
    pegar_duracao_processo=duracao.get(pegar_nome_processo)
    return pegar_nome_processo,pegar_duracao_processo

def VerificarHaProcessoChegada(verificacao):
    global cpu_valor
    global tempo
    if (verificacao[0] and verificacao[1]) != None:
        processo_e_duracao=verificacao[0]+"("+verificacao[1]+")"
        fila.append(processo_e_duracao)
        resposta="#[evento] CHEGADA: "+ verificacao[0]
        #cpu_valor=DecrementarValor(cpu_nome)
        cpu_formatada=cpu_nome+"("+str(cpu_valor)+")"
        AlterarQuantidadeExecucao(cpu_nome)
        print(resposta)
        print("FILA: ",fila)
        print("CPU: ",cpu_formatada)
        cpu_valor=DecrementarValor(cpu_nome)
    else:
        AlterarQuantidadeExecucao(cpu_nome)
        cpu_formatada=cpu_nome+"("+str(cpu_valor)+")"
        print("FILA: ",fila)
        print("CPU: ",cpu_formatada)
        cpu_valor=DecrementarValor(cpu_nome)
        

for i in range(12):
    print("********** TEMPO ",tempo,"**********")
    if tempo==0:
        verificacao=ProcurarProcessoChegada(tempo)
        cpu_nome=verificacao[0]
        cpu_valor=verificacao[1]
        cpu_formatada=cpu_nome+"("+cpu_valor+")"
        AlterarQuantidadeExecucao(cpu_nome)
        print("FILA: Não há processos na fila")
        print("CPU: ",cpu_formatada)
        tempo=tempo+1
        cpu_valor=DecrementarValor(cpu_nome)
        print()
    else:
        io=VerificacaoIO(cpu_nome,cpu_valor)
        verificar_encerramento=VerificarEncerrarProcesso(cpu_nome)
        print()
        if io != "OK" and verificar_encerramento !="OK":
            verificacao=ProcurarProcessoChegada(tempo)
            VerificarHaProcessoChegada(verificacao)
        print()
        tempo=tempo+1




