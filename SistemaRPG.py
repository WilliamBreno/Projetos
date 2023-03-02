import sqlite3
import PySimpleGUI as sg
from Funções.lo import inserir_dados, atualizar_dados, deletar_dados, delete_especifico

conn = sqlite3.connect('Banco_Dados_RPG_Gui.db')
sg.theme('DarkAmber')
deletar_button = sg.Button('Deletar', size=(10, 1))

confirm_layout = [
    [sg.Text('Tem certeza que deseja deletar essa lista?')],
    [sg.Button('Sim', key='confirm-delete'), sg.Button('Não')]
]

layout = [[sg.Text('Nome:', size=(7, 1), justification='left'), sg.InputText(key='nome', size=(20, 1))],
          [sg.Text('Vida:', size=(7, 1), justification='left'),
           sg.InputText(key='vida', size=(20, 1))],
          [sg.Text('Armadura:', size=(7, 1), justification='left'),
           sg.InputText(key='armor', size=(20, 1))],
          [sg.Button('Inserir'), sg.Button('Atualizar'), sg.Button('Limpar'),
           sg.Button('Deletar Total'), sg.Button('Deletar Específico')],
          [sg.Table(values=[], headings=['ID', 'Nome', 'Vida', 'Armadura'], key='table', num_rows=5), sg.Button('Campo de Batalha',
                                                                                                                image_filename='espadas.png', image_size=(110, 70), size=(15, 3), button_color=('white', 'red'), pad=((30, 10), 10), border_width=3)],
          ]

icon = 'alvore.ico'
window = sg.Window('RPG-Alvorecer', layout, icon=icon)
lista_verificada = False
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Inserir':
        inserir_dados(values['nome'], values['vida'], values['armor'])
    elif event == 'Atualizar':
        atualizar_dados(values['nome'], values['vida'], values['armor'])
    elif event == 'Deletar Total':
        cursor = conn.execute('SELECT id, nome FROM tabela')
        rows = cursor.fetchall()
        if not rows:
            icon = 'pngwing.com.ico'
            sg.popup(
                'A lista está vazia. Não há registros para deletar.', icon=icon)
        else:
            # Atualiza a tabela na interface gráfica com os dados selecionados
            window['table'].update(values=rows)
            # Pede confirmação do usuário antes de deletar todos os dados da tabela
            layout = [[sg.Text('Deseja deletar toda a lista?')],
                      [sg.Button('Sim', key='Yes'), sg.Button('Não', key='No')]]
            icon = 'pngwing.com.ico'
            windowconfirm = sg.Window(
                'Deletar Tudo', layout, icon=icon, finalize=True, size=(250, 80))
            event, values = windowconfirm.read(close=True)
            if event == 'Yes':
                conn.execute('DELETE FROM tabela')
                conn.commit()
                sg.popup('Dados deletados com sucesso.', icon=icon)
                window['table'].update(values=conn.execute(
                    'SELECT * FROM tabela').fetchall())

    if event == 'Limpar':
        deletar_dados(values['nome'])
    window['nome'].update('')
    window['vida'].update('')
    window['armor'].update('')
    window['table'].update(values=conn.execute(
        'SELECT * FROM tabela').fetchall())

    if event == 'Deletar Específico':
        layout_popup = [[sg.Text('Digite o ID do personagem que deseja deletar:')],
                        [sg.Input(key='ID')],
                        [sg.Button('OK'), sg.Button('Cancelar')]]

        window_popup = sg.Window(
            'Deletar personagem:', layout_popup, icon=icon)
        while True:
            event_popup, values_popup = window_popup.read()

            if event_popup == sg.WIN_CLOSED or event_popup == 'Cancelar':
                break
            elif event_popup == 'OK':
                num = values_popup['ID']
                delete_especifico(num)
                conn.commit()
                window['table'].update(num)
                window_popup.close()
                window['table'].update(values=conn.execute(
                    'SELECT * FROM tabela').fetchall())
    if event == 'Campo de Batalha':
        conn = sqlite3.connect('Banco_Dados_RPG_Gui.db')
        dados = conn.execute("SELECT * from tabela")
        personagens = []
        for valor in dados:
            dicio = {'nome': valor[1], 'vida': valor[2], 'armor': valor[3]}
            personagens.append(dicio)
        # Define a função para atualizar a lista de personagens na janela

        def atualiza_lista(lista, personagens):
            lista.update(
                [f"{personagem['nome']} (vida: {personagem['vida']})" for personagem in personagens])
        # Define a janela principal com uma lista de personagens e um botão para diminuir a vida
        layout = [
            [sg.Listbox(values=[f"{personagem['nome']} (vida: {personagem['vida']})" for personagem in personagens], size=(
                40, 4), key='LIST', select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)],
            [sg.Text('Diminuir vida:', size=(11, 1), justification='left'), sg.Input(
                key='INPUTD', size=(10, 1)), sg.Button('Dano', button_color=('yellow', 'red')), sg.Button('True Damage', image_filename='fogos.png', image_size=(80, 20), size=(15, 3), button_color=('black', 'white'), pad=((10, 10), 10), border_width=3)],
            [sg.Text('Aumentar vida:', size=(11, 1), justification='left'), sg.Input(
                key='INPUTV', size=(10, 1)), sg.Button('Vida', button_color=('yellow', 'green'))],
            [sg.Button('Finalizar Batalha')]
        ]

        # Cria a janela com o layout definido
        icon = 'pngwing.com.ico'
        window2 = sg.Window('Campo de Batalha', layout, icon='pngwing.com.ico')
        # Loop principal da janela
        while True:
            event, values = window2.read()  # Lê os eventos da janela
            # Verifica se o usuário fechou a janela
            if event in (sg.WIN_CLOSED, 'Finalizar Batalha'):
                break
            if event == 'LIST':
                old_value = values['LIST']
                new_value = values['LIST'][0]
                window2['LIST'].update(values=old_value + [new_value])
            if event == 'Dano':
                try:
                    # Lê o valor digitado pelo usuário
                    valor = int(values['INPUTD'])
                    personagem_selecionado = values['LIST'][0].split(
                        ' (vida: ')[0]  # Lê o personagem selecionado pelo usuário
                    for personagem in personagens:
                        armadura = personagem['armor']
                        if personagem['nome'] == personagem_selecionado:
                            if personagem['armor'] != '' and valor < armadura:
                                personagem['vida'] -= 0
                            elif personagem['armor'] != '' and valor >= armadura:
                                personagem['vida'] -= abs(valor - armadura)
                            else:
                                armadura = 0
                                personagem['vida'] -= abs(valor - armadura)
                            if personagem['vida'] <= 0:
                                personagem['vida'] = 0
                                sg.popup(f'{personagem["nome"]} morreu!')
                            break
                except ValueError:
                    sg.popup('Digite um valor válido!')
                except IndexError:
                    sg.popup('Selecione um personagem!')
                else:
                    atualiza_lista(window2['LIST'], personagens)
            if event == 'Vida':  # Verifica se o usuário clicou no botão 'Diminuir'
                try:
                    # Lê o valor digitado pelo usuário
                    valor = int(values['INPUTV'])
                    personagem_selecionado = values['LIST'][0].split(
                        ' (vida: ')[0]  # Lê o personagem selecionado pelo usuário
                    for personagem in personagens:
                        if personagem['nome'] == personagem_selecionado:
                            # Diminui a vida do personagem selecionado
                            personagem['vida'] += valor
                            break
                except ValueError:
                    # Exibe uma mensagem de erro se o valor digitado não for um número
                    sg.popup('Digite um valor válido!')
                except IndexError:
                    sg.popup('Selecione um personagem!')
                else:
                    # Atualiza a lista de personagens na janela
                    atualiza_lista(window2['LIST'], personagens)
            if event == 'True Damage':  # Verifica se o usuário clicou no botão 'Diminuir'
                try:
                    # Lê o valor digitado pelo usuário
                    valor = int(values['INPUTD'])
                    personagem_selecionado = values['LIST'][0].split(
                        ' (vida: ')[0]  # Lê o personagem selecionado pelo usuário
                    for personagem in personagens:
                        if personagem['nome'] == personagem_selecionado:
                            # Diminui a vida do personagem selecionado
                            personagem['vida'] -= valor
                            break
                except ValueError:
                    # Exibe uma mensagem de erro se o valor digitado não for um número
                    sg.popup('Digite um valor válido!')
                except IndexError:
                    sg.popup('Selecione um personagem!')
                else:
                    # Atualiza a lista de personagens na janela
                    atualiza_lista(window2['LIST'], personagens)
        window2.close()
window.close()
conn.close()
