
import numpy as np
import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores

@pytest.mark.exercicio_1
def test_divisao_por_zero_tende_a_infinito():
    v1 = 3.0
    v2 = 0.0
    assert np.inf == divisao(v1, v2)

@pytest.mark.exercicio_1
def test_calculo_da_media_com_elementos_nao_numericos_na_lista_e_calcula_a_media_dos_elementos_numericos_presentes():
    lista = [2, 2, 'abc', 'gf', 5]
    assert 3.0 == media_lista_valores(lista)

@pytest.mark.exercicio_1
def test_media_de_lista_vazia_deve_retornar_zero():
    lista_vazia = []
    assert 0.0 == media_lista_valores(lista_vazia)

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0 
    assert 12 == soma(v1, v2)

@pytest.mark.op_simples
def test_soma_dois_valores_negativos():
    v1 = -9.0
    v2 = -2.0
    assert -11.0 == soma(v1, v2)

@pytest.mark.op_simples
def test_soma_dois_valores_de_sinais_opostos():
    v1 = -9.0
    v2 = +2.0
    assert -7.0 == soma(v1, v2)

@pytest.mark.op_simples
def test_subtracao_dois_valores_positivos():
    v1 = 10.0
    v2 = 12.0
    assert -2 == sub(v1, v2)

@pytest.mark.op_simples
def test_divisao_dois_numeros_positivos():
    v1 = 12
    v2 = 10
    assert 1.2 == divisao(v1, v2)

@pytest.mark.op_simples
def test_multiplicacao_dois_numeros_positivos():
    v1 = 15.0
    v2 = 2.0
    assert 30 == multiplicacao(v1, v2)

@pytest.mark.op_complexas
def test_media_lista_valores_positivos():
    lista = [1, 3, 5, 7, 9]
    assert 5.0 == media_lista_valores(lista)