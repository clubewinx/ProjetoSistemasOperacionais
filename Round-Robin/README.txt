Para executar o programa são necessários alguns passos:

Baixar o pip (gerenciador de pacotes do python)
	-Windows: o instalador normal do python já vem com o pip por padrão
	-Linux: em algumas distros o pip já vem por padrão, é necessário verificar se a sua distro já tem o recurso ou é preciso baixar.

Instalar o ambiente virtual caso seu python seja inferior ao 3.3
	-terminal Windows: python -m pip install --user virtualenv
	-terminal Linux:python3 -m pip install --user virtualenv

Criar um ambiente virtual dentro da pasta raíz do projeto a ser executado.
	-Windows: raizdoprojeto>python -m venv venv
	-Linux: raiz do projeto>python3 -m venv venv

Ativar o ambiente virtual.
	-Windows: raizdoprojeto>cd venv/cd Scripts/activate
	-Linux: raiz do projeto>d venv/cd bin/activate

Instalar os pacotes que estão dentro do requirements.txt, com o ambiente virtual habilitado:
	-Windows: raizdoprojeto>python3 -m pip install -r requirements.txt
	-Linux: raiz do projeto>python3 -m pip install -r requirements.txt

Com a virtualenv ativa e as dependências do projeto baixadas você pode executar os seguintes comandos para rodar esta app:
	-Windows:raizdoprojeto>codigo>python escalonador.py
	-Linux:raizdoprojeto>codigo>python3 escalonador.py

Para para a execução do programa basta digitar Ctrl+C

Para sair da virtualenv:
	-Windows: raizdoprojeto>deactivate
	-Linux: raiz do projeto>deactivate

Pacotes utilizados:
	Modulo OS do python para buscar o arquivo a ser inputado dentro da automação
	Matplotlib que plota graficamente as informações referentes aos processos e seus respectivos tempos de execução.
	Os demais pacotes que constam no requirements.txt ou são distribuições mínimas do python ou acompanham o matplotlib em sua instalação padrão.

Obrigatoriedades: É mandatório colocar um arquivo no formato txt dentro onde se encontra o codigo fonte que contenha no MÍNIMO os pids dos processos, a duração total do processo e o instante de chegada de cada pid.

	