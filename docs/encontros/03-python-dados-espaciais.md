# Encontro 3 — Python II: grades, tabelas, mapas vetoriais e raster

O aluno sai do encontro tendo usado as quatro bibliotecas que carregam os dados de qualquer modelo espacial: NumPy (a grade como matriz), pandas (tabelas), GeoPandas (vetor) e rasterio (raster). Os dados são reais e lidos de versões fixas: focos de queimada no Maranhão, os estados do IBGE e o MapBiomas da Ilha do Maranhão, lido por janela direto do mosaico nacional.

**Notebook:** [encontro03_python_dados_espaciais.ipynb](../notebooks/encontro03_python_dados_espaciais.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 15 de exposição, 70 de prática, 10 de fechamento |
| Pré-requisito | Encontro 2 (variáveis, listas, laços, funções) |
| Material | Notebook `encontro03_python_dados_espaciais.ipynb` (38 células, roda em cerca de 4 s sem a Parte 4) |
| Dados | Focos de queimada (BDQueimadas/INPE, 5 e 6 set 2026) do repositório do livro *Geospatial Modeling with Python*; estados (IBGE) do livro *Introdução ao Geoprocessamento e Sensoriamento Remoto*; MapBiomas Coleção 11, 2024 |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, Caps. 3, 7 e 8 |

**Objetivos**

1. Tratar uma grade como matriz do NumPy: indexar, comparar e contar classes com máscaras.
2. Ler uma tabela com pandas, filtrar linhas e agrupar por categoria.
3. Ler um shapefile com GeoPandas, selecionar feições e transformar coordenadas de uma tabela em pontos.
4. Ler só uma janela de um raster grande com rasterio, contar pixels por classe e salvar o recorte.
5. Ler dados por endereços fixos (commit), como preparação para o encontro 4.

## Antes da aula

- [ ] Instalar `geopandas`, `rasterio` e `matplotlib` (no Colab, só o `rasterio` falta, e a primeira célula o instala sozinha quando o notebook roda no Colab; o selo **Abrir no Colab** fica no topo do notebook).
- [ ] Conferir que a rede do laboratório acessa `raw.githubusercontent.com` (Partes 2 e 3) e `storage.googleapis.com` (Parte 4, MapBiomas).
- [ ] **Gerar antes os recortes do MapBiomas** rodando a Parte 4 em casa, com `ANO = 2024` e `ANO = 1985`, e distribuir `mapbiomas_ilha_2024.tif` e `mapbiomas_ilha_1985.tif`. Se a rede da aula falhar, os alunos abrem o arquivo local (a última célula mostra como).
- [ ] Rodar a Parte 4 completa uma vez e anotar a tabela de classes: ela não pôde ser testada ao preparar o material (ver Achados), e as respostas da pergunta 4 dependem dela.
- [ ] Números que não mudam nas Partes 1 a 3: 27 células de floresta na grade; 1.260 focos, 1.092 no Cerrado, 118 com FRP acima de 100 MW; Barra do Corda com 110 focos; Maranhão com 329.651 km².

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | Retomar o encontro 2: listas guardam valores; hoje, grades, tabelas e mapas | — |
| 5–20 | Exposição | Raster × vetor; matriz, tabela, geometria; sistema de coordenadas; ler só uma janela de um arquivo grande | — |
| 20–35 | Prática | NumPy: a grade de classes, máscara, contagem, área; pergunta 1 | Parte 1 |
| 35–55 | Prática | pandas: os focos de queimada; filtrar, agrupar, gráfico de barras; pergunta 2 | Parte 2 |
| 55–70 | Prática | GeoPandas: estados; o Maranhão; focos como pontos no mapa; pergunta 3 | Parte 3 |
| 70–90 | Prática | rasterio: janela do MapBiomas, tabela de classes, mapa, recorte salvo; pergunta 4 | Parte 4 |
| 90–100 | Fechamento | O mesmo dado em quatro formas; ponte para o encontro 4 (o endereço com commit é uma forma de reprodutibilidade) | Para casa |

Se a rede falhar na Parte 4, usar o recorte distribuído e seguir. Se o tempo apertar, a Parte 3 pode parar no mapa dos estados; os pontos sobre o Maranhão ficam para casa.

## Exposição (15 min, cerca de 5 slides)

**1. Raster e vetor (5 min).**

| | Raster | Vetor |
| --- | --- | --- |
| O que é | grade regular de pixels, cada um com um valor | feições (pontos, linhas, polígonos) com atributos |
| Em Python | matriz do NumPy, lida com rasterio | tabela com geometria, lida com GeoPandas |
| Exemplos | MapBiomas, PRODES, altitude, NDVI | municípios, estradas, focos de queimada, unidades de conservação |
| Na disciplina | o substrato dos modelos em grade (encontros 6, 9 a 12) | os dados que viram variáveis da grade (encontro 10) |

**2. Tabela e geometria (3 min).** Uma tabela do pandas é uma planilha com colunas nomeadas; um GeoDataFrame é a mesma tabela com a coluna `geometry`. Quase tudo que se faz com tabelas (filtrar, agrupar) vale para mapas vetoriais.

**3. Sistema de coordenadas (3 min).** Toda geometria e todo raster têm um sistema de coordenadas (CRS). Os estados estão em SIRGAS 2000 geográfico (EPSG:4674), em graus; o MapBiomas, em graus também. Áreas em graus não fazem sentido: para medir, usa-se uma projeção de área igual (encontro 10).

**4. Ler só o pedaço (4 min).** O mosaico do MapBiomas do Brasil tem dezenas de bilhões de pixels. Como é um GeoTIFF organizado em blocos, o rasterio lê só os blocos da janela pedida, direto do servidor. É o mesmo princípio que o DisSCube usa (encontro 10).

## Prática (70 min)

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 1. NumPy | Grade 6 × 8 com floresta (3), pastagem (15) e água (33): 27 células de floresta (56%), 11 de pastagem, 10 de água. Pastagem com células de 30 m: 0,0099 km² | Uma comparação na grade inteira gera uma máscara; somar a máscara conta |
| 2. pandas | 1.260 focos em 5 e 6 de setembro de 2026: 1.092 no Cerrado, 167 na Amazônia, 1 na Caatinga; 118 com FRP acima de 100 MW. Dez municípios com mais focos, Barra do Corda à frente (110) | Filtrar é usar uma máscara nas linhas; agrupar resume por categoria. O endereço do arquivo tem um commit fixo |
| 3. GeoPandas | Estados do IBGE por região; Maranhão com 329.651 km²; focos convertidos em pontos sobre o estado, coloridos por bioma | Uma tabela com latitude e longitude vira mapa com `points_from_xy` e um CRS |
| 4. rasterio | Janela da Ilha do Maranhão no mosaico de 2024 (cerca de 1.300 × 1.850 pixels); tabela de pixels e área por classe; mapa com as oito classes principais; recorte salvo como GeoTIFF | Não se baixa o Brasil para estudar a Ilha. A área em km² é aproximada |

**Para casa**

1. Trocar `ANO` para 1985 e comparar a Área Urbanizada de 1985 e 2024.
2. Coluna `data` com o dia e contagem de focos por dia e por bioma.
3. Contar quantos focos caem dentro de outro estado com `gpd.sjoin` e explicar o resultado.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Floresta depois de mudar a célula (0, 0) | 26 células (eram 27) |
| 2. Maior FRP médio entre os dez | Governador Luiz Rocha (148,5 MW, com 52 focos). Mais focos não quer dizer fogo mais intenso: Barra do Corda tem o dobro de focos e FRP médio de 51,3 MW; Alto Parnaíba, 64 focos e 11,4 MW |
| 3. Onde se concentram os focos | No centro-sul do estado, no Cerrado (87% dos focos); 27% estão ao norte de 4° S, onde ficam os 167 focos da Amazônia maranhense. O mapa mostra o que a tabela de biomas resumia |
| 4. Classe com mais área; a área é exata? | A classe depende da tabela da aula (conferir antes). A área é aproximada: o pixel do MapBiomas é definido em graus (cerca de 0,00027°), o que dá 30 m no sentido norte-sul e 30 m × cosseno da latitude no leste-oeste. Na Ilha (2,6° S) a diferença é de 0,1%; em latitudes maiores cresce. Para área exata, reprojetar para uma projeção de área igual |

**Para casa, com os números do teste**

2. Em 5 de setembro: 728 focos no Cerrado e 76 na Amazônia; em 6 de setembro: 364 no Cerrado, 91 na Amazônia e 1 na Caatinga.
3. Nenhum foco cai em outro estado: o arquivo traz só focos do Maranhão (`bdqueimadas_ma.csv`), e os 1.260 caem dentro do polígono do MA. É uma lição sobre conhecer a origem do dado antes de analisá-lo.

## Achados ao testar

Testado em 31 out 2026 com Python 3.13, geopandas 1.2.0, rasterio 1.5.2 e pandas. As Partes 1 a 3 rodam em cerca de 4 s, lendo os dados do GitHub por commit fixo.

1. **A Parte 4 não pôde ser executada ao preparar o material:** o ambiente de teste bloqueia `storage.googleapis.com` (resposta 403). A lógica foi conferida com um raster sintético em EPSG:4326 cobrindo a mesma área: a janela sai com 1.299 × 1.855 pixels, a tabela e o mapa funcionam e o recorte é salvo. No site, essas células aparecem sem saída (marca `sem-saida-no-site`). A URL é a mesma que o DisSCube 0.6.0 usa para a Coleção 11.
2. **O FRP tem valores ausentes:** 1.119 dos 1.260 focos têm FRP. O `describe` mostra a contagem; vale comentar com a turma que média de coluna com ausentes ignora as linhas vazias.
3. **Os dados de focos e estados não têm fonte registrada nos repositórios de origem** (ponto já anotado nas revisões dos dois livros). O notebook cita BDQueimadas/INPE e IBGE; convém registrar data de extração e licença nos repositórios.
