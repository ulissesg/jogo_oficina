#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pc_simples import *

''' Programa do aviao '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

#(LARGURA, ALTURA) = (600, 400)
#tela = criar_tela_base(LARGURA, ALTURA) #descomente isso


'''==================='''
'''# Definições de dados: '''


''' Aviao eh um Pc_simples
interp. representa um aviao com suas posicoes e velocidades.
'''
#EXEMPLOS:
AVIAO_INICIAL = Pc_simples(0, 200, 1, -1)
AVIAO_INICIAL2 = Pc_simples(600, 50, -1, -1)
AVIAO_MEIO = Pc_simples(300, 200, 1, 1)
AVIAO_FINAL = Pc_simples(300, 400, 1, 1)

#TEMPLATE
'''
def fn_para_aviao(av):
    ... av.x
        av.y
        av.dx
        av.dy
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


