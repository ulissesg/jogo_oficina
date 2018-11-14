#!/usr/bin/env python
# -*- coding: utf-8 -*-

from personagem import *

''' Programa dos asteroides '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

#(LARGURA, ALTURA) = (600, 400)
#tela = criar_tela_base(LARGURA, ALTURA) #descomente isso


'''==================='''
'''# Definições de dados: '''

''' Asteroide eh um Personagem
interp. representa um asteroide com suas posicoes e velocidades.
'''
#EXEMPLOS:
ASTEROIDE_INICIAL = Personagem(50, 0, 1, 1)
ASTEROIDE_INICIAL2 = Personagem(600, 0, -1, 1)
ASTEROIDE_MEIO = Personagem(300, 200, 1, 1)
ASTEROIDE_FINAL = Personagem(300, 400, 1, 1)

#TEMPLATE
'''
def fn_para_asteroide(ast):
    ... ast.x
        ast.y
        ast.dx
        ast.dy
'''

'''
ListaAsteroide é um desses:
    - VAZIA
    - juntar(Asteroide, ListaAsteroide)
'''
#Exemplos:
L_ASTEROIDE_1 = criar_lista(ASTEROIDE_INICIAL)
L_ASTEROIDE_INICIAL = criar_lista(
    Personagem(600, 50, -1, -1),
    Personagem(50, 0, 1, 1),
    Personagem(300, 400, 1, 1)
)

'''
#template
def fn_para_lista(lista):
    if lista.vazia:
        return ...
    else:
        ... lista.primeiro
            fn_para_lista(lista.resto)
'''

'''===================='''
''' Funções: '''


'''
tock: EstadoMundo -> EstadoMundo
Produz o próximo ...
# !!! TODO
def tock(estado):
    pass
'''


'''
desenha: EstadoMundo -> Imagem
Desenha...
# !!! TODO
def desenha(estado):
    pass
'''


'''
trata_tecla: EstadoMundo, Tecla -> EstadoMundo
Quando teclar ... produz ... <apagar caso não precise usar>
# !!! TODO
Template:

def trata_tecla(estado, tecla):
    if tecla == pg.K_SPACE:
        ... estado
    else:
        ... estado
'''


'''
trata_mouse: EstadoMundo, Int, Int, EventoMouse -> EstadoMundo:
Quando fazer ... nas posições x y no mouse produz ...   <apagar caso não precise usar>
# !!! TODO
Template:

def trata_mouse(estado, x, y, ev):

    if ev == pg.MOUSEMOTION:
        ... estado
    else:
        ... estado

'''

''' ================= '''
''' Main (Big Bang):'''


''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com ...'''
# def main(m):
#     big_bang(m, tela=tela, frequencia=XX, \
#              quando_tick=tock, \
#              desenhar=desenha, \
#              quando_tecla=..., \
#              quando_mouse=..., \
#              parar_quando=...)
#




