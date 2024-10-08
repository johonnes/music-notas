<img src="https://music-notas.readthedocs.io/pt-br/latest/assets/logo.png" width="200">

# Notas music

[![Documentation Status](https://readthedocs.org/projects/music-notas/badge/?version=latest)](https://music-notas.readthedocs.io/pt-br/latest/?badge=latest)[![CI](https://github.com/johonnes/music-notas/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/johonnes/music-notas/actions/workflows/pipeline.yaml)<a href="https://codecov.io/gh/johonnes/music-notas" > 
 <img src="https://codecov.io/gh/johonnes/music-notas/graph/badge.svg?token=VTY5KDYYMD"/> 
 </a>

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmônicos.
Toda a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando tem um subcomando relacionado a cada ação que a aplicação pode realizar. Como `escalas`, `acordes` e `campo-harmonico`

## Como instalar o projeto

Para instalação do CLI do projeto recomendamos que use o pipx para fazer essa instalação:

```bash
pipx install notas-musicais
```

## como usar?

## Escalas

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
notas-musicais
```

Retornando os graus correspondentes as notas.

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma você pode alterar a escala retornada. Por exemplo, a escala de `F`:

```bash
notas-musicais escala F
```

resultado
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ F │ G  │ A   │ A# │ C │ D  │ E   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

 ##### Alterando a tonalidade

Você pode alterar a tonalidade de maior para menor, acrescentando o segundo parâmetro do CLI. Por exemplo, a escala de `G`maior:

```bash
notas-musicais escala G maior
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

### Uso básico

```bash
notas-musicais acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

#### Variações na cifra

```bash
nota-musicais acorde Cm
┏━━━┳━━━━━━┳━━━┓
┃ I ┃ III- ┃ V ┃
┡━━━╇━━━━━━╇━━━┩
│ C │ D#   │ G │
└───┴──────┴───┘
```

## Campo harmonico

Você pode chamar os campos harmônicos via o subcomando `campo-harmonico`. Por exemplo:

```bash
notas-musicais campo-harmonico
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os parâmetros utilizados são a tônica de C e o campo harmônico maior.

### Alterações nos campos harmônicos

Você pode alterar os parâmetros da tônica e da tonalidade.

notas-musicais campo-harmonico [TONICA] [TONALIDADE]
Alteração na tônica do campo
Um exemplo com o campo harmônico de E:

```bash
notas-musicais campo-harmonico E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Alteração da tonalidade do campo

Um exemplo utilizando o campo harmônico de E na tonalidade menor:

```bash
notas-musicais campo-harmonico E menor
┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informações

Para descobrir outras opções, você pode usar a flag --help:

```bash
notas-musicais --help
                                                                       
 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...

╭─ Commands ──────────────────────────────────────────────────────────╮
│ acorde                                                              │
│ campo-harmonico                                                     │
│ escala                                                              │
╰─────────────────────────────────────────────────────────────────────╯
```

### Mais informações sobre os subcomandos

As informações sobre os subcomandos podem ser acessadas usando a flag --help após o nome do parâmetro. Um exemplo do uso do help nos campos harmônicos:

```bash
notas-musicais --help
 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE] 
                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica do campo harmônico           │
│                                 [default: c]                        │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmônico       │
│                                 [default: maior]                    │
╰─────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                         │
╰─────────────────────────────────────────────────────────────────────╯
```
