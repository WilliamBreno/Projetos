from random import sample
from time import sleep
print('-'*36)
print('\033[32m$$$$\033[m \033[33mMEGA SENA\033[m \033[32m$$$$\033[m'.center(59))
print('-'*36)
for c in range(1,int(input('Digite quantos jogos deseja fazer: '))+1):
    print(f'JOGO {c}: {sample(range(1,60),6)}')
    print('-'*35)
while True:
    des = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('-'*35)
    if des == "N":
        print('.'*3,'\033[31mO PROGRAMA IRÁ ENCERRAR\033[m','.'*3)
        sleep(1.5)
        print('-'*35)
        print('\033[7;41mO PROGRAMA FOI ENCERRADO!!\033[m\n','-'*5,'VOLTE SEMPRE😄','-'*5)
        break
    if des != 'S':
        print(f'{"OPÇÃO INVÁLIDA!!":^5}')
    if des == "S":
        for c in range(1,int(input('Digite quantos jogos deseja fazer: '))+1):
             print(f'JOGO {c}: {sample(range(1,60),6)}')
             print('-'*35)