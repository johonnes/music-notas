from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_cli():
    result = runner.invoke(app)
    assert result.exit_code == 0
