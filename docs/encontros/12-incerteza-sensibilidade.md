# Encontro 12 — Incerteza e sensibilidade

O aluno sai do encontro sabendo perguntar quanto um mapa simulado depende das escolhas feitas, e mostrar a resposta. Com o lab15 do encontro 11 ele varre um coeficiente e mede a sensibilidade a cada um. Depois roda o modelo 50 vezes com coeficientes sorteados (uma semente por rodada) e faz um mapa de concordância. O encontro termina com a primeira conferência dos projetos.

**Notebook:** [encontro12_incerteza_sensibilidade.ipynb](../notebooks/encontro12_incerteza_sensibilidade.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 20 de exposição, 45 de prática, 30 de conferência dos projetos |
| Material | Notebook `encontro12_incerteza_sensibilidade.ipynb` (15 células, roda em cerca de 15 s; as 50 rodadas levam 4 s) |
| Modelo | lab15 do LuccME (`PotentialDLogisticRegression` + `AllocationDClueSLike`, tolerância 10), do `disslucc` 0.5.0 |
| Dados | `cs_moju` do `luccme-goldens` v1.1.0 |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, cap. 32; Saltelli et al. (2008), *Global Sensitivity Analysis: The Primer*, cap. 1; Pontius e Millones (2011) para o encontro 13 |

**Objetivos**

1. Separar as fontes de incerteza de um modelo LUCC: dados, parâmetros, estrutura e cenário.
2. Fazer uma varredura de um parâmetro e uma análise de sensibilidade "um de cada vez".
3. Fazer uma análise de Monte Carlo reprodutível, com uma semente por rodada.
4. Ler e comunicar um mapa de concordância, dizendo o que ele inclui e o que não inclui.
5. Conferir o estado do projeto com a lista do notebook.

## Antes da aula

- [ ] Nada a instalar além do ambiente do encontro 11.
- [ ] Rodar o notebook do professor. Números que não mudam:
    - 237 células novas no modelo base;
    - varredura de `dist_rios_`: com o fator 0, 139 células novas ficam perto de rio (174 no modelo base) e 202 são iguais às do modelo base; com o fator 2, 191 e 219;
    - sensibilidade a 20%: no máximo 8 células mudam de lugar (`dist_br` −20%);
    - 50 rodadas com 10% de sorteio: 216 células em 90% ou mais das rodadas, 36 incertas e 17 raras.
- [ ] Pedir na véspera que cada aluno traga a lista da Parte 6 preenchida, com a grade, a regressão e a pergunta.
- [ ] Preparar uma ordem para a conferência: 3 minutos por aluno, com o professor anotando o que falta para o encontro 13.

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | "Se o coeficiente das estradas fosse 20% maior, o mapa seria outro?" | — |
| 5–25 | Exposição | Fontes de incerteza; varredura e sensibilidade; Monte Carlo e semente; como comunicar | — |
| 25–40 | Prática | Modelo base; varredura de um coeficiente | Partes 1 a 3 |
| 40–50 | Prática | Sensibilidade "um de cada vez" | Parte 4 |
| 50–70 | Prática | 50 rodadas; mapa de concordância; Perguntas 3 e 4 | Parte 5 |
| 70–100 | Conferência | Cada aluno apresenta a lista da Parte 6 em 3 minutos | Parte 6 |

A conferência usa o tempo que for preciso; com turma grande, a Parte 4 fica para casa. O ponto do encontro é a Parte 5, e a conferência não pode ser cortada: é ela que organiza a oficina do encontro 13.

## Exposição (20 min, cerca de 7 slides)

**1. Fontes de incerteza (5 min).** A tabela da Parte 1:

- dados: erros de classificação, escala das camadas;
- parâmetros: coeficientes estimados, tolerância e elasticidade escolhidas;
- estrutura: tipo de potencial, tipo de alocação;
- cenário: a demanda futura.

O cenário não é incerteza a reduzir: é uma pergunta "e se", tratada por cenários (encontro 9). Hoje só os parâmetros.

**2. Varredura e sensibilidade (5 min).** Varredura: um parâmetro, vários valores, um gráfico. Sensibilidade "um de cada vez": cada parâmetro varia um pouco, os outros ficam fixos, e se compara o efeito. É simples e não capta interações entre parâmetros; métodos globais (Saltelli et al., 2008) existem para isso, mas estão fora do escopo da disciplina.

**3. Monte Carlo e semente (5 min).** Sortear os parâmetros, rodar muitas vezes e olhar a distribuição dos resultados. Cada rodada tem a sua semente, e o conjunto todo é reprodutível (encontro 4). O sorteio deveria vir do ajuste: o `statsmodels` dá a matriz de covariância dos coeficientes (`ajuste.cov_params()`), de onde se sorteia com `np.random.multivariate_normal`. No lab15 não há ajuste (encontro 11), por isso o notebook sorteia ±10% em torno de cada coeficiente, de forma independente.

**4. Comunicar (5 min).** Um único mapa simulado passa uma precisão que o modelo não tem. O mapa de concordância separa o que é robusto do que é incerto. Ele também tem limites: aqui todas as rodadas têm a mesma demanda, e a incerteza dos dados e da estrutura não entra. Mostrar o mapa de concordância junto com a lista do que ele não inclui.

## Prática (45 min)

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 2. Modelo base | 237 células novas em 0,1 s | A mesma função do encontro 11, com os coeficientes como argumento |
| 3. Varredura | Fator 0 a 2 em `dist_rios_`: perto de rio, de 139 a 191 células; iguais ao modelo base, de 202 a 237 | O coeficiente acrescenta 35 células perto dos rios; as outras 139 já iriam para lá. Pergunta 1 |
| 4. Sensibilidade | ±20% em cada coeficiente: de 0 a 8 células mudam de lugar | O lugar é robusto aos coeficientes. Pergunta 2 |
| 5. Monte Carlo | 50 rodadas em 4 s; 216 células em ≥ 90%, 36 incertas, 17 raras; a mesma semente repete o mapa | Perguntas 3 e 4 |
| 6. Conferência | Lista de sete itens por projeto | O que falta é o plano até o encontro 13 |

**Para casa**

1. Varrer a tolerância de 5 a 300.
2. Repetir o Monte Carlo com 30% de sorteio.
3. Completar a lista da Parte 6.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Sem efeito dos rios | Ainda ficam 139 células novas perto de um rio, contra 174 no modelo base. O coeficiente de `dist_rios_` acrescenta cerca de 35 células à faixa; a maior parte iria para lá de qualquer forma, porque as outras variáveis (estradas, distância às áreas ocupadas) já dão potencial alto perto dos rios, onde está a ocupação de 1999. Um coeficiente grande não quer dizer que a variável, sozinha, decide o lugar |
| 2. Sensível ou robusto | Robusto aos coeficientes: no pior caso 8 das 237 células mudam de lugar (3%). O que mexe muito no mapa é a tolerância (no "para casa", com 300 não há mudança nenhuma) e a demanda, que decide quanto. Também a estrutura: no encontro 11, o potencial linear pôs a mudança em outro lugar |
| 3. Mapa base ou de concordância | O de concordância, com uma frase sobre o que ele cobre. O mapa base mostra uma resposta única e esconde que parte dela é incerta. O de concordância mostra que 216 células são robustas e cerca de 50 dependem dos coeficientes. Mas ele também esconde coisas (Pergunta 4) e pode ser lido, errado, como probabilidade de desmatamento |
| 4. O que o mapa não inclui | A demanda (todas as rodadas desmatam a mesma quantidade), os dados (erros do mapa de 1999 e das distâncias), a estrutura (logística, CLUE-S), a tolerância e a elasticidade, os coeficientes da floresta e as constantes. Também as correlações entre os coeficientes: o sorteio é independente, e o certo seria usar a covariância do ajuste |

**Para casa, com os números do teste**

1. Tolerância de 5, 10, 20, 50, 100 e 300: 234, 237, 226, 227, 194 e 0 células novas. Em todos os casos, as células novas são um subconjunto das do modelo base. A tolerância muda a quantidade, não o lugar; os coeficientes mudam o lugar, pouco.
2. Com 30% de sorteio: 183 células em ≥ 90% das rodadas, 105 incertas e 73 raras. A faixa incerta triplica.

## Achados ao testar

Testado em 1 nov 2026 com Python 3.13, dissmodel 0.6.6, disslucc 0.5.0 e luccme-goldens 1.1.0. O notebook roda sem erro em cerca de 15 s; cada rodada do lab15 leva 0,1 s.

1. **As alocações do DisSLUCC não sorteiam nada.** CLUE e CLUE-S são determinísticos: rodar de novo dá o mesmo mapa. "Várias sementes", no cronograma, aqui quer dizer as sementes do sorteio dos coeficientes. Um modelo com sorteio na própria regra (o incêndio dos encontros 4 e 6) mostraria a outra forma de incerteza; fica como sugestão para uma versão futura.
2. **O lugar, no lab15, é pouco sensível aos coeficientes.** Com ±20%, no máximo 8 das 237 células mudam. A lição funciona, mas os números são pequenos. Com `VARIACAO = 0.5` ou `SORTEIO = 0.3` o efeito aparece mais; vale mostrar um dos dois em aula.
3. **O total de células novas varia entre 237 e 242 nas varreduras**, porque a tolerância de 10 células deixa uma folga. Isso não é sensibilidade do lugar, e a varredura mostra as duas coisas em colunas separadas.
4. **O sorteio não vem de um ajuste.** Os coeficientes do lab15 não têm erro-padrão publicado e não puderam ser reajustados (encontro 11), por isso o sorteio é de ±10% independente. Para o projeto, o roteiro indica o caminho certo (`cov_params()` e `multivariate_normal`); vale um exemplo pronto numa versão futura do notebook, usando o lab01.
