from fractions import Fraction # Importa o módulo que trata de frações
from math import trunc # Importa a função "Trunc"


class Calcula_probabilidade:
    def __init__(self, probabilidade, abates_feitos):
        self.__fracao = self.__calcula_fracao(probabilidade) # Fração 
        self.__chances = self.__calcula_chances(self.__fracao, abates_feitos) # Chances em formato de dicionário
        self.__lista_chances = self.__gera_lista() # Lista das chances


    def __calcula_chances(self, probabilidade, abates_feitos): # Retorna um dicionário com as chances
        chances = {}
        if abates_feitos == '': # Se os abates forem vazios, a variável será zero
            abates_feitos = 0
        for i in range(1,10):  # Contador de 1 até 9
            for c in range(30, 91, 10): # Contadoor de 30 até 90 de dez em dez
                chances[f'{c}%'] = trunc(c/((float(abates_feitos) - float(probabilidade)))) # Chances na posição c irá receber  cálculo de probabilidade
                if i == 8:
                    chances['95%'] = trunc(95/((float(abates_feitos) - float(probabilidade)))) # Se o índice for igua a oito, chances na posição 95 irá receber o cálculo de 95% 
                if i == 9:
                    chances['97%'] = trunc(97/((float(abates_feitos) - float(probabilidade)))) # A mesma coisa do anterior porém com 97% 
        return chances
    

    def __calcula_fracao(self, fracao):
        if fracao == '': # Retornará um erro caso o usuário não tenha digitado o valor
            raise ValueError('Preencha o primeiro campo') 
        return Fraction(fracao) # Trata a fração forneceida pelo usuário
    

    def __gera_lista(self): # Retorna uma lista com as chances
        lista = []

        for k,v in self.__chances.items():
            lista.append(f'Para você ter {k} de chances de conseguir o item você deverá matar {str(v).replace("-","")} inimigos no jogo.') # A lista adciona a string retirando o sinal "-" do valor se houver
        return lista
        

    @property
    def lista_chances(self): # Getter da lista de chances
        return self.__lista_chances
