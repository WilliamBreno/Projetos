from Interface import *
from time import sleep
from Interface.Arquivos import *
arq = 'Ficha.txt'
if not arquivoExiste(arq):
    CriarArquivo(arq)
    
while True:
    
    resposta = menu(['Criar um novo Cadastro','Fazer Login','Mostrar lista de cadastrados','Sair do programa'])
    if resposta == 1:
        cabeçalho('\033[1;36mNOVO CADASTRO\033[m')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        while True:
            sexo = str(input('Sexo [F/M]: ')).upper()[0].strip()
            if sexo in "FM":
                break
        senha = str(input('Crie sua senha: '))
        cadastrar(arq, nome, idade, sexo, senha)
    elif resposta == 2:
        LerLogin(arq)
    elif resposta == 3:
        LerArquivo(arq)
    elif resposta == 4:
        cabeçalho('ENCERRANDO...')
        sleep(1)
        cabeçalho('\033[1;31mPROGRAMA ENCERRADO!\033[m'.center(60))
        break
    else:
        print('ESSA OPÇÃO NÂO EXISTE!! Digite uma opção válida')
    sleep(2)