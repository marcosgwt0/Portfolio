import random
jogo = int(input('Escolha seu modo de jogo: Digite (1) para jogar contra a máquina, (2) para jogar contra outro jogador, e (3) para ver a máquina jogar contra ela mesma: '))

jogada = ['pedra','papel','tesoura']

pontos1 = 0
pontos2 = 0

if jogo == 1:
        while True:
            comandoJogador = str(input('Digite sua jogada ou PARAR se quiser parar: '))
            print('-' * 10)
            maquina = random.choice(jogada)
            if comandoJogador == 'PARAR':
                if pontos1>pontos2:
                    print('O total de pontos foi de: {}, e {}, quem ganhou foi O Jogador! Parabéns!'.format(pontos1, pontos2))
                    print('-' * 10)
                    print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
                elif pontos1 == pontos2:
                    print('O total de pontos foi de: {}, e {}, houve um empate!'.format(pontos1, pontos2))
                    print('-' * 10)
                    print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
                else:
                    print('O total de pontos foi de: {}, e {}, quem ganhou foi a máquina!'.format(pontos1, pontos2,))
                    print('-' * 10)
                    print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
                break
            if maquina == 'pedra':
                if comandoJogador == 'pedra':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('O resultado foi um empate!')
                    print('-' * 10)
            elif maquina == 'papel':
                if comandoJogador == 'pedra':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('Que pena :( Você perdeu.')
                    print('-' * 10)
                    pontos2 += 1
            elif maquina == 'tesoura':
                if comandoJogador == 'pedra':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('Parabéns! Você ganhou!')
                    print('-' * 10)
                    pontos1 += 1
            if maquina == 'pedra':
                if comandoJogador == 'papel':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('Parabéns! Você ganhou!')
                    print('-' * 10)
                    pontos1 += 1
            elif maquina == 'papel':
                if comandoJogador == 'papel':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('O resultado foi um empate!')
                    print('-' * 10)
            elif maquina == 'tesoura':
                if comandoJogador == 'papel':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('Que pena :( Você perdeu.')
                    print('-' * 10)
                    pontos2 += 1
            if maquina == 'pedra':
                if comandoJogador == 'tesoura':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('Que pena :( Você perdeu!')
                    print('-' * 10)
                    pontos2 += 1
            elif maquina == 'papel':
                if comandoJogador == 'tesoura':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('Parabéns! Você ganhou!')
                    print('-' * 10)
                    pontos1 += 1
            elif maquina == 'tesoura':
                if comandoJogador == 'tesoura':
                    print('você jogou: ',comandoJogador)
                    print('A máquina jogou:', maquina)
                    print('-' * 10)
                    print('O resultado foi um empate.')
                    print('-' * 10)


