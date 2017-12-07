#-*-coding: utf-8 -*-

import random
import pygame
import json

#pygame.init()
#screen = pygame.display.set_mode((800,600),0,32)


#2copas = pygame.image.load('2Copas.png').convert()
#3Copas = pygame.load(/home/andre/python/Cartas/Copas/3Copas.png)
#4Copas = pygame.load(/home/andre/python/Cartas/Copas/4Copas.png)
#5Copas = pygame.load(/home/andre/python/Cartas/Copas/5Copas.png)
#6Copas = pygame.load(/home/andre/python/Cartas/Copas/6Copas.png)
#7Copas = pygame.load(/home/andre/python/Cartas/Copas/7Copas.png)
#8Copas = pygame.load(/home/andre/python/Cartas/Copas/8Copas.png)
#9Copas = pygame.load(/home/andre/python/Cartas/Copas/9Copas.png)
#10Copas = pygame.load(/home/andre/python/Cartas/Copas/10Copas.png)
#AsCopas = pygame.load(/home/andre/python/Cartas/Copas/AsCopas.png)
#DamaCopas = pygame.load(/home/andre/python/Cartas/Copas/DamasCopas.png)
#ReiCopas = pygame.load(/home/andre/python/Cartas/Copas/ReiCopas.png)
#ValeteCopas = pygame.load(/home/andre/python/Cartas/Copas/ValeteCopas.png)

#2Espada = pygame.load(/home/andre/python/Cartas/Espadas/2Espada.png)
#3Espada = pygame.load(/home/andre/python/Cartas/Espadas/3Espada.png)
#4Espada = pygame.load(/home/andre/python/Cartas/Espadas/4Espada.png)
#5Espada = pygame.load(/home/andre/python/Cartas/Espadas/5Espada.png)
#6Espada = pygame.load(/home/andre/python/Cartas/Espadas/6Espada.png)
#7Espada = pygame.load(/home/andre/python/Cartas/Espadas/7Espada.png)
#8Espada = pygame.load(/home/andre/python/Cartas/Espadas/8Espada.png)
#9Espada = pygame.load(/home/andre/python/Cartas/Espadas/9Espada.png)
#10Espada = pygame.load(/home/andre/python/Cartas/Espadas/10Espada.png)
#AsEspada = pygame.load(/home/andre/python/Cartas/Espadas/AsEspada.png)
#DamaEspada = pygame.load(/home/andre/python/Cartas/Espadas/DamaEspada.png)
#ReiEspada = pygame.load(/home/andre/python/Cartas/Espadas/ReiEspada.png)
#ValeteEspada = pygame.load(/home/andre/python/Cartas/Espadas/ValeteEspada.png)

#2Ouro = pygame.load(/home/andre/python/Cartas/Ouros/2Ouro.png)
#3Ouro = pygame.load(/home/andre/python/Cartas/Ouros/3Ouro.png)
#4Ouro = pygame.load(/home/andre/python/Cartas/Ouros/4Ouro.png)
#5Ouro = pygame.load(/home/andre/python/Cartas/Ouros/5Ouro.png)
#6Ouro = pygame.load(/home/andre/python/Cartas/Ouros/6Ouro.png)
#7Ouro = pygame.load(/home/andre/python/Cartas/Ouros/7Ouro.png)
#8Ouro = pygame.load(/home/andre/python/Cartas/Ouros/8Ouro.png)
#9Ouro = pygame.load(/home/andre/python/Cartas/Ouros/9Ouro.png)
#10Ouro = pygame.load(/home/andre/python/Cartas/Ouros/10Ouro.png)
#AsOuro = pygame.load(/home/andre/python/Cartas/Ouros/AsOuro.png)
#DamaOuro = pygame.load(/home/andre/python/Cartas/Ouros/DamaOuro.png)
#ReiOuro = pygame.load(/home/andre/python/Cartas/Ouros/ReiOuro.png)
#ValeteOuro = pygame.load(/home/andre/python/Cartas/Ouros/ValeteOuro.png)

#2Paus = pygame.load(/home/andre/python/Cartas/Paus/2Paus.png)
#3Paus = pygame.load(/home/andre/python/Cartas/Paus/3Paus.png)
#4Paus = pygame.load(/home/andre/python/Cartas/Paus/4Paus.png)
#5Paus = pygame.load(/home/andre/python/Cartas/Paus/5Paus.png)
#6Paus = pygame.load(/home/andre/python/Cartas/Paus/6Paus.png)
#7Paus = pygame.load(/home/andre/python/Cartas/Paus/7Paus.png)
#8Paus = pygame.load(/home/andre/python/Cartas/Paus/8Paus.png)
#9Paus = pygame.load(/home/andre/python/Cartas/Paus/9Paus.png)
#10Paus = pygame.load(/home/andre/python/Cartas/Paus/10Paus.png)
#AsPaus = pygame.load(/home/andre/python/Cartas/Paus/AsPaus.png)
#DamaPaus = pygame.load(/home/andre/python/Cartas/Paus/DamaPaus.png)
#ReiPaus = pygame.load(/home/andre/python/Cartas/Paus/ReiPaus.png)
#ValetePaus = pygame.load(/home/andre/python/Cartas/Paus/ValetePaus.png)

#TrazPreto = pygame.load(/home/andre/python/Cartas/card back black.png)


#screen.blit (2Ouro, (30, 20));


'''
3 - Espadas
2 - Copas
1 - Ouros
0 - Paus

11 - Valete
12 - Rainha
13 - Rei
'''


class Carta:
    listaDeNaipes = ["Paus", "Ouros", "Copas", "Espadas"]
    listaDePosicoes = ["narf", "Ás", "2", "3", "4", "5", "6", "7", "Valete", "Rainha", "Rei"]
    def __init__(self, naipe=0, posicao=0):
        self.naipe = naipe
        self.posicao = posicao

# método init omitido
    def __str__(self):
        return (self.listaDePosicoes[self.posicao] + " de " + self.listaDeNaipes[self.naipe])

    def __cmp__(self, other):
  # verificar os naipes
        if self.naipe > other.naipe: return 1
        if self.naipe < other.naipe: return -1
  # as cartas têm o mesmo naipe... verificar as posições
        if self.posicao > other.posicao: return 1
        if self.posicao < other.posicao: return -1
  # as posições são iguais... é um empate
        return 0

class Baralho:
    def __init__(self):
        self.cartas = []
        for naipe in range(4):
            for posicao in range(1, 11):
                self.cartas.append(Carta(naipe, posicao))

    def imprimirBaralho(self):
        for carta in self.cartas:
            print(carta)

    def __str__(self):
        s = ""
        for i in range(len(self.cartas)):
            s = s + " "*i + str(self.cartas[i]) + "\n"
        return s

    def embaralhar(self):
        nCartas = len(self.cartas)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

    def pegaCarta(self):
        self.mao = []
        ind = self.cartas.pop(0)
        self.mao.append(ind)

    def minhaMao(self):
        minhaMao = self.cartas[0:3]
        for carta in minhaMao:
            print(carta)
        del self.cartas[0:3]

    def computerMao(self):
        computerMao = self.cartas[0:3]
        for carta in computerMao:
            print(carta)
        del self.cartas[0:3]



