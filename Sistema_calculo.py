import PySimpleGUI as sg # Importa a biblioteca de interface gráfica
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED,WIN_CLOSED, Window, popup #Importa os métodos da classe "PySimpleGUI"
from Calcula_probalidade import * # Importa a classe de cálculo de probabilidade

class Sistema_Calculo_de_chances:
    def __janela_principal(self): # Retorna a janela principal
        sg.theme('Reds')
        layout = [
            [sg.Text('Probabilidade do item ser obtido:', justification='left'), sg.Input(key='prob')],
            [sg.Text('Quantos abates você ja fez?:', justification='left'), sg.Input(key='kills')],
            [sg.Button('Verificar'), sg.Button('Cancelar')]
        ]

        return sg.Window(title='Calcula probabilidade', layout=layout)
    

    def __janela_propabilidade(self, lista): # Retorna a janela com as probabilidades
        sg.theme('Reds')
        layout = [
            [sg.Listbox(values=lista, size=(80, len(lista)))], 
            [sg.Button('Sair')]
        ]

        return sg.Window(title='Chances', layout=layout)


    def window_init(self): # Função que administra a dinâmica das janelas
        window = self.__janela_principal() # Define a janela

        while True: # Looping da janela
            event, values = window.read() # Lê os eventos e os valores fornecidos pela janela

            if event == 'Cancelar' or event == WINDOW_CLOSED: # Verifica se a janela foi fechada
                break

            elif event == 'Verificar': # Verifica se o evento "Verificar" ocorreu
                try:
                    calculo = Calcula_probabilidade(values['prob'], values['kills']) # Instancia um objeto do tipo "Calcula_probabilidade"
                    
                except Exception as E: # Intercepta as excessões
                    sg.popup(E) # Mostra um popup com a menssagem de erro
                    continue # Retorna ao looping
                else: 
                    window2 = self.__janela_propabilidade(calculo.lista_chances) # Define a segunda janela

                    while True: # Looping da segunda janela
                        e, v = window2.read() # Lê os evento da segunda janela

                        if e == 'Sair' or e == WIN_CLOSED: # Verfiva se a janela foi fechada
                            break

                    window2.close() # Fecha a segunda janela

        window.close() # Fecha a primeira janela


if __name__ == '__main__': # Veriica se o contexto de execução está no escopo global
    sistema = Sistema_Calculo_de_chances() # Instancia um objeto do tipo "Sistema_calculo_de_chances"
    sistema.window_init() # Inicializa as janelas