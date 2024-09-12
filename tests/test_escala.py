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
    'tonica,tonalidade, esperado',
    [
        ('c', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('c#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('d', 'maior', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('d#', 'maior', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('e', 'maior', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('f', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('f#', 'maior', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('g', 'maior', ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('g#', 'maior', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('a', 'maior', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('a#', 'maior', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('b', 'maior', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
        ('c', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('c#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('d', 'menor', ['D', 'E', 'F', 'G', 'A', 'A#', 'C']),
        ('d#', 'menor', ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#']),
        ('e', 'menor', ['E', 'F#', 'G', 'A', 'B', 'C', 'D']),
        ('f', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
        ('f#', 'menor', ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']),
        ('g', 'menor', ['G', 'A', 'A#', 'C', 'D', 'D#', 'F']),
        ('g#', 'menor', ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#']),
        ('a', 'menor', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
        ('a#', 'menor', ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#']),
        ('b', 'menor', ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']),
    ],
)
def test_notas_maiores_corretas(tonica, tonalidade, esperado):
    resultado = escala(tonica, tonalidade)
    assert resultado['notas'] == esperado