if jogo == 2:
    while True:
        comandoJogador = str(input('Jogador 1, por favor digite sua jogada ou PARAR se quiser parar: '))
        if comandoJogador == 'PARAR':
            if pontos1>pontos2:
                print('O total de pontos foi de: {}, e {}, quem ganhou foi O Jogador 1! Parabéns!'.format(pontos1, pontos2))
                print('-' * 10)
                print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
            elif pontos1 == pontos2:
                print('O total de pontos foi de: {}, e {}, houve um empate!'.format(pontos1, pontos2))
                print('-' * 10)
                print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
            else:
                print('O total de pontos foi de: {}, e {}, quem ganhou foi O Jogador 2! Parabéns!'.format(pontos1, pontos2,))
                print('-' * 10)
                print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
            break
        comandoJogador2 = str(input('Jogador 2, por favor digite sua jogada: '))
        print('-' * 10)
        if comandoJogador == 'pedra':
                if comandoJogador2 == 'pedra':
                    print('Jogador 1 jogou: ',comandoJogador)
                    print('Jogador 2 jogou: ', comandoJogador2)
                    print('-' * 10)
                    print('O resultado foi um empate!')
                    print('-' * 10)
                elif comandoJogador2 == 'papel':
                        print('Jogador 1 jogou: ',comandoJogador)
                        print('Jogador 2 jogou: ', comandoJogador2)
                        print('-' * 10)
                        print('Parabéns! O Jogador 2 ganhou!')
                        print('-' * 10)
                        pontos2 += 1
                elif comandoJogador2 == 'tesoura':
                        print('Jogador 1 Jogou: ',comandoJogador)
                        print('Jogador 2 jogou: ', comandoJogador2)
                        print('-' * 10)
                        print('Parabéns! O Jogador 1 ganhou!')
                        print('-' * 10)
                        pontos1 += 1
        elif comandoJogador == 'papel':
            if comandoJogador2 == 'papel':
                        print('Jogador 1 jogou: ',comandoJogador)
                        print('Jogador 2 jogou: ', comandoJogador2)
                        print('-' * 10)
                        print('O resultado foi um empate!')
                        print('-' * 10)
            elif comandoJogador2 == 'pedra':
                        print('Jogador 1 Jogou: ',comandoJogador)
                        print('Jogador 2 jogou: ', comandoJogador2)
                        print('-' * 10)
                        print('Parabéns! O Jogador 1 ganhou!')
                        print('-' * 10)
                        pontos1 += 1
            elif comandoJogador2 == 'tesoura':
                        print('Jogador 1 Jogou: ',comandoJogador)
                        print('Jogador 2 jogou: ', comandoJogador2)
                        print('-' * 10)
                        print('Parabéns! O Jogador 2 ganhou!')
                        print('-' * 10)
                        pontos2 += 1
        elif comandoJogador == 'tesoura':
                    if comandoJogador2 == 'tesoura':
                        print('Jogador 1 Jogou: ',comandoJogador)
                        print('Jogador 2 jogou: ', comandoJogador2)
                        print('-' * 10)
                        print('O resultado foi um empate!')
                        print('-' * 10)
                    elif comandoJogador2 == 'papel':
                        print('Jogador 1 Jogou: ',comandoJogador)
                        print('Jogador 2 jogou: ', comandoJogador2)
                        print('-' * 10)
                        print('Parabéns! O Jogador 1 ganhou!')
                        print('-' * 10)
                        pontos1 += 1
                    elif comandoJogador2 == 'pedra':
                        print('Jogador 1 Jogou: ',comandoJogador)
                        print('Jogador 2 jogou: ', comandoJogador2)
                        print('-' * 10)
                        print('Parabéns! O Jogador 2 ganhou!')
                        print('-' * 10)
                        pontos2 += 1

if jogo == 3:
    while True:
        maquina = random.choice(jogada)
        maquina2 = random.choice(jogada)
        if maquina == 'pedra':
                if maquina2 == 'pedra':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('O resultado foi um empate!')
                    print('-' * 10)
                elif maquina2 == 'tesoura':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('A maquina 1 ganhou!')
                    print('-' * 10)
                    pontos1 += 1
                elif maquina2 == 'papel':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('A maquina 2 ganhou!')
                    print('-' * 10)
                    pontos2 += 1
        elif maquina == 'papel':
                if maquina2 == 'papel':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('O resultado foi um empate!')
                    print('-' * 10)
                elif maquina2 == 'pedra':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('A maquina 1 ganhou!')
                    print('-' * 10)
                    pontos1 += 1
                elif maquina2 == 'tesoura':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('A maquina 2 ganhou!')
                    print('-' * 10)
                    pontos2 += 1
        elif maquina == 'tesoura':
                if maquina2 == 'tesoura':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('O resultado foi um empate!')
                    print('-' * 10)
                if maquina2 == 'papel':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('A maquina 1 ganhou!')
                    print('-' * 10)
                    pontos1 += 1
                elif maquina2 == 'pedra':
                    print('a maquina 1 jogou: ',maquina)
                    print('A máquina 2 jogou:', maquina2)
                    print('-' * 10)
                    print('A maquina 2 ganhou!')
                    print('-' * 10)
                    pontos2 += 1
                    
        comandoJogador = str(input('Jogador, por favor digite PARAR se quiser parar de assistir a máquina jogar, e se quiser continuar, digite 3: '))
        print('-' * 10)
        if comandoJogador == 'PARAR':
            if pontos1>pontos2:
                print('O total de pontos foi de: {}, e {}, quem ganhou foi A Máquina1!'.format(pontos1, pontos2))
                print('-' * 10)
                print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
            elif pontos1 == pontos2:
                print('O total de pontos foi de: {}, e {}, houve um empate!'.format(pontos1, pontos2))
                print('-' * 10)
                print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
            else:
                print('O total de pontos foi de: {}, e {}, quem ganhou foi A Máquina 2!'.format(pontos1, pontos2,))
                print('-' * 10)
                print('Feito com carinho por Marcos Gabriel Wonsovicz Troiano, e Maria Julia Lazaroto S2')
            break
            


