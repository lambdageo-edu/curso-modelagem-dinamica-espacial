# Encontro 9 — Um modelo LUCC com o DisSLUCC

O aluno sai do encontro tendo rodado um modelo de mudança de uso de verdade, o lab01 do LuccME (Acre, 2008 a 2014), com as três peças do encontro 8 escritas como objetos do DisSLUCC: demanda, potencial e alocação. Verifica o porte contra as saídas do LuccME, descobre que o modelo verificado não respeita a demanda por causa da tolerância da alocação, e compara dois cenários de demanda. Os dados vêm prontos; o encontro 10 mostra como montá-los.

**Notebook:** [encontro09_disslucc.ipynb](../notebooks/encontro09_disslucc.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 25 de exposição, 60 de prática, 10 de fechamento |
| Material | Notebook `encontro09_disslucc.ipynb` (35 células, roda em cerca de 15 s) |
| Modelo | `DemandPreComputedValues`, `PotentialLinearRegression` e `AllocationClueLike` do `disslucc` 0.5.0 |
| Dados e referência | `csAC` (6.574 células de 5 × 5 km) e as saídas do LuccME para o lab01 e a variante `lab01_md1643`, do `luccme-goldens` v1.1.0 (DOI 10.5281/zenodo.23161342) |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, caps. 26 (LUCC) e 30 (verificação); Verburg et al. (1999), a alocação contínua; Aguiar et al. (2012), o LuccME |

**Objetivos**

1. Reconhecer demanda, potencial e alocação num modelo real e o que cada uma recebe como entrada.
2. Ler os coeficientes de uma regressão de potencial e dizer se os sinais fazem sentido.
3. Verificar um porte contra a implementação de referência, e saber explicar uma diferença intencional.
4. Distinguir verificação de adequação: um modelo pode reproduzir o original e mesmo assim não cumprir a demanda.
5. Construir um cenário mudando só a demanda, e comparar cenários em área e em mapa.

## Antes da aula

- [ ] Instalar o DisSLUCC: `pip install "disslucc==0.5.0"` (está no PyPI). No Colab, a primeira célula do notebook instala tudo sozinha; o selo **Abrir no Colab** fica no topo do notebook.
- [ ] Conferir acesso a `raw.githubusercontent.com`. Sem rede, copiar para a pasta `dados_lab01/` os sete arquivos da lista `ARQUIVOS` (do `luccme-goldens` v1.1.0); a função `baixar` aceita arquivos já presentes se o hash confere.
- [ ] Rodar o notebook do professor. Números que não mudam: desmatado de 19.983 km² em 2008; diferenças contra o LuccME abaixo de 5 × 10⁻⁷; iterações da variante `[0, 0, 8, 26, 18, 17, 17]`; com tolerância de 5.000 km², 24.530 km² desmatados em 2014 contra 21.607 da demanda; com 200 km², 21.611 (tendência) e cerca de 20.800 (governança); 1.135 células diferem mais de 1 ponto percentual entre os cenários.
- [ ] Trazer as fichas de leitura do encontro 8 devolvidas, com os drivers marcados: são usadas no fechamento.

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | Retomar o encontro 8: "quanto, onde provável, onde de fato". Hoje as três peças viram código | — |
| 5–30 | Exposição | O lab01; demanda como tabela; potencial por regressão; alocação CLUE e tolerância; verificação pelos goldens | — |
| 30–45 | Prática | Baixar e conferir hashes; mapas dos dados; tabela da demanda; sinais dos coeficientes | Partes 0 a 3 |
| 45–60 | Prática | A função `simular`; rodar o lab01; mapas do potencial e do ganho de desmatado | Parte 4 |
| 60–70 | Prática | Verificação contra o LuccME; a variante com o laço de ajuste; a correção de célula | Parte 5 |
| 70–80 | Prática | A demanda foi atendida? Tolerância de 5.000 contra 200 km² | Parte 6 |
| 80–90 | Prática | Cenários tendência e governança: curvas e mapa do desmatamento evitado | Parte 7 |
| 90–100 | Fechamento | Pergunta 3 em voz alta; drivers do lab01 contra os da ficha de cada aluno; ponte para o encontro 10 | Para casa |

Se o tempo apertar, a Parte 5 pode ser só mostrada (a verificação foi feita da mesma forma nos encontros 5 a 7). A Parte 6 não deve ser cortada: é a lição principal do encontro.

## Exposição (25 min, cerca de 8 slides)

**1. O lab01 (3 min).** Primeiro exemplo do pacote LuccME, do INPE: Acre, células de 25 km², três classes (floresta, desmatado, outros) como frações da célula, de 2008 a 2014. Vamos rodar exatamente o modelo publicado, com os coeficientes que os autores ajustaram.

**2. Demanda como tabela (3 min).** `DemandPreComputedValues` recebe a área de cada classe em cada ano. Ela não olha o mapa: só diz o total. Cenário, no DisSLUCC, é antes de tudo outra tabela de demanda; isso volta no fim da aula e no encontro 12.

**3. Potencial por regressão (6 min).** Uma regressão linear por classe sobre os drivers (`PotentialLinearRegression`, Verburg et al., 1999). Dois detalhes que o notebook mostra: (a) o potencial que a alocação usa é a regressão menos a fração que a célula já tem, ou seja, espaço para crescer; (b) os coeficientes de distância são minúsculos porque a distância está em metros. De onde vêm os coeficientes (ajuste por regressão) é o encontro 11.

**4. Alocação CLUE e tolerância (7 min).** `AllocationClueLike` distribui a mudança pelas células, proporcional ao potencial, e confere a soma contra a demanda. Se a diferença passa da tolerância (`max_difference`, em km²), ajusta e tenta de novo; o número de tentativas é o que o LuccME chama de iterações. Antecipar a pergunta da aula: o que acontece com uma tolerância grande demais?

**5. Verificação pelos goldens (6 min).** Como nos encontros 5 a 7: o `luccme-goldens` guarda, célula a célula, o que o LuccME calculou. Diferenças de 10⁻⁷ são ruído numérico. Uma diferença de projeto: no LuccME, a correção de célula da alocação nunca roda (um erro de digitação no nome de um campo no código Lua); o DisSLUCC a roda por padrão e a desliga com `cell_correction=False` para reproduzir o original. Verificar é também saber explicar onde e por que os dois diferem.

## Prática (60 min)

O aluno não escreve o modelo: lê a função `simular` (cerca de 30 linhas) e muda os dois parâmetros dela, a demanda e a tolerância. A parte de código nova para a turma é pequena; o esforço está em ler tabelas e mapas.

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 0. Preparação | Sete arquivos baixados e conferidos pelo hash | A mesma ideia do encontro 4: o arquivo é o publicado ou o notebook para |
| 1. Dados | 6.574 células; seis mapas (desmatado, rodovias, assentamentos, UC, TI); 19.983 km² desmatados em 2008 | O desmatamento já segue as estradas, sobretudo no leste |
| 2. Demanda | Cerca de 256 km² por ano até 2011 e 286 a partir de 2012; `outros` constante | A demanda é só uma tabela |
| 3. Potencial | Coeficientes das duas regressões, lado a lado | Pergunta 1 |
| 4. Modelo | `simular` roda o lab01 em centésimos de segundo; mapas do potencial, do desmatado em 2014 e do ganho | Pergunta 2; potencial negativo onde já não há espaço |
| 5. Verificação | Diferenças abaixo de 5 × 10⁻⁷ no lab01; variante com 1.643 km²: iterações `[0, 0, 8, 26, 18, 17, 17]` nos dois programas; correção de célula: até 0,039 numa célula | Igualdade numérica, inclusive no laço de ajuste; a diferença intencional está documentada |
| 6. Demanda atendida? | Com 5.000 km² de tolerância, 24.530 km² desmatados em 2014 (2.923 a mais que a demanda); com 1.643, 22.609; com 200, 21.611 em menos de 1 s | Pergunta 3 |
| 7. Cenários | Governança corta à metade o desmatamento anual: cerca de 20.800 km² em 2014 contra 21.611; 1.135 células com diferença acima de 1 ponto percentual | Pergunta 4; só a demanda mudou |

**Para casa**

1. Dobrar o coeficiente de `rodovias` no potencial do desmatado e rodar a tendência.
2. Cenário intermediário (`REDUCAO = 0.25`) no gráfico dos cenários.
3. Drivers do lab01 contra os drivers da ficha do encontro 8; trazer a lista para o encontro 10.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Sinais dos coeficientes | Rodovias negativo para o desmatado: quanto mais longe da estrada, menor o potencial (acesso e custo de transporte). Assentamentos negativo para floresta e positivo para desmatado: assentamentos concentram abertura de lotes. UC e TI positivas para floresta e negativas para desmatado (onde aparecem). Pode surpreender: `fertilidad` negativo para floresta e positivo para desmatado é coerente (solo bom atrai uso agrícola), e `dist_riobr` (distância em linha reta à capital, Rio Branco) positivo para floresta e negativo para desmatado diz que o desmatamento cai com a distância ao principal mercado, efeito que se confunde com o das estradas, que também saem da capital. Bom momento para lembrar que coeficiente de regressão não é causa |
| 2. Onde o desmatamento avança | No leste e sudeste (região de Rio Branco), ao longo das estradas e nos assentamentos, e em manchas ao longo dos rios no oeste. O ganho é contínuo e difuso: a alocação acrescenta pequenas frações a muitas células, em vez de converter células inteiras, porque as classes são frações (alocação contínua; a discreta é o encontro 11) |
| 3. Verificação × demanda | Não é contradição. A verificação garante que o DisSLUCC faz as mesmas contas que o LuccME, com os mesmos parâmetros, inclusive a tolerância. Ela não diz se os parâmetros são adequados nem se o modelo representa o Acre: isso é validação (encontro 13). Aqui a tolerância de 5.000 km² é maior que todo o desmatamento do período (1.625 km²), e a alocação aceita a primeira tentativa, que desmata demais |
| 4. Onde está o desmatamento evitado | Concentrado onde o potencial é alto: leste e sudeste, perto das estradas e assentamentos. A governança não muda o potencial; ela só reduz o total, e a alocação corta primeiro nas células que receberiam mais. O efeito máximo é pequeno por célula (cerca de 4 pontos percentuais em 2014), espalhado por mais de mil células |

**Para casa, com os números do teste**

1. Com o coeficiente de `rodovias` dobrado (`-0.0000019844`), o desmatado em 2014 continua em 21.610 km²: a demanda decide quanto. O mapa muda: 1.006 células diferem mais de 1 ponto percentual da tendência, e a parcela do desmatamento novo a menos de 20 km de uma rodovia sobe de 31% para 45% (a menos de 50 km, de 67% para 86%).
2. Com `REDUCAO = 0.25`, a demanda de 2014 é de 21.201 km²; a curva simulada fica a menos de 200 km² dela, entre as outras duas.

## Achados ao testar

Testado em 31 out 2026 com Python 3.13, dissmodel 0.6.6, disslucc 0.5.0 e luccme-goldens 1.1.0. O notebook roda sem erro em cerca de 15 s; com tolerância de 200 km², cada cenário leva menos de 1 s (300 a 430 iterações por ano).

1. **Sem a banda `mask` o modelo não confere com o LuccME e pode não convergir.** A grade retangular (89 × 165) tem células fora do Acre; o DisSLUCC só as ignora se houver uma banda `mask` no `RasterBackend`. Nada no erro aponta para isso. Vale documentar no `disslucc` ou criar a máscara automaticamente na leitura de um espaço celular vetorial.
2. **A tolerância do lab01 (5.000 km²) faz o modelo ignorar a demanda**, no LuccME e no DisSLUCC: 2.923 km² a mais em 2014. Com 5.000 km² os dois cenários dariam o mesmo mapa. O notebook usa 200 km² nos cenários. Com 50 km² ainda converge (cerca de 4 s); com 10 km², a alocação falha ("Allocation did not converge").
3. **`cell_correction` tem padrão diferente do LuccME por decisão de projeto**, documentada no código do `disslucc`. Para verificar é preciso passar `cell_correction=False`; quem esquecer vê diferenças de até 0,039 e pode achar que o porte está errado.
4. **`dist_riobr` é a distância euclidiana a Rio Branco, não a rios.** O lab01 não documenta a coluna, mas os dados confirmam: os valores são exatamente a distância de cada centro de célula a um único ponto (erro médio abaixo de 1 m), e esse ponto cai na latitude de Rio Branco (9,97° S), na parte leste do estado. `fertilidad` continua sem definição nos dados; o notebook a interpreta pelo nome (solo fértil).
5. **As coordenadas do `csAC.shp` não batem com o `.prj`.** Elas estão sem o falso leste e falso norte declarados (5.000 km e 10.000 km) e, mesmo somando esses valores, o Acre cai cerca de 3° a leste da posição real. Não afeta o modelo, que só usa linha e coluna, mas impede sobrepor o espaço celular a dados externos sem corrigir a projeção: um bom exemplo para o encontro 10.
6. **O potencial guardado (`d_pot`) é a regressão menos o uso atual.** Faz sentido para a alocação, mas o mapa assusta (valores negativos) se não for explicado; o notebook explica logo abaixo da figura.
