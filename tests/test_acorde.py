from pytest import mark

from notas_musicais.acordes import acorde

"""
Entrada
acorde C

Esperado:
I - III - V
C    E    G

{'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
"""


@mark.parametrize(
    'nota,esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('Cm+', ['C', 'D#', 'G#']),
        ('C°', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('F#', ['F#', 'A#', 'C#']),
    ],
)
def test_acorde_deve_retornar_as_notas_correspondentes(nota, esperado):
    notas, _ = acorde(nota).values()

    assert esperado == notas


@mark.parametrize(
    'nota,esperado',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('Cm+', ['I', 'III-', 'V+']),
        ('C°', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
    ],
)
def test_acorde_deve_retornar_os_graus_correspondentes(nota, esperado):
    _, graus = acorde(nota).values()

    assert esperado == graus
