from time import sleep
alunos = []
numeros = []
while True:
    nome= str(input('Digite seu nome: '))
    nota1= float(input('Digite sua primeira nota: '))
    nota2= float(input('Digite sua segunda nota: '))
    media = (nota1 + nota2) / 2
    numeros.append(media)
    alunos.append([nome,[nota1,nota2],media])
    print('-'*35) 
    opc = str(input('Deseja continuar? [S/N]')).upper()[0].strip()
    print('-'*35) 
    if opc == 'N':
        break

print('-'*35)  
print(f'{"Nº":<5}{"Nomes":<10}{"Notas":<10}{"Media"}')
print('-'*35) 
for p,n in enumerate(alunos):
    print(f'\033[1m{p+1:<5}\033[m\033[1m{n[0]:<7}\033[m\033[1m{n[1][0:]}\033[m    \033[1m{n[2]}\033[m')
    print('-'*35) 


while True:
    res = int(input('Deseja ver a nota de quem?(Digite \033[1;33m"0"\033[m para parar o sistema!)\nNº: '))
    print('='*60)
    if res == 0:
        sleep(1)
        print(f'{"":^20}', 'ENCERRANDO...')
        sleep(1.5)
        print(f'{"":>12}','-'*28)
        print(f'{"":^14}','\033[1;31mO PROGRAMA FOI ENCERRADO\033[m')
        print(f'{"":>10}','-'*32)
        break
        
    print(f'O aluno \033[1m{alunos[res-1][0]}\033[m teve as seguintes notas: \033[1;32m{alunos[res-1][1]}\033[m')
   
    if numeros[res-1] >= 7:
        print(f'\033[1;32mAprovado\033[m com media: \033[1;32m{numeros[res-1]}\033[m ')
    else:
        print(f'\033[1;31mReprovado\033[m com media: \033[1;31m{numeros[res-1]}\033[m ')
    print('='*50)