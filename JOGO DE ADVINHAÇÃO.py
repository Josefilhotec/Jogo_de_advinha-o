# jogo onde o computador, vai “pensar” em um número entre 0 e 10.
# O jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número, voce é capaz de advinhar qual é?')
jogador = palpite = 0
while jogador != computador:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if computador > jogador:
        print('É maior... tente novamente.')
    elif computador < jogador:
        print('É menor... tente novamente.')
print('>>> PARABENS <<< \nVocê acertou em {} palpites'.format(palpite))

computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    if computador > jogador:
        print(' É mais ... tente novamente.')
    elif computador < jogador:
        print('È menos... tente novamente.')
print('>>>> PARABÉNS <<<<\nVocê acertou em {} palpites'.format(palpite))


