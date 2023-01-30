import random
from time import sleep

print('-='*30)
print('\033[7;40mJOKENPÔ!!\033[m')
print('-='*30)
print('')

sleep(1.5)
print('O computador está pronto\nIrá jogar...')
sleep(2)
print('')
print('Agora é sua vez!!')
print('')

lista = ['pedra', 'papel', 'tesoura']
escolhaPC = random.choice(lista)

player = str(input('Escolha:\n\033[1;33m(P)\033[mPedra👊\n\033[1;32m(Pa)\033[mPapel🖐️\n\033[1;34m(T)\033[mTesoura✌️\n ')).title()
print('-='*30)
papel = 'Pa'
pedra = 'P'
tesoura = 'T'

print('JO 👊')
sleep(1.5)
print('KEN 🖐️')
sleep(1.5)
print('PÔ!! ✌️')
sleep(0.5)
print('-='*30)


if escolhaPC == 'pedra' and player == papel:
    print(f'O Pc jogou \033[1;33m{escolhaPC}\033[m 👊 e você jogou \033[1;32mPapel\033[m 🖐️')
    print('Você VENCEU!!')
        
elif escolhaPC == 'papel' and player == tesoura:
    print(f'O Pc jogou \033[1;32m{escolhaPC}\033[m 🖐️ e você jogou \033[1;34mTesoura\033[m ✌️')
    print('Você VENCEU!!')
elif escolhaPC == 'tesoura' and player == pedra:     
    print(f'O Pc jogou \033[1;34m{escolhaPC}\033[m ✌️ e você jogou \033[1;33mPedra\033[m 👊')
    print('Você VENCEU!!')
elif escolhaPC == 'papel' and player == pedra:    
    print(f'O Pc jogou \033[1;32m{escolhaPC}\033[m 🖐️ e você jogou \033[1;33mPedra\033[m 👊')
    print('Você PERDEU!!')
elif escolhaPC == 'tesoura' and player == papel:   
    print(f'O Pc jogou \033[1;34m{escolhaPC}\033[m ✌️ e você jogou \033[1;32mPapel\033[m 🖐️')
    print('Você PERDEU!!')
elif escolhaPC == 'pedra' and player == tesoura:   
    print(f'O Pc jogou \033[1;33m{escolhaPC}\033[m 👊 e você jogou \033[1;34mTesoura\033[m ✌️')
    print('Você PERDEU!!')
elif (escolhaPC == 'papel' and player == papel) or (escolhaPC == 'pedra' and player == pedra) or (escolhaPC == 'tesoura' and player == tesoura):
    print(f'O Pc jogou \033[1;31m{escolhaPC}\033[m e você jogou \033[1;31m{escolhaPC}\033[m')
    print('EMPATE!!')