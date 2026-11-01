# Encontro 11 — Potencial, alocação e restrições

O aluno sai do encontro sabendo de onde vêm os coeficientes de um potencial e o que eles dizem. Ele também distingue alocação contínua de discreta e vê o que uma restrição faz com o desmatamento. O lab01 do LuccME tem coeficientes que o aluno reproduz por mínimos quadrados. O lab15 (Mojuí dos Campos) é o exemplo discreto, verificado contra o LuccME e usado para a comparação e para a restrição. A regressão do próprio projeto fica como tarefa.

**Notebook:** [encontro11_potencial_alocacao.ipynb](../notebooks/encontro11_potencial_alocacao.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 25 de exposição, 60 de prática, 10 de fechamento |
| Material | Notebook `encontro11_potencial_alocacao.ipynb` (28 células, roda em cerca de 15 s, incluindo o download) |
| Componentes | `PotentialLinearRegression` + `AllocationClueLike` (contínua); `PotentialDLogisticRegression` + `AllocationDClueSLike` (discreta), do `disslucc` 0.5.0; regressão com `statsmodels` |
| Dados e referência | `csAC` (lab01) e `cs_moju` (lab15, 5.914 células de cerca de 500 m) e a saída do LuccME para a variante `lab15_md10`, do `luccme-goldens` v1.1.0 |
| Leitura de apoio | Verburg et al. (2002), CLUE-S; Overmars, Verburg e Veldkamp (2007), sobre a especificação do potencial; livro *Geospatial Modeling with Python*, caps. 13 (regressão) e 26 |

**Objetivos**

1. Ajustar uma regressão linear de potencial e ler coeficientes, valor-p e R².
2. Comparar o peso das variáveis pelo efeito de um desvio padrão, e não pelo tamanho do coeficiente.
3. Distinguir alocação contínua (frações) de discreta (uma classe por célula) e escolher a que combina com os dados.
4. Explicar matriz de transição e elasticidade.
5. Representar uma restrição como região e reconhecer o vazamento.

## Antes da aula

- [ ] Instalar o `statsmodels` (`pip install statsmodels`); o resto vem dos encontros 9 e 10. No Colab, a primeira célula instala tudo sozinha.
- [ ] Conferir acesso a `raw.githubusercontent.com` (nove arquivos do `luccme-goldens` v1.1.0).
- [ ] Rodar o notebook do professor. Números que não mudam:
    - os coeficientes ajustados batem com os do lab01 até a quarta casa, com R² de 0,387 para o desmatado;
    - com só as rodovias, o R² cai para 0,152;
    - lab15 com tolerância 300: nenhuma mudança (205 células em todos os anos);
    - lab15 com tolerância 10: iterações `[0, 67, 56, 56, 61, 61]` e nenhuma célula diferente do LuccME;
    - 237 células novas na discreta, contra 3.948 células com ganho na contínua (no máximo 0,20);
    - faixa de 0,0045°: 1.367 células protegidas, 174 novas evitadas na faixa e 176 deslocadas.
- [ ] Trazer as regressões que os alunos já tenham feito com o cubo do encontro 10, se houver.

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | Nuvem de pontos do encontro 10: "como passar disso para um número no modelo?" | — |
| 5–30 | Exposição | Regressão linear e logística; o que o R² e o valor-p dizem e não dizem; contínua × discreta; matriz de transição, elasticidade; restrições e vazamento | — |
| 30–45 | Prática | Reajustar o lab01; efeito de um desvio padrão; potencial de uma variável só | Parte 1 |
| 45–60 | Prática | lab15: tolerância 300 e 10; verificação; mapa das células novas | Parte 2 |
| 60–75 | Prática | Contínua × discreta em Mojuí dos Campos | Parte 3 |
| 75–90 | Prática | Faixa protegida ao longo dos rios; evitadas e deslocadas | Parte 4 |
| 90–100 | Fechamento | Pergunta 4 em voz alta; apresentar o "para casa" | Para casa |

Se o tempo apertar, a Parte 3 pode ser só mostrada. A Parte 4 não deve ser cortada: o vazamento prepara os cenários do encontro 12 e a discussão dos projetos.

## Exposição (25 min, cerca de 8 slides)

**1. Regressão linear (6 min).** A reta (ou o plano) que passa mais perto dos pontos. O que se lê de um ajuste:

- coeficiente: quanto o potencial muda por unidade da variável;
- valor-p: se o coeficiente se distingue de zero;
- R²: quanto da variação entre células o modelo explica.

Nenhum dos três diz que a variável causa a mudança. Os coeficientes não se comparam entre si quando as unidades diferem (metros e frações); para isso se usa o efeito de um desvio padrão.

**2. Regressão logística (4 min).** Para dados que só valem 0 ou 1 (floresta ou desmatada), a reta sai de 0 a 1 e se ajusta mal. A logística dá uma probabilidade entre 0 e 1. Os coeficientes se leem pelo sinal: positivo aumenta a probabilidade, negativo diminui.

**3. Contínua × discreta (6 min).**

| | Contínua (`ClueLike`, CLUE) | Discreta (`DClueSLike`, CLUE-S) |
| --- | --- | --- |
| Estado da célula | frações de cada classe | uma classe |
| Potencial típico | regressão linear | regressão logística |
| Tamanho de célula típico | km (a célula mistura usos) | dezenas a centenas de metros |
| Dados de entrada | cobertura por célula (`percentage` do encontro 10) | mapa de classes (`majority`) |
| Mudança | pequenas frações em muitas células | células inteiras |

Mencionar a terceira alocação, a contínua com saturação (lab03): quando a célula se aproxima do limite, a mudança passa para as vizinhas.

**4. Matriz de transição e elasticidade (4 min).** A matriz diz o que pode virar o quê (desmatado não volta a floresta, no lab15). A elasticidade é a resistência de cada classe a mudar.

**5. Restrições e vazamento (5 min).** Uma restrição é uma região com outra matriz de transição. Se a demanda não muda, a mudança proibida vai para fora da área protegida. É o vazamento, um tema central na avaliação de áreas protegidas: proteger um lugar só reduz o total se a demanda também cair.

## Prática (60 min)

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 1. Potencial | O ajuste reproduz os coeficientes do lab01; R² 0,387; efeito de um desvio padrão: assentamentos +0,067, distância a Rio Branco −0,061, rodovias −0,047, UC de uso sustentável −0,038, fertilidade +0,032. Com só as rodovias, R² 0,152 | Os autores do lab01 fizeram exatamente esta regressão sobre o mapa de 2008. Perguntas 1 e 2 |
| 2. Discreta | Com tolerância 300, nada muda (a demanda cresce 238 células). Com 10, iterações iguais às do TerraME e nenhuma célula diferente; 237 células novas | O mesmo problema de tolerância do encontro 9; matriz de transição |
| 3. Contínua × discreta | 3.948 células com ganho de no máximo 0,20, contra 237 células inteiras. A regressão linear em Mojuí tem R² 0,11 e é dominada por duas distâncias quase iguais | Natureza do resultado; o lugar muda por causa do potencial. Pergunta 3 |
| 4. Restrição | 1.367 células protegidas; das 237 novas, 174 caíam na faixa; com a restrição, nenhuma na faixa e 176 deslocadas para fora | Vazamento. Pergunta 4 |

**Para casa**

1. Ajustar uma regressão para a classe que muda no projeto, com duas ou três variáveis do cubo do encontro 10 (ou com o cubo Amazônia, para quem não tem grade própria).
2. Calcular o efeito de um desvio padrão.
3. Trazer a tabela para o encontro 12.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Qual variável pesa mais | Assentamentos (+0,067 para um desvio padrão), seguida da distância a Rio Branco (−0,061). A que pesa menos é a fertilidade (+0,032). Confere com o encontro 9: o desmatamento se concentra no leste, perto da capital e nos assentamentos. O coeficiente de `rodovias` parece minúsculo (−0,0000009922) só porque está por metro |
| 2. O que o potencial de uma variável só não representa | Com só as rodovias, o potencial é uma faixa suave ao longo das estradas. Ele superestima o desmatamento ao longo das rodovias no centro e no oeste, onde há pouco, e não reproduz a concentração no sudeste, perto de Rio Branco e dos assentamentos. O R² cai de 0,39 para 0,15 |
| 3. Contínua ou discreta no projeto | Depende dos dados e da célula. Com o MapBiomas agregado por `percentage` em células de 1 km ou mais, a contínua é a natural. Com `majority` em células pequenas (até algumas centenas de metros), em que cada célula é de fato uma classe, a discreta. Uma célula grande tratada como uma classe só perde a mistura de usos |
| 4. Como a proteção reduziria o desmatamento | Mudando também a demanda: um cenário em que a política reduz a quantidade (como a governança do encontro 9) e protege a faixa. A restrição decide onde não pode; a demanda decide quanto. Sozinha, a restrição só desloca |

## Achados ao testar

Testado em 1 nov 2026 com Python 3.13, dissmodel 0.6.6, disslucc 0.5.0, statsmodels 0.15.0 e luccme-goldens 1.1.0. O notebook roda sem erro em cerca de 15 s, incluindo o download; cada simulação leva menos de 1 s.

1. **Os coeficientes do lab01 são uma regressão linear sobre o mapa de 2008.** O ajuste por mínimos quadrados com `statsmodels` reproduz os do script até a quarta casa decimal, para a floresta e para o desmatado. Com isso, o encontro pode mostrar que o potencial do lab tem origem conhecida e verificável.
2. **Os coeficientes do lab15 não saem dos dados do `cs_moju`.** Tentamos regressões logísticas para o desmatado de 1999, 2004 e 2007 e para a mudança de 1999 a 2004. Os coeficientes saem dezenas de vezes maiores, e o de `dist_area_` com o sinal trocado. Provavelmente vieram de outra área ou de outro período; o notebook os usa como publicados e não os apresenta como ajustados.
3. **`dist_area_` é idêntica a `dist_mojui`** (diferença zero em todas as células), e as duas têm correlação de 0,96 com `dist_curua`. Por isso a regressão linear da Parte 3 tem coeficientes enormes e de sinais opostos nessas variáveis. O notebook usa isso como exemplo de colinearidade.
4. **O lab15 original não muda nada.** Com tolerância de 300 células, maior que o crescimento da demanda no período (238), a alocação aceita "nenhuma mudança" em todos os anos, no LuccME e no DisSLUCC. É o mesmo problema do lab01 (encontro 9), mais forte; o `disslucc-benchmark` já registra que o lab15 do pacote quase não discrimina. O notebook usa a variante com tolerância 10.
5. **Uma restrição exige repetir o potencial para cada região.** No `AllocationDClueSLike`, a restrição é uma região com outra matriz de transição, e o `PotentialDLogisticRegression` precisa de um conjunto de coeficientes por região, mesmo que iguais. Funciona, mas um parâmetro de "camada de restrição" seria mais simples para quem não programa.
6. **Não dá para comparar as alocações com o mesmo potencial.** A contínua usa potencial linear e a discreta, logístico. A Parte 3 compara a forma do resultado, mas o lugar muda junto com o potencial, e o notebook diz isso.
7. **`statsmodels` é dependência nova** do ambiente da disciplina (está no Colab; no laboratório, acrescentar).
