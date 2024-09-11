from rich import print
from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.escala import escala

console = Console()
app = Typer()


@app.command()
def escalas(tonica=Argument('c'), tonalidade=Argument('maior')):
    table = Table()
    notas, graus = escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)
    table.add_row(*notas)
    console.print(table)
