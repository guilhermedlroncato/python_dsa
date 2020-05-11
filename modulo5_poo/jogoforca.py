# -*- coding: utf-8 -*-
# Implementação do Jogo da Forca
# Programação Orientada a Objetos

import random
import simpleaudio as sa
from time import sleep
from os import system, name

class Forca:
    def __init__(self, palavra, posicao):
        self.palavra = palavra
        self.letreiro = ['_ '] * len(palavra)
        self.palpites = []
        self.acertos = []
        self.erros = []
        self.posicao = posicao
        self.somacerto = "D:\\Python\\DSA\\modulo5_poo\\aplausos5.wav"
        self.somerro = "D:\\Python\\DSA\\modulo5_poo\\vaia1.wav"
        self.tabuleiro = [
            ''' 
                +----------+
                |          |
                |
                |
                |
                |
                |
                |
                |
            ========================= 
            ''',
            ''' 
                +----------+
                |          |
                |          O
                |
                |
                |
                |
                |
                |
            ========================= 
            ''',
            ''' 
                +----------+
                |          |
                |          O
                |          |
                |
                |
                |
                |
                |
            ========================= 
            ''',
            ''' 
                +----------+
                |          |
                |          O
                |         /| 
                |          
                |
                |
                |
                |
            ========================= 
            ''',
            ''' 
                +----------+
                |          |
                |          O
                |         /|\ 
                |          
                |
                |
                |
                |
            ========================= 
            ''',
            ''' 
                +----------+
                |          |
                |          O
                |         /|\ 
                |         /          
                |
                |
                |
                |
            ========================= 
            ''',
            ''' 
                +----------+
                |          |
                |          O
                |         /|\ 
                |         / \         
                |
                |
                |
                |
            ========================= 
            '''
        ]
    
    def atualizaTabuleiro(self):
        print(self.tabuleiro[self.posicao])        
        print('')
        for i, v in enumerate(self.letreiro): 
            if i == 0:
                print('            ' + v, end = ' ')
            else:
                print(v, end = ' ')
        print('\n\n')
        print('            Letras Informadas: ', self.palpites)

    def verificaLetra(self, letra):
        cont = 0

        verifica = [v for v in self.palavra if v == letra]
        
        for v in verifica: 
            self.acertos.append(v)

        for i, va in enumerate(self.palavra):
            if va == letra:
                self.letreiro[i] = va
                if cont == 0:
                    wave_obj = sa.WaveObject.from_wave_file(self.somacerto)
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                    cont += 1                                        
        
        self.palpites.append(letra)
        if len(verifica) == 0:
            self.erros.append(letra)
            self.posicao = len(self.erros)
            if cont == 0:
                wave_obj = sa.WaveObject.from_wave_file(self.somerro)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                cont += 1
    
    def verificaFimJogo(self):
        if len(self.palavra) == len(self.acertos):
            return 'ganhou'
        elif len(self.erros) == 6:
            return 'perdeu'
        else:
            return ''

def main():
    system('cls')    
    palavra = input('Digite a palavra a ser descoberta: ')
    system('cls')
    jogo = Forca(palavra, 0)
    ganhou = ''
    perdeu = ''
    while ganhou == '' and perdeu == '':    
        system('cls')
        jogo.atualizaTabuleiro()
        letra = input('\n            Informe uma Letra: ')
        jogo.verificaLetra(letra)
        resultado = jogo.verificaFimJogo()
        if resultado == 'ganhou':
            ganhou = resultado
            system('cls')
            jogo.atualizaTabuleiro()               
            system('cls')         
            print('\n\n\n\n\n\n\n\n\n\n\n\n                           +================================================================+')
            print('                           +                      VOCÊ GANHOU DANADO!!                      +')
            print('                           +================================================================+')
            wave_obj = sa.WaveObject.from_wave_file("D:\\Python\\DSA\\modulo5_poo\\aplausos6.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
        if resultado == 'perdeu':
            perdeu = resultado
            system('cls')
            jogo.atualizaTabuleiro()               
            system('cls')      
            print('\n\n\n\n\n\n\n\n\n\n\n\n                           +================================================================+')
            print('                           +                  VOCÊ PERDEU!! BUA BUA BAU!!                   +')
            print('                           +================================================================+')    
            print(f'                                           ==>> A palavra era: {jogo.palavra.upper()} <<==  ') 
            wave_obj = sa.WaveObject.from_wave_file("D:\\Python\\DSA\\modulo5_poo\\oh2.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()     
        
system('cls')
print('\n\n\n\n\n\n\n\n\n\n\n\n                           +================================================================+')
print('                           +                          JOGO DA FORCA                         +')
print('                           +================================================================+')
sleep(3)
opcao = ''
while opcao != 'n':
    main()
    sleep(3)
    system('cls')
    opcao = input('Deseja jogar novamente (s/n): ')
exit()

