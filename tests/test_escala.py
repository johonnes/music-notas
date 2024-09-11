from pytest import mark, raises

from notas_musicais.escala import ESCALAS, NOTAS, escala


def test_escala_letra_minuscula():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'
    # Act - chamar o que testar
    result = escala(tonica, tonalidade)
    # Assert
    assert result


def test_escala_nota_inexistente():
    tonica = 'x'
    tonalidade = 'maior'
    messagem_erro = f'Essa nota não existe, tente uma dessas{NOTAS}'
    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    assert messagem_erro == error.value.args[0]


def test_tonalidade_inexistente():
    tonica = 'c'
    tonalidade = 'tonalidade'
    messagem_erro = (
        f'Essa escala não existe, tente uma dessas{list(ESCALAS.keys())}'
    )
    with raises(KeyError) as error:
        escala(tonica, tonalidade)
    assert messagem_erro == error.value.args[0]


@mark.parametrize(
    'tonica,esperado',
    [
        ('c', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('c#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('d', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('d#', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('e', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('f', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('f#', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('g', ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('g#', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('a', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('a#', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('b', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
    ],
)
def test_notas_maiores_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado


@mark.parametrize(
    'tonica,esperado',
    [
        ('c', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('c#', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('d', ['D', 'E', 'F', 'G', 'A', 'A#', 'C']),
        ('d#', ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#']),
        ('e', ['E', 'F#', 'G', 'A', 'B', 'C', 'D']),
        ('f', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
        ('f#', ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']),
        ('g', ['G', 'A', 'A#', 'C', 'D', 'D#', 'F']),
        ('g#', ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#']),
        ('a', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
        ('a#', ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#']),
        ('b', ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']),
    ],
)
def test_notas_menores_corretas(tonica, esperado):
    resultado = escala(tonica, 'menor')
    assert resultado['notas'] == esperado
