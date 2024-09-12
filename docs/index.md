![logo do projeto](assets/logo.png){width="300" .center}
# Notas musicais

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmônicos.
Toda a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando tem um subcomando relacionado a cada ação que a aplicação pode realizar. Como `escalas`, `acordes` e `campo-harmonico`


### como usar?
Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run notas-musicais
```
Retornando os graus correspondentes as notas.
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```
### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma você pode alterar a escala retornada. Por exemplo, a escala de `F`:

```bash
poetry run notas-musicais escala F
```
resultado
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ F │ G  │ A   │ A# │ C │ D  │ E   │
└───┴────┴─────┴────┴───┴────┴─────┘
```
### Alterando a tonalidade

Você pode alterar a tonalidade de maior para menor, acrescentando o segundo parâmetro do CLI. Por exemplo, a escala de `G`maior:

```bash
poetry run notas-musicais escala G maior
```
resultado
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ G │ A  │ B   │ C  │ D │ E  │ F#  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

## Acordes

#### Uso básico

```bash
poetry run notas-musicais acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```
## Variações na cifra

```bash
poetry run nota-musicais acorde Cm
┏━━━┳━━━━━━┳━━━┓
┃ I ┃ III- ┃ V ┃
┡━━━╇━━━━━━╇━━━┩
│ C │ D#   │ G │
└───┴──────┴───┘
```

## Mais informações

Para descobrir mais funcionalidades do CLI, basta inserir --help no terminal:

```bash
poetry run notas-musicais --help
```