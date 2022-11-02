import os
import matplotlib.pyplot as plt

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
contagem_quantum={None:None}

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

def VerificacaoIO(cpu_nome_copia,cpu_valor_copia,tempo):
    global fila
    global cpu_valor
    global cpu_nome
    global cpu_formatada
    checar_qntd_exec=quantidade_executadas[cpu_nome_copia]
    if str(checar_qntd_exec) in tempo_IO[cpu_nome_copia] and fila !=[]:
        tempo_IO[cpu_nome_copia].remove(str(checar_qntd_exec))
        cpu_aux=fila[0].replace("("," ").replace(")"," ").split(" ")
        cpu_nome=cpu_aux[0]
        cpu_valor=cpu_aux[1]
        cpu_antiga=cpu_nome_copia+"("+str(cpu_valor_copia)+")"
        cpu_formatada=cpu_nome+"("+str(cpu_valor)+")"
        fila.pop(0)
        fila.append(cpu_antiga)
        resposta="#[evento] OPERACAO I/O: "+ cpu_nome_copia
        print(resposta)

def VerificarEncerrarProcesso(cpu_nome_copia):
    global fila
    global cpu_valor
    global cpu_nome
    global cpu_formatada
    checar_qntd_exec=quantidade_executadas[cpu_nome_copia]
    duracao_processo=duracao.get(cpu_nome_copia)
    if str(checar_qntd_exec)==str(duracao_processo) and fila != []:
        cpu_aux=fila[0].replace("("," ").replace(")"," ").split(" ")
        cpu_nome=cpu_aux[0]
        cpu_valor=cpu_aux[1]
        cpu_formatada=cpu_nome+"("+str(cpu_valor)+")"
        fila.pop(0)
        resposta="#[evento] ENCERRANDO OPERAÇÃO: "+ cpu_nome_copia
        print(resposta)

def calcularQuantum(cpu_nome_copia):
    global contagem_quantum 
    valor_atual=contagem_quantum.get(cpu_nome_copia)
    valor_atual=valor_atual+1
    contagem_quantum[cpu_nome_copia]=valor_atual
    

def LimparQuantum():
    global contagem_quantum 
    contagem_quantum={None:None}

def checarQuantum(cpu_nome_copia): 
    global contagem_quantum 
    global duracao
    global quantidade_executadas
    global quantum
    global fila
    global cpu_valor
    global cpu_nome
    global cpu_formatada
    valor_quantum_atual=contagem_quantum.get(cpu_nome_copia,None)
    if (valor_quantum_atual)==None:
        nome_key=list(contagem_quantum.keys())[0]
        contagem_quantum[cpu_nome_copia]=contagem_quantum.pop(nome_key)
        contagem_quantum[cpu_nome_copia]=0
        valor_quantum_atual=contagem_quantum[cpu_nome_copia]
    if int(valor_quantum_atual)<int(quantum):
        calcularQuantum(cpu_nome_copia)  
    elif valor_quantum_atual>=quantum:
        resposta="#[evento] FIM DE QUANTUM: "+ cpu_nome_copia
        if fila != []:
            pegar_duracao_processo=int(duracao.get(cpu_nome_copia))
            qtd_exe_atual=int(quantidade_executadas.get(cpu_nome_copia,None))
            cpu_aux=fila[0].replace("("," ").replace(")"," ").split(" ")
            cpu_nome=cpu_aux[0]
            cpu_valor=cpu_aux[1]
            cpu_formatada=cpu_nome+"("+str(cpu_valor)+")"
            fila.pop(0)
            if (qtd_exe_atual)<=pegar_duracao_processo:
                quantum_restante=pegar_duracao_processo-qtd_exe_atual
                cpu_antiga=cpu_nome_copia+"("+str(quantum_restante)+")"
                fila.append(cpu_antiga)
        LimparQuantum()    
        print(resposta)
  
def checarFila(fila):
    if fila==[]:
        return "FILA: Não há processos na fila"
    else:
        return fila

def verificarEncerramentoEscalonamento():
    global quantidade_executadas
    global duracao
    global cpu_nome
    global controle
    tamanho_duracao=len(duracao)
    for value in quantidade_executadas:
        if str(quantidade_executadas[value])==str(duracao[value]):
            tamanho_duracao=tamanho_duracao-1
    if tamanho_duracao==0:
        print("#[evento] ENCERRANDO ",cpu_nome)
        controle=False
        return True

   

def ProcurarProcessoChegada(tempo):
    pegar_nome_processo=comeco_processo.get(str(tempo),None)
    pegar_duracao_processo=duracao.get(pegar_nome_processo)
    return pegar_nome_processo,pegar_duracao_processo

def VerificarHaProcessoChegada(verificacao):
    global cpu_valor
    global tempo
    global cpu_formatada
    if (verificacao[0] and verificacao[1]) != None:
        processo_e_duracao=verificacao[0]+"("+verificacao[1]+")"
        fila.append(processo_e_duracao)
        resposta="#[evento] CHEGADA: "+ verificacao[0]
        cpu_formatada=cpu_nome+"("+str(cpu_valor)+")"
        print(resposta)
    else:
        cpu_formatada=cpu_nome+"("+str(cpu_valor)+")"
        
def plotarGrafico(grafico):
    if (grafico.capitalize()).strip()=='True':
        names = list(quantidade_executadas.keys())
        values = list(quantidade_executadas.values())
        plt.plot(names, values, color='black',)
        plt.scatter(names, values, color='green')
        plt.title('Quantidade de vezes executadas em cada processo até o tempo:  %d' %tempo)
        plt.xlabel('Eixo: Processos')
        plt.ylabel('Eixo: Tempo decorrido em cada processo')
        plt.show(block=False)
        plt.pause(4)
        plt.close()

Start=True
for key, value in dados_dict.items():
    duracao[key]=value[0]
    try:
        comeco_processo[value[1]]=key
        tempo_IO[key]=value[2::]
        quantidade_executadas[key]=0
        quantidade_decrementada[key]=0
    except:
        print('Não é possível prosseguir sem saber quais são os instantes de entrada de todos os processos.')
        Start=False
        break

if Start:      
    quantum=int(input('Digite o valor do quantum: '))
    grafico=input('Acompanhar gráficos durante a execução? True/False')
    if type(quantum)!=int:
        print("Inválido")
    else:
        ComecarProcesso()
        while(controle):
            print("********** TEMPO ",tempo,"**********")
            plotarGrafico(grafico)
            if tempo==0:
                verificacao=ProcurarProcessoChegada(tempo)
                cpu_nome=verificacao[0]
                cpu_valor=verificacao[1]
                cpu_formatada=cpu_nome+"("+cpu_valor+")"
                checarQuantum(cpu_nome)
                AlterarQuantidadeExecucao(cpu_nome)
                print(checarFila(fila))
                print("CPU: ",cpu_formatada)
                tempo=tempo+1
                cpu_valor=DecrementarValor(cpu_nome)
                print()
            else:
                finalizar=verificarEncerramentoEscalonamento()
                if finalizar:
                    FinalizarProcesso()
                else:
                    VerificacaoIO(cpu_nome,cpu_valor,tempo)
                    VerificarEncerrarProcesso(cpu_nome)
                    verificacao=ProcurarProcessoChegada(tempo)
                    VerificarHaProcessoChegada(verificacao)
                    checarQuantum(cpu_nome)
                    AlterarQuantidadeExecucao(cpu_nome)
                    cpu_valor=DecrementarValor(cpu_nome)
                    print(checarFila(fila))
                    print("CPU: ",cpu_formatada)
                    print()
                    tempo=tempo+1
            




