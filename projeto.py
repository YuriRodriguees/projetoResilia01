import time
from utilidade import aprensentacao, separar_por_linha
from historia import historia_Mei, historia_Ren, historia_Yuta

def apresentar_menu():
    separar_por_linha()
    escolha = input('Digite o número do ninja: ')
    separar_por_linha()
    return escolha 
    

if __name__ == '__main__':
    while True:
        escolha = apresentar_menu()
        if escolha == '1':
            print('Você escolheu o ninja "Mei"\n')
            historia_Mei()
            time.sleep(3)
            exit()
        if escolha == '2':
            print('Você escolheu o ninja "Ren"')
            historia_Ren()
            time.sleep(3)
            exit()
        if escolha == '3':
            print('Você escolheu o ninja "Yuta"')   
            historia_Yuta()
            time.sleep(3)
            exit()
        