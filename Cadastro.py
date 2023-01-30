import datetime
from time import sleep
des = 'sS'
dados = {}
total = []
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Ano'] = int(input('Ano de nascimento: '))
    dados['Carteira'] = int(input('Numero da sua carteira de trabalho (Digite 0 se não tem): '))
    if dados['Carteira'] == 0:
        break
    dados['AnoContratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Seu salario: '))
    sleep(1)
    print('-'*35)
    print('\033[1;32mCADASTRADO REALIZADO COM SUCESSO!!\033[m')
    print('-'*35)
    sleep(0.5)
    aposentadoria = (dados['AnoContratação']  - dados['Ano']) + 35
    dados['Aposentadoria'] = aposentadoria
    total.append(dados.copy())
    for p,d in dados.items():
        print(f'{p}: \033[1;33m{d}\033[m')
    while des != "S":
        des = str(input('Deseja cadastrar outra pessoa? [\033[1;32mS\033[m/\033[1;31mN\033[m]: ')).upper()[0].strip()
        print('-'*35)
        if des == 'N':
            break

print('\033[1;31mPROGRAMA ENCERRADO!!\033[m')
print('-'*35)
print()
print()
print('Lista de dados cadastrados')
dados.clear()
print(total)