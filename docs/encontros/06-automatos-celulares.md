# Encontro 6 — Autômatos celulares

O aluno sai do encontro sabendo nomear os quatro ingredientes de um autômato celular (espaço, estado, vizinhança, regra), tendo visto que a borda da grade muda o resultado, e tendo observado um padrão de paisagem emergir de uma regra local: o limiar de conectividade da floresta num incêndio. É a ponte entre a dinâmica de sistemas (encontro 5) e os modelos de uso da terra (a partir do encontro 8).

**Notebook:** [encontro06_automatos_celulares.ipynb](../notebooks/encontro06_automatos_celulares.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 25 de exposição, 55 de prática, 15 de fechamento |
| Material | Notebook `encontro06_automatos_celulares.ipynb` (30 células, roda em cerca de 20 s) |
| Modelos | `GameOfLife` (vetor), `GameOfLifeRaster` e `FireModelRaster` do `dissmodel-ca` v0.2.0 |
| Referência | Grade do planador do TerraME (`life_glider`) no `terrame-goldens` v0.1.0, lida do GitHub |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, Caps. 18 e 24 |

**Objetivos**

1. Identificar espaço celular, estado, vizinhança e regra num modelo.
2. Distinguir vizinhança de von Neumann e de Moore, e borda fechada de periódica.
3. Explicar comportamento emergente com o planador do Jogo da Vida.
4. Comparar o mesmo modelo em grade vetorial e raster, em tempo de execução.
5. Relacionar conectividade da paisagem a um limiar de percolação.

## Antes da aula

- [ ] O ambiente do encontro 4 já tem o `dissmodel-ca` v0.2.0; nada a instalar. No Colab, a primeira célula do notebook instala tudo sozinha; o selo **Abrir no Colab** fica no topo do notebook.
- [ ] Conferir acesso a `raw.githubusercontent.com` (Parte 5). Sem rede, copiar `goldens/ca/grids/life_glider.csv.gz` do `terrame-goldens` v0.1.0 para a pasta da turma.
- [ ] Rodar o notebook do professor. Números que não mudam: 2.576 células vivas no passo 200, zero células diferentes do TerraME. Os tempos variam: cerca de 0,2 s por passo em vetor e 0,0001 s em raster numa grade 30 × 30, e a razão oscila entre 800× e 2.300× em execuções seguidas na mesma máquina, porque o passo em raster é curto demais para medir com precisão. Falar em "cerca de mil vezes".
- [ ] Trazer em papel quadriculado um blinker (três células em linha) para a turma aplicar a regra do Jogo da Vida à mão antes de ver no computador.
- [ ] Recolher os diagramas de estoque e fluxo pedidos no encontro 5 e escolher dois para comentar na abertura.

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | Dois diagramas de estoque e fluxo da turma; pergunta: "e se cada pedaço do território tivesse o seu estoque?" | — |
| 5–30 | Exposição | Os quatro ingredientes; vizinhanças; borda; emergência; vetor e raster; o blinker à mão no papel | — |
| 30–38 | Prática | Grade vetorial: uma linha por célula, identificador "linha-coluna" | Parte 1 |
| 38–45 | Prática | Vizinhanças e bordas desenhadas; pergunta 1 (a divisa com o Pará) | Parte 2 |
| 45–58 | Prática | Planador: forma que anda; borda periódica × fechada | Parte 3 |
| 58–65 | Prática | Mesmo modelo em raster: cerca de mil vezes mais rápido; 40 mil células em segundos | Parte 4 |
| 65–70 | Prática | Comparação com o TerraME, célula a célula, em 100 passos | Parte 5 |
| 70–85 | Prática | Incêndio e conectividade: três mapas e a curva de percolação | Parte 6 |
| 85–100 | Fechamento | Pergunta 3 em turma; ligar o limiar à fragmentação e ao desmatamento a partir de estradas; exercícios | Para casa |

Se o tempo apertar, a Parte 5 pode ser só mostrada (o encontro 5 já fez uma comparação com o TerraME). A Parte 6 não deve ser cortada: é a que liga o autômato à paisagem e prepara o encontro 8.

## Exposição (25 min, cerca de 7 slides)

**1. Do lugar ao território (3 min).** No encontro 5 havia um estoque; agora cada célula tem o seu, e o que acontece numa célula depende das vizinhas. Isso é a primeira lei da geografia (Tobler) em forma de regra.

**2. Os quatro ingredientes (7 min).**

| Ingrediente | Escolha | Exemplo em uso da terra |
| --- | --- | --- |
| Espaço celular | forma e tamanho das células; vetor ou raster | grade de 5 km sobre o Maranhão |
| Estado | valor guardado em cada célula | classe de uso (floresta, pasto, agricultura) ou fração de cada classe |
| Vizinhança | quem influencia cada célula | as 8 células em volta; ou as células a até 20 km |
| Regra | como o estado muda | uma célula de floresta vizinha de pasto tem mais chance de ser desmatada |

Aplicar a regra do Jogo da Vida ao blinker no papel: três células em linha viram três células em coluna, e voltam.

**3. Vizinhança e borda (5 min).** Von Neumann (4) e Moore (8). A borda é uma escolha do modelo, não um detalhe: fechada (o mundo acaba), periódica (toro, comum em modelos teóricos e no TerraME) ou com um anel de células externas lidas dos dados. Para estudos sobre territórios reais, a periódica quase nunca faz sentido.

**4. Emergência (5 min).** Regras locais e simples produzem padrões globais que ninguém programou: o planador anda, o fogo para ou atravessa a paisagem dependendo da conectividade. Wolfram, Toffoli e Margolus estudaram isso em autômatos abstratos; a modelagem ambiental usa a mesma ideia (crescimento urbano, como o SLEUTH; desmatamento, como o Dinamica EGO).

**5. Vetor e raster no DisSModel (5 min).** O mesmo modelo existe nas duas formas:

| | Vetor (`CellularAutomaton`) | Raster (`RasterCellularAutomaton`) |
| --- | --- | --- |
| Dados | `GeoDataFrame`, uma linha por célula | matrizes NumPy no `RasterBackend` |
| Regra | `rule(idx)`: uma célula por vez | `rule(arrays)`: a grade inteira de uma vez |
| Serve para | polígonos irregulares, municípios, setores | grades regulares grandes |
| Velocidade (30 × 30) | cerca de 0,2 s por passo | cerca de 0,0001 s por passo |

O custo do vetor é Python célula a célula, não a geometria. No encontro 10 os dados chegam como raster, pelo DisSCube.

## Prática (55 min)

Como no encontro 5, o notebook traz funções de apoio que o aluno só usa: `rodar` (guarda "fotos" da grade em alguns passos), `mostrar` (desenha as fotos) e `como_matriz` (converte a grade vetorial numa matriz). As fotos usam a linha 0 embaixo, como no mapa.

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 1. Espaço celular | Grade 5 × 5; a tabela do GeoPandas e o mapa com os identificadores "linha-coluna" | Uma célula é uma linha de tabela com geometria |
| 2. Vizinhança | Quatro desenhos: von Neumann (4), Moore (8), Moore no canto com borda fechada (3) e periódica (8) | A borda periódica liga o canto aos outros três cantos |
| 3. Planador | Grade 12 × 12; a forma se repete a cada 4 passos, deslocada na diagonal. Com borda periódica, sai por um canto e volta pelo oposto; com fechada, vira um bloco parado no canto | Mesma regra, outro resultado: a borda faz parte do modelo |
| 4. Raster | Cronômetro: vetor cerca de mil vezes mais lento (a razão oscila entre 800× e 2.300×). Grade 200 × 200 aleatória (30% vivas): 2.576 vivas no passo 200 | Mesma regra escrita sobre matrizes |
| 5. TerraME | Lê a grade do planador do TerraME (30 × 30, 101 passos) e compara: zero células diferentes | Comparação célula a célula só vale para modelo determinístico |
| 6. Incêndio | Fogo a partir da borda esquerda; mapas com 55%, 60% e 65% de floresta; curva com 17 densidades × 10 sementes (cerca de 3 s): o salto fica entre 0,55 e 0,65 | O limiar (cerca de 0,59) emerge da conectividade, não do código |

**Para casa**

1. Refazer a curva com vizinhança de Moore (`incendio(p, semente, vizinhanca=DIRS_MOORE)`) e dizer se o limiar sobe ou desce.
2. Jogo da Vida em raster começando com 10%, 30% e 50% de vivas: tabela de vivas no passo 200.
3. Uma frase sobre um modelo de uso da terra da própria área: qual seria o estado de cada célula e quais vizinhas importam.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Borda para um modelo do Maranhão; divisa com o Pará | Periódica não: ligaria o litoral ao Tocantins. Fechada é a mais simples, mas as células da divisa perdem vizinhas e ficam artificialmente isoladas. O ideal é uma faixa de células além da divisa, lidas dos dados (MapBiomas cobre o país inteiro), que influenciam mas não são simuladas |
| 2. O que mudou no planador com borda fechada? | Ao chegar ao canto, perde vizinhas e vira um bloco 2 × 2 parado. A regra foi a mesma; mudou o espaço. Efeito de borda é resultado do modelo, não do processo estudado |
| 3. Uma pergunta de pesquisa com esse modelo | Respostas abertas. Exemplos: dispersão de uma espécie entre fragmentos de mangue; avanço do desmatamento a partir de estradas; propagação de fogo no Cerrado conforme a fragmentação |
| 4. Onde a faixa entre sementes é mais larga | Perto do limiar (0,55 a 0,62): lá, a posição exata das poucas células que ligam os fragmentos decide se o fogo passa. Longe dele, todas as rodadas concordam. Perto de um limiar, uma rodada só não diz nada; é preciso várias sementes |

**Para casa, com os números do teste**

1. Com Moore o limiar **desce** para cerca de 0,41 (40% de floresta já queima 38% em média; 45% queima 92%). Com 8 vizinhas, o fogo passa também pelas diagonais e a floresta fica "conectada" com menos células.
2. Vivas no passo 200 (grade 200 × 200, semente 1): 1.610 começando com 10%, 2.576 com 30% e 3.129 com 50%.

## Achados ao testar

Testado em 31 out 2026 com Python 3.13, dissmodel 0.6.6, dissmodel-ca 0.2.0 e terrame-goldens 0.1.0. O notebook roda sem erro em cerca de 20 s (a maior parte é o Jogo da Vida vetorial). Pontos para o `dissmodel-ca`:

1. **`grid_neighbors` está num módulo privado** (`dissmodel_ca.models._neighborhood`). É a única forma de mostrar a borda periódica num desenho, e o notebook o importa assim. Vale expô-lo em `dissmodel_ca` ou mover para o `dissmodel.geo`.
2. **`GameOfLife.initialize_patterns` sorteia a posição com `random` sem semente** e supõe grade quadrada; `initialize` usa semente fixa 42 sem parâmetro. O notebook põe o planador à mão. Para a aula do encontro 4 isso é um contraexemplo útil; para o pacote, aceitar `seed`.
3. **A vizinhança do `FireModelRaster` não é parâmetro:** `self.dirs` é fixado no `setup`, e o notebook troca depois de criar o modelo. Um `neighborhood="moore"` no `setup` seria mais claro.
4. **Convenção de linhas:** no `vector_grid`, a linha cresce com o y (linha 0 embaixo); num `imshow` padrão, a linha 0 fica em cima. O notebook usa `origin="lower"`. Documentar a convenção junto do `parse_idx` evitaria figuras espelhadas.
