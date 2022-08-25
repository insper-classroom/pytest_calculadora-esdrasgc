import numpy as np

def soma(va: float, vb: float):
    ''' Função que retorna a soma entre dois valores
    '''
    return va + vb

def sub(va: float, vb: float):
    ''' Função que retorna a subtração entre dois valores
    '''
    return va - vb

def multiplicacao(va: float, vb: float):
    ''' Função que retorna a multiplicação entre dois valores
    '''
    return va * vb

def divisao(va: float, vb: float):
    ''' Função que retorna a divisão entre dois valores
    '''
    try: 
        result = va/ vb
    except ZeroDivisionError:
        result = np.inf
    return result

def media_lista_valores(v:list):
    ''' Função que retorna a média entre N valores'''
    lista = []
    for element in v:
        if isinstance(element, int) or isinstance(element, float):
            lista.append(element)

    if len(lista) == 0:
        return 0

    return np.mean(lista)
