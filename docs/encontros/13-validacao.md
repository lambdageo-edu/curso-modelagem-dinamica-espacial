# Encontro 13 — Validação e oficina de projeto

O encontro tem duas partes. Na primeira, uma demonstração de 25 minutos compara o lab15 com o desmatamento observado em 2004. Ela mostra figura de mérito, quantidade e localização, modelos nulos e erro por resolução. Na segunda, cada aluno aplica as mesmas funções ao próprio modelo, com o professor atendendo um por um. O aluno sai com o material de validação que vai apresentar no seminário.

**Notebook:** [encontro13_validacao.ipynb](../notebooks/encontro13_validacao.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 25 de demonstração, 65 de oficina, 5 de fechamento |
| Material | Notebook `encontro13_validacao.ipynb` (15 células, roda em cerca de 6 s) |
| Modelo e dados | lab15 (tolerância 10) sobre o `cs_moju` do `luccme-goldens` v1.1.0, que traz o desmatado observado em 1999 (`d`), 2004 (`d04`) e 2007 (`d07`) |
| Funções | `pontius_millones` e `naive_allocation` do `disslucc.validation`; figura de mérito e erro por bloco escritos no notebook |
| Leitura de apoio | Pontius e Millones (2011); Pontius et al. (2008); Pontius, Huffaker e Denman (2004), sobre validação em várias resoluções |

**Objetivos**

1. Distinguir verificação (o programa faz as contas do modelo) de validação (o modelo se parece com o mundo).
2. Ler acertos, omissões, falsos alarmes e a figura de mérito.
3. Separar o erro em quantidade e localização.
4. Comparar o modelo com modelos nulos: persistência e sorteio.
5. Avaliar o erro em mais de uma resolução e achar a resolução a partir da qual o modelo vale a pena.
6. Validar o próprio modelo e preparar o material do seminário.

## Antes da aula

- [ ] Nada a instalar além do ambiente do encontro 12.
- [ ] Rodar o notebook do professor. Números que não mudam:
    - figura de mérito do lab15 de 15,1% (63 acertos, 179 omissões, 174 falsos alarmes), contra 2,1% do sorteio;
    - a ordenação pelo potencial dá o mesmo resultado do lab15;
    - erro total de 6,04% no lab15 (0,02% de quantidade, 6,02% de localização), contra 4,16% na persistência (4,02% de quantidade);
    - por resolução, o lab15 empata com a persistência em blocos de 16 células (cerca de 8 km) e fica abaixo dela em blocos de 32 (2,99% contra 4,02%).
- [ ] Rever as listas do encontro 12 e separar os alunos em dois grupos: quem já tem uma rodada para validar e quem ainda precisa rodar o modelo.
- [ ] Ter à mão os notebooks dos encontros 9 a 12, que servem de base para os modelos dos alunos.

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | Verificação × validação: "o DisSLUCC bate com o LuccME; o LuccME bate com o mundo?" | — |
| 5–30 | Demonstração | O professor roda e comenta as Partes 1 a 4, com as Perguntas 1 a 4 para a turma | Partes 1 a 4 |
| 30–95 | Oficina | Atendimento individual com a lista da Parte 5 | Parte 5 e Oficina |
| 95–100 | Fechamento | O formato do seminário; o que entregar | — |

A demonstração deve ser feita pelo professor, na tela, para sobrar tempo de oficina. Os alunos rodam o notebook depois, como referência.

## Demonstração (25 min)

**1. Simulado × observado (5 min).** Mapa com acertos, omissões e falsos alarmes. A figura de mérito (Pontius et al., 2008) conta só as células que mudaram, e por isso não é inflada pelas milhares de células de floresta que nenhum dos dois mapas mudou. Uma acurácia de "94% das células corretas" engana justamente por contar essas células.

**2. Quantidade e localização (6 min).** A decomposição de Pontius e Millones (2011). O modelo acerta a quantidade, porque a demanda vem dos dados, e erra a localização. A persistência é o contrário. Por isso o modelo erra mais que "nada muda" na resolução da célula. É o resultado mais contraintuitivo do encontro e merece tempo.

**3. Modelos nulos (6 min).** Um modelo só tem valor em relação a uma alternativa simples. O sorteio, com a mesma quantidade e lugar ao acaso, tem figura de mérito de 2,1%; o lab15, de 15,1%: o potencial ajuda. A ordenação pelo potencial, sem o laço do CLUE-S, dá exatamente o mesmo resultado; neste lab, quem decide é o potencial.

**4. Resolução (8 min).** Errar a célula vizinha conta como erro inteiro. Agrupando em blocos, o erro do modelo cai e cruza o da persistência por volta de 8 km, a "resolução nula" de Pontius, Huffaker e Denman (2004). Em blocos de 8 km o sorteio chega a errar um pouco menos que o modelo. Fechar com a Pergunta 4: para que decisões este modelo serve?

Lembrar o aviso do notebook: não sabemos se os coeficientes do lab15 foram ajustados com o mapa de 2004. Validação honesta usa um mapa que não entrou no ajuste.

## Oficina (65 min): o que conferir em cada projeto

Começar pelos alunos que já têm uma rodada; os demais trabalham nos notebooks 9 a 12 enquanto esperam. Em cada atendimento, nesta ordem:

1. **O mapa observado é comparável ao simulado?** Mesma grade, mesmas classes e mesmo ano. Se veio de outra fonte, passar pelo DisSCube na mesma grade (encontro 10).
2. **A quantidade simulada bate com a demanda?** Se não bate, a tolerância está grande (encontros 9 e 11).
3. **A validação usa um ano que não entrou no ajuste?** Se a regressão foi ajustada com o mesmo mapa usado na validação, dizer isso no seminário.
4. **O modelo bate os nulos?** Figura de mérito contra o sorteio, erro total contra a persistência, em mais de uma resolução.
5. **O que o modelo não representa?** Uma frase, para o seminário.

**Problemas mais prováveis, e onde já apareceram**

| Sintoma | Causa provável | Encontro |
| --- | --- | --- |
| O modelo não muda nada, ou muda muito mais que a demanda | tolerância (`max_difference`) maior que a mudança do período | 9, 11 |
| O resultado não confere, ou a alocação não converge | falta a banda `mask` com as células válidas | 9 |
| O mapa observado não se sobrepõe ao simulado | grade ou projeção diferente; coordenadas que não batem com o `.prj` | 9, 10 |
| Coeficientes enormes e de sinais opostos | duas variáveis quase iguais na regressão (colinearidade) | 11 |
| A figura de mérito sai `nan` ou muito alta | modelo contínuo comparado como se fosse discreto; escolher um limiar de mudança | 13 |
| Gráficos somem do notebook | `disscube plot` trocou o modo do matplotlib; rodar `%matplotlib inline` | 10 |

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Onde estão os erros | O erro é principalmente de região. Os falsos alarmes se concentram no norte; as omissões se espalham pelo sul, ao longo das faixas já desmatadas em 1999 (as vicinais), onde o desmatamento de fato avançou. Há acertos no noroeste. Como o erro é de região, e não de "célula ao lado", agrupar em blocos pequenos quase não ajuda |
| 2. Pior que "nada muda" | A persistência erra só a quantidade: deixa de desmatar as 238 células e nunca põe nada no lugar errado (4,02% de quantidade). O lab15 acerta a quantidade, mas cada célula no lugar errado conta duas vezes: um falso alarme onde desmatou e uma omissão onde deveria ter desmatado. Com 174 falsos alarmes, o erro de localização chega a 6,02% |
| 3. Melhor que sortear? | Cerca de 7 vezes melhor (15,1% contra 2,1%): o potencial põe a mudança mais perto de onde ela aconteceu do que o acaso. A ordenação pelo potencial dá o mesmo resultado: neste lab, o laço de ajuste do CLUE-S não muda nada, e quem decide o lugar é o potencial (o `disslucc-benchmark` já registra que o lab15 do pacote quase não discrimina) |
| 4. Para que decisões serve | Na célula (500 m), o modelo erra mais que a persistência: não serve para escolher propriedades a fiscalizar. Ele só empata com a persistência em blocos de cerca de 8 km, onde o sorteio também já chega perto, e fica melhor que os dois em blocos de 16 km. Serve, com cautela, para indicar regiões de mais de 10 km. Dizer isso é parte do resultado, não uma falha do trabalho |

## Achados ao testar

Testado em 1 nov 2026 com Python 3.13, dissmodel 0.6.6, disslucc 0.5.0 e luccme-goldens 1.1.0. O notebook roda sem erro em cerca de 6 s. As funções da Parte 5 foram testadas com matrizes 2D montadas a partir do `cs_moju`, como as de uma grade do DisSCube.

1. **Na resolução da célula, o lab15 erra mais que a persistência**, e só a alcança em blocos de cerca de 8 km. É o resultado típico dos estudos de Pontius e um bom fecho para a disciplina, mas pode desanimar quem esperava "o modelo acerta". O roteiro trata isso como resultado, não como fracasso.
2. **A ordenação pelo potencial (`naive_allocation`) dá exatamente o mesmo mapa do CLUE-S** (63 acertos, 179 omissões, 174 falsos alarmes). Confirma o registro do `disslucc-benchmark` de que o lab15 quase não discrimina.
3. **O mapa observado tem quatro células desmatadas em 1999 que voltam a floresta em 2004**, e duas de 2004 que voltam em 2007. A matriz de transição do lab15 não permite isso, então essas células são sempre erro do modelo. São poucas, mas um aluno atento vai perguntar: são provavelmente erros de classificação do mapa observado.
4. **A figura de mérito não está no `disslucc.validation`**, que tem `pontius_millones` e `confusion_metrics`. O notebook a define em poucas linhas. Vale acrescentá-la ao pacote, junto com o erro por bloco.
5. **A validação fora da amostra não foi feita.** O `cs_moju` tem o desmatado de 2007 (`d07`), mas a demanda do lab15 vai só até 2004. Estender a demanda até 2007 permitiria uma validação com um mapa que certamente não entrou no ajuste; fica como sugestão para uma versão futura do notebook.
