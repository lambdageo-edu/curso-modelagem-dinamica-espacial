# Encontro 10 — Dados para o modelo: do mapa à grade com o DisSCube

O aluno sai do encontro sabendo de onde vêm as variáveis de um espaço celular. No encontro 9 elas vieram prontas. Aqui ele as produz a partir de camadas comuns (raster de classes, linhas, pontos, polígonos), com um arquivo TOML que declara a grade, as fontes e as variáveis. Lê o registro da execução, confere o resultado com o TerraME e entrega a grade a um modelo do DisSModel. A grade do projeto fica como tarefa.

**Notebook:** [encontro10_disscube.ipynb](../notebooks/encontro10_disscube.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 25 de exposição, 60 de prática, 10 de fechamento |
| Material | Notebook `encontro10_disscube.ipynb` (32 células, roda em cerca de 12 s, incluindo o download) |
| Ferramenta | `disscube` 0.6.0 (PyPI), com o extra `dissmodel` |
| Dados | Exemplo Amazônia do pacote `gis` do TerraME (PRODES simplificado, rodovias, portos, terras indígenas), lido do GitHub do TerraME num commit fixo |
| Arquivo TOML | `benchmarks/terrame_fill/amazonia.toml` do `disscube-benchmark` v1.1.0 (DOI 10.5281/zenodo.23366475) |
| Referência | O espaço celular do TerraME para o mesmo exemplo, `goldens/fill/amazonia_terrame.csv` do `luccme-goldens` v1.1.0 |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, cap. 28; documentação do DisSCube (guia dos arquivos TOML e correspondência entre o `fill` do TerraME e os operadores); Ferreira et al. (2020), sobre o Brazil Data Cube |

**Objetivos**

1. Associar cada variável de um espaço celular ao tipo de camada de origem e à operação que a produz.
2. Explicar por que a grade é declarada antes dos dados, e o que se perde quando ela não está explícita.
3. Ler e rodar um arquivo TOML: grade, fontes com hash, variáveis.
4. Usar o registro da execução para dizer exatamente como uma variável foi feita.
5. Conferir uma variável derivada contra uma referência e explicar uma diferença de definição.
6. Entregar a grade a um modelo do DisSModel.

## Antes da aula

- [ ] Instalar o DisSCube: `pip install "disscube[dissmodel]==0.6.0"`. No Colab, a primeira célula do notebook instala tudo sozinha; o selo **Abrir no Colab** fica no topo do notebook.
- [ ] Conferir acesso a `raw.githubusercontent.com` (fontes do TerraME, TOML do benchmark e referência do `luccme-goldens`).
- [ ] Rodar o notebook do professor. Números que não mudam: grade de 72 × 52 = 3.744 células de 50 km; 2.174 células com dado do PRODES; diferença contra o TerraME menor que 10⁻¹⁰ nas frações do PRODES, até 0,004 em `protected`, menos de 1 mm em `distports`; em `distroads`, média de 300 m, máximo de 18 km e 79,2% das células a até 100 m; fração em corte raso de 28% (até 25 km da rodovia) a 0,7% (200 a 400 km).
- [ ] **Rodar o modelo do "para casa" com uma área de teste**, ao menos uma vez, na rede da sala. Ele lê o MapBiomas no Google Cloud Storage, o que não pôde ser testado ao preparar este material (ver Achados). Se não funcionar, avisar a turma e indicar um caso pronto.
- [ ] Ter à mão as fichas do encontro 8 com os drivers de cada projeto (Pergunta 1).

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | "No encontro 9 a tabela veio pronta. Quem fez essa tabela, e como?" | — |
| 5–30 | Exposição | A grade como garantia; o `fill` do TerraME e seus operadores; cubo de dados; fontes abertas; o arquivo TOML | — |
| 30–40 | Prática | Os tipos de variável do lab01 e do exemplo Amazônia; drivers do projeto | Parte 1 |
| 40–55 | Prática | Ler o TOML: grade, fontes, variáveis; `validate` e `run`; o mapa | Partes 2 e 3 |
| 55–65 | Prática | `run.json`, `spec_hash`, rodar de novo, mudar a resolução | Parte 4 |
| 65–80 | Prática | Conferir com o TerraME; vértice × segmento | Parte 5 |
| 80–90 | Prática | `to_raster_backend`; a máscara; desmatamento × distância | Parte 6 |
| 90–100 | Fechamento | Apresentar o "para casa": cada aluno escreve o `[grid]` da sua área antes de sair | Para casa |

Se o tempo apertar, a Parte 4 pode ficar só na primeira tabela (sem a mudança de resolução). O fechamento não deve ser cortado: escrever o retângulo e a resolução da própria área em sala evita que a tarefa empaque no primeiro passo.

## Exposição (25 min, cerca de 8 slides)

**1. A grade como garantia (6 min).** Começar pelo achado do encontro 9: as coordenadas do espaço celular do Acre não batem com o `.prj` e o estado aparece cerca de 3° a leste. O modelo funcionou, mas nenhuma camada nova pode ser sobreposta sem antes descobrir e corrigir o erro. Num TOML, a grade (projeção, retângulo, tamanho da célula) é declarada antes de qualquer dado e todas as fontes são reprojetadas para ela. Se duas pessoas usam a mesma grade, as células se casam uma a uma.

**2. O `fill` do TerraME e seus operadores (7 min).** No TerraME, preencher o espaço celular é chamar `fill` com uma operação por atributo. O vocabulário é pequeno e o DisSCube o mantém:

| Pergunta a cada célula | Camada | TerraME | DisSCube |
| --- | --- | --- | --- |
| que fração é desta classe? | raster de classes | `coverage` | `percentage` |
| que fração está dentro dos polígonos? | polígonos | `area` | `area` |
| a que distância está o objeto mais próximo? | linhas ou pontos | `distance` | `distance` |
| qual a média, o máximo, o mínimo? | raster contínuo | `average`, `maximum`, `minimum` | `mean`, `max`, `min` |
| qual a classe predominante? | raster de classes | `mode` | `majority` |
| há algum objeto na célula? | qualquer | `presence` | `presence` |

A diferença não está nas operações, e sim no que acontece em volta delas: arquivo declarativo em vez de script, hash de cada fonte, registro da execução e cache pela especificação.

**3. Cubo de dados (4 min).** Uma pilha de variáveis na mesma grade, com o tempo como mais uma dimensão (`floresta_2008`, `floresta_2024`). O DisSCube guarda cada variável com a especificação que a produziu; `export` gera GeoTIFF ou netCDF e `to_raster_backend` entrega ao DisSModel.

**4. Fontes abertas (5 min).** O DisSCube lê diretamente o MapBiomas (coleção 11, 30 m, 1985 a 2025), o PRODES, o Brazil Data Cube (índices de satélite pelo catálogo STAC), o OpenStreetMap e modelos de elevação. Mostrar um caso do `disscube-grids` (Ilha do Maranhão ou BR-163): um TOML curto produz uma grade com três fontes. Cuidado com a licença de cada fonte (MapBiomas CC BY 4.0; PRODES CC BY-SA 4.0) e com o fato de que fontes diferentes definem "floresta" de jeitos diferentes.

**5. O arquivo TOML (3 min).** Três blocos: `[grid]`, `[[source]]` e `[[derive]]`. Dois comandos: `validate` (não baixa nada) e `run`. É o mesmo arquivo para 72 × 52 células ou para o Brasil inteiro.

## Prática (60 min)

O aluno não escreve o TOML em aula: lê um pronto, roda e faz uma alteração (a resolução). O notebook tem uma função `disscube(...)` que chama o mesmo comando do terminal e mostra só o resumo.

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 1. Tipos de variável | Tabela do lab01 e tabela do exemplo Amazônia, com o operador de cada variável | Poucas operações produzem todas as variáveis. Pergunta 1 |
| 2. O TOML | Hash conferido; grade de 72 × 52 células de 50 km; uma fonte com URL e hash; cinco `[[derive]]` | Um shapefile são quatro arquivos, e cada um aparece como fonte |
| 3. Rodar | `validate` lista 13 fontes e 5 variáveis; `run` em cerca de 6 s com o download; mapa das cinco variáveis | Pergunta 2 |
| 4. Registro | `run.json` com versão, hash do TOML e `spec_hash` de cada variável; a segunda execução leva 0,1 s; com células de 100 km todos os hashes mudam | Pergunta 3; ligar ao encontro 4 |
| 5. Conferência | Frações do PRODES idênticas, `protected` até 0,004, `distports` abaixo de 1 mm; `distroads` com média de 300 m e máximo de 18 km | Vértice × segmento (figura); Pergunta 4 |
| 6. Para o modelo | `RasterBackend` com cinco bandas e a máscara (2.174 células); corte raso médio cai de 28% para 0,7% com a distância | É o objeto do encontro 9; o encontro 11 ajusta os coeficientes |

**Para casa**

1. Copiar o modelo de TOML, trocar o retângulo pela área do projeto, rodar `validate` e `run`.
2. Acrescentar um driver de uma camada própria (`type = "file"`).
3. Sem área própria: usar um caso do `disscube-grids` v1.1.0.
4. Trazer para o encontro 11 a figura do `disscube plot` e o `run.json`.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Tipo de camada e operador dos drivers do projeto | Depende do projeto. Exemplos: estradas ou rios (linhas) e sedes municipais ou portos (pontos) → `distance`; unidades de conservação, terras indígenas, assentamentos, tipos de solo (polígonos) → `area`; uso da terra do MapBiomas (raster de classes) → `percentage` ou `majority`; elevação, declividade, NDVI (raster contínuo) → `mean`. Vale chamar atenção para drivers que não são camadas (preço, crédito, política): entram pela demanda ou como cenário, não pela grade |
| 2. Distâncias no retângulo todo, PRODES só onde há dado | A distância existe em qualquer ponto do plano: o DisSCube mede do centro de cada célula até o objeto mais próximo, sem recortar pela área de estudo. O PRODES só tem pixels válidos dentro da Amazônia Legal, e fora dela a fração fica sem valor. Não é um problema se o modelo souber quais células usar: a máscara da Parte 6 sai justamente da variável com dado ausente (a mesma banda `mask` que faltou no encontro 9) |
| 3. O que o `run.json` diz que a frase não diz | O arquivo exato (URL e hash), portanto a edição e o ano do PRODES; a grade (projeção, retângulo, resolução); a classe contada (código 10, corte raso); o operador; a versão do DisSCube e a data da execução. Com isso outra pessoa refaz a variável idêntica, e o `spec_hash` permite saber se duas variáveis com o mesmo nome são de fato a mesma |
| 4. Vértice ou segmento | Para um projeto novo, a distância ao segmento é a distância geométrica correta e deve ser preferida. Para reproduzir um estudo feito no TerraME, há duas saídas: medir e relatar a diferença, como na tabela, ou reproduzir a regra do vértice. Em nenhum dos casos se deve trocar silenciosamente uma pela outra: o método precisa dizer qual distância foi usada |

## Achados ao testar

Testado em 31 out 2026 com Python 3.13, disscube 0.6.0, dissmodel 0.6.6 e luccme-goldens 1.1.0. O notebook roda sem erro em cerca de 12 s, incluindo cerca de 6 s de download das fontes; com as fontes em cache, cerca de 7 s.

1. **`disscube plot` troca o modo gráfico do matplotlib** (`matplotlib.use("Agg")`) e, depois dele, os gráficos do notebook deixam de aparecer, sem nenhum erro. O notebook volta ao modo do Jupyter com `%matplotlib inline` logo depois do `plot`. Vale corrigir no `disscube`: desenhar com uma `Figure` própria em vez de mudar o modo global.
2. **Os produtos ficam registrados com caminhos relativos à pasta em que o `run` foi chamado.** Abrir o mesmo cubo com `CubeClient` a partir de outra pasta dá "Derived variable not found on disk". No notebook tudo roda na mesma pasta, mas um aluno que rode o `run` no terminal e abra o cubo num notebook de outra pasta vai encontrar esse erro. Vale registrar os caminhos relativos ao workspace.
3. **O modelo de TOML do "para casa" (MapBiomas) foi validado, mas não rodado.** O ambiente de preparação não alcança o Google Cloud Storage (resposta 403). O professor precisa rodá-lo antes da aula.
4. **O endereço padrão do PRODES no DisSCube 0.6.0** (`prodes_amazonia_legal_2025_v20260408.zip`, no TerraBrasilis) respondeu 404 em 31 out 2026, e com isso o caso `cases/br163/prodes.toml` do `disscube-grids` não rodou. Pode ser restrição do ambiente de preparação ou troca de edição pelo INPE. Se for troca, o DisSCube precisa de nova versão; até confirmar, o "para casa" indica o caso MapBiomas da BR-163 e não os casos do PRODES.
5. **Um shapefile vira quatro fontes no TOML** (`.shp`, `.shx`, `.dbf`, `.prj`), e o exemplo com quatro camadas tem 13 fontes. Para quem não programa, isso polui a leitura do arquivo. Vale aceitar no `disscube` uma fonte que baixe os arquivos irmãos do `.shp` automaticamente.
6. **Cada comando repete a lista inteira de fontes e variáveis.** O notebook mostra só o resumo final (a função `disscube` corta a lista). No terminal, uma opção `--quiet` ajudaria.
