import time

def historia_Mei():
    print('''Olá, sou o ninja Mei!\n\nVocê caiu na nossa realidade, vou ajudar você sair daqui!\n''')
    print('''Por onde você quer ir?\n\nDarei algumas opções para você.\nEssas opções, pode definir se você volta a sua casa!\n\n''')
    print('''Você tem o portal "R" e o portal "X"\n''')
    escolha_Mei = input('Digite o portal: ')
    if escolha_Mei.upper() == 'R':
        print('')
        print('Você está a 1 passo de sair desse lugar horrível.')
        print('''Agora você tem a porta A e a porta C.\n''')
        escolha_Mei2 = input('Digite a porta: ')
        if escolha_Mei2.upper() == 'A':
            print('Tome cuidado para não vir para esse lugar de novo.')
            exit()
        elif escolha_Mei2.upper() == 'C':
            print('Você entrou na porta que não abre mais.\n\nNão tem como mais voltar para casa :(')
            time.sleep(3)
            exit()
        else:
            print('Digite "A" ou "C"') 
            time.sleep(3)
            exit()
    elif escolha_Mei.upper() == 'X':
        print('')
        print('Oh Meu Deus, você morreu ;-;')   
        time.sleep(3)
        exit()
    else:
        print('Digite "R" ou "X"')
        exit()
        time.sleep(3)
def historia_Ren():
    print('''Olá, sou o ninja Ren!\n\nVocê caiu na nossa realidade, vou ajudar você sair daqui!''')
    print('''Por onde você quer ir?\n\nDarei algumas opções para você.\nEssas opções, pode definir se você volta a sua casa!\n''')
    print('''Você tem a entrada "50" e a entrada "60"\n''')
    escolha_Ren = int(input('Digite a entrada: '))
    if escolha_Ren == 50:
        print('Você foi teleportado para sua casa, tome cuidado e não volte!')
        time.sleep(4)
        exit()
    elif escolha_Ren == 60:
        print('Você vai ficar na nossa realidade, até se tornar um ninja!')   
        time.sleep(4) 
        exit()
    else:
        print('Digite "50" ou "60"')
        time.sleep(3)
        exit()

def historia_Yuta():
    print('''Olá, sou o ninja Yuta!\n\nVocê caiu na nossa realidade, vou ajudar você sair daqui!''')
    print('''Por onde você quer ir?\n\nDarei algumas opções para você.\nEssas opções, pode definir se você volta a sua casa!\n''')
    print('''Você tem a o caminho "1" e o caminho "2"\n''')
    escolha_Yuta = int(input('Digite o caminho: '))
    if escolha_Yuta == 1:
        print('Nossa, estou andando faz 2 dias e não chego em lugar nenhum...\n')
        print('Game over')
        time.sleep(3)
        exit()
    elif escolha_Yuta == 2:
        print('Você foi sequestrado e morto em seguida.\n')
        print('Gamer over')
        time.sleep(3.5)
        exit()  
    else:
        print('Digite "1" ou "2"')
        time.sleep(2.5)
        exit()   