# Encontro 7 — Agentes e acoplamento

O aluno sai do encontro tendo lido e rodado um modelo de agentes (Schelling), comparado um modelo com sorteio ao TerraME pela distribuição de 50 rodadas, e visto dois modelos de paradigmas diferentes rodarem juntos: uma dinâmica de sistemas diz **quanto** desmatar e um autômato celular diz **onde**. Essa divisão é a estrutura dos modelos LUCC do encontro 8 em diante. O encontro também abre o projeto final.

**Notebook:** [encontro07_agentes_acoplamento.ipynb](../notebooks/encontro07_agentes_acoplamento.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 25 de exposição, 55 de prática, 15 de fechamento |
| Material | Notebook `encontro07_agentes_acoplamento.ipynb` (21 células, roda em cerca de 11 s) |
| Modelos | `Schelling` do `dissmodel-abm` v0.2.0; `Demanda` e `Alocacao`, escritos no notebook |
| Referência | 50 rodadas do Schelling no TerraME (`goldens/logo/schelling.csv.gz`), `terrame-goldens` v0.1.0 |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, Cap. 25; Railsback e Grimm (2019), cap. 1; Schelling (1971); Grimm et al. (2020), o protocolo ODD usado no relatório do projeto |

**Objetivos**

1. Distinguir agente de célula: quem decide, quem se move, onde está o estado.
2. Explicar segregação como padrão emergente de preferências individuais moderadas.
3. Comparar um modelo estocástico com a referência pela distribuição de muitas rodadas.
4. Acoplar dois modelos no mesmo relógio e conferir que eles contam a mesma coisa.
5. Separar, num modelo de mudança de uso, a quantidade (demanda) da localização (alocação).
6. Esboçar o projeto final.

## Antes da aula

- [ ] Instalar o `dissmodel-abm` pela tag: `pip install "dissmodel-abm @ git+https://github.com/DisSModel/dissmodel-abm.git@v0.2.0"`. Ele ainda não está no PyPI. No Colab, a primeira célula do notebook instala tudo sozinha; o selo **Abrir no Colab** fica no topo do notebook.
- [ ] Conferir acesso a `raw.githubusercontent.com` (Parte 2). Sem rede, copiar `goldens/logo/schelling.csv.gz` do `terrame-goldens` v0.1.0 para a pasta da turma.
- [ ] Rodar o notebook do professor. Números que não mudam: vizinhos do mesmo grupo de 52% para 65% (preferência 3, semente 1); médias de insatisfeitos de 18,0% (TerraME) e 18,2% (DisSModel) no passo 0; floresta de 9.900 para 5.402 células em 30 anos.
- [ ] Levar a folha do esboço do projeto (seção 4 do notebook) impressa ou num formulário; ela é devolvida no encontro 8.
- [ ] Opcional: abrir o Schelling no NetLogo Web para mostrar o mesmo modelo noutra ferramenta (2 min).

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | Retomar o limiar do incêndio: "o padrão saiu de uma regra local; hoje as regras são de indivíduos" | — |
| 5–30 | Exposição | Agente × célula; Schelling; comparar modelos com sorteio; acoplamento; quanto × onde | — |
| 30–45 | Prática | Schelling: início e fim; vizinhos do mesmo grupo; preferência de 1 a 5 | Parte 1 |
| 45–55 | Prática | 50 rodadas contra 50 do TerraME; o grupo de insatisfeitos que esvazia antes da hora | Parte 2 |
| 55–75 | Prática | Demanda + Alocação no mesmo relógio; conferir que contam o mesmo; quatro combinações de taxa e peso | Parte 3 |
| 75–85 | Prática | Esboço do projeto: cada aluno preenche os seis itens | Parte 4 |
| 85–100 | Fechamento | Três alunos leem a pergunta do projeto; ponte para o encontro 8 (demanda, potencial e alocação nos modelos LUCC) | Para casa |

Se o tempo apertar, a Parte 2 pode ser só mostrada. A Parte 3 não deve ser cortada: é a ponte direta para os modelos LUCC.

## Exposição (25 min, cerca de 7 slides)

**1. Agente × célula (6 min).**

| | Autômato celular | Modelo de agentes |
| --- | --- | --- |
| O que muda | o estado da célula | a posição e o estado do agente |
| Quem decide | a regra, igual para todas as células | cada agente, com seus atributos |
| Espaço | é o próprio modelo | é onde os agentes estão |
| Exemplos na área | desmatamento por contágio, crescimento urbano | produtores que decidem o uso do lote, migração, pecuária |

No `dissmodel-abm`, os nomes seguem o TerraME: `Agent`, `Society`, `CellSpace`, colocação aleatória, `Group`. As células são bandas de um `RasterBackend`, o mesmo do encontro 6. É uma extensão alfa (versão 0.2.0), instalada do GitHub; a disciplina só a usa para ler modelos prontos.

**2. Schelling (5 min).** Preferências moderadas (aceitar até 5 de 8 vizinhos do outro grupo) produzem manchas homogêneas. É o exemplo clássico de que o padrão agregado não revela a intenção individual, e um alerta para quem interpreta mapas de uso da terra só pelo resultado.

**3. Comparar modelos com sorteio (4 min).** Ligar ao encontro 6: o Jogo da Vida foi comparado célula a célula; aqui só dá para comparar a distribuição de muitas rodadas, porque TerraME e Python sorteiam números diferentes. Mostrar a figura das duas faixas sobrepostas.

**4. Acoplamento (5 min).** Vários `Model` no mesmo `Environment` rodam na ordem em que foram criados. Um lê o atributo do outro; o acoplamento é só isso. Riscos: a ordem importa (alocar antes de calcular a demanda usa o valor do ano anterior) e os dois precisam contar a mesma coisa nas mesmas unidades.

**5. Quanto × onde (5 min).** A separação que o CLUE (Veldkamp e Fresco, 1996) consagrou e que o LuccME e o DisSLUCC seguem: uma **demanda** externa ao espaço define quanto muda; um **potencial** por célula e uma **alocação** definem onde. O exemplo do notebook tem as três peças, em miniatura: taxa (demanda), vizinhos desmatados mais acaso (potencial) e escolha das células de maior potencial (alocação). O encontro 8 parte daqui.

## Prática (55 min)

O notebook tem uma função de apoio, `rodar(passos, criar, anotar)`, que cria os modelos, roda e anota um valor por passo. O aluno lê e roda; na Parte 3 lê as duas classes (`Demanda` e `Alocacao`, cerca de 25 linhas) e muda parâmetros.

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 1. Schelling | Grade 25 × 25, 593 agentes. Com preferência 3, vizinhos do mesmo grupo sobem de 52% para 65% em 500 passos. Varredura de 1 a 5: 52%, 57%, 65%, 73% e 70%; insatisfeitos no fim de 0% a 27% | A segregação cresce com a preferência até 4; com 5, os agentes não acham lugar e o processo trava |
| 2. Comparação | 50 rodadas de cada lado: médias de 18,0% e 18,2% no passo 0, 9,4% e 9,7% no 50, 4,0% e 4,3% no 100; as faixas se sobrepõem | Comparação por distribuição; o porte reproduz até a peculiaridade do original (o grupo esvazia com 6% ainda insatisfeitos) |
| 3. Acoplamento | Grade 100 × 100 com uma estrada; 2% ao ano: floresta de 9.900 para 5.402 células em 30 anos, igual na demanda e no mapa. Quatro combinações: sem contágio, o desmatamento sai espalhado; com contágio, em faixa ao longo da estrada. Com 3% e contágio, abrem-se frentes novas longe da estrada | A taxa decide a área; o peso dos vizinhos decide a forma. Quando a demanda passa do que a frente comporta, o acaso abre frentes novas |
| 4. Projeto | Seis itens: pergunta, área e período, paradigma, estado e regra, dados, como saber se deu certo | Entregar no encontro 8 |

**Para casa**

1. Schelling com 20% de células livres: a segregação final sobe ou desce?
2. Taxa de desmatamento cai à metade a partir do ano 15 (dica: `self.env.now()` dentro de `Demanda.execute`).
3. Esboço do projeto.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Por que preferência 5 termina menos segregada que 4? | Há só 32 células livres e um agente se move por passo, para uma célula livre sorteada (não para uma que o satisfaça). Com exigência alta, quase toda mudança gera nova insatisfação e o arranjo não se estabiliza em 500 passos; um quarto continua insatisfeito. Segregação precisa de espaço para se reorganizar |
| 2. Corrigir a peculiaridade do original? | Depende da pergunta. Para comparar com o TerraME ou reproduzir um estudo, mantém-se o original e documenta-se. Uma versão corrigida é outro modelo: roda-se como experimento à parte, com nome próprio, e o método descreve a diferença e mostra o efeito nos resultados |
| 3. O que a taxa e o peso mudaram? | A taxa muda a quantidade (área desmatada por ano); o peso dos vizinhos muda a forma (faixa contínua ou pontos espalhados). A taxa se confere com uma série anual de área, como a do PRODES; a forma só com mapas, comparando padrões espaciais (oficina de projeto, encontro 13) |

**Para casa, com os números do teste**

1. Com 20% de células livres (preferência 3, semente 1), os vizinhos do mesmo grupo sobem de 65% para 70%: mais lugares livres, mais chance de achar vizinhança parecida. Os insatisfeitos no fim sobem de 6,1% para 8,4%, efeito do grupo que deixa de verificar quem volta a ficar insatisfeito.
2. Uma solução em `Demanda.execute`:

```python
taxa = self.taxa if self.env.now() < 15 else self.taxa / 2
self.neste_ano = round(taxa * self.floresta)
```

## Achados ao testar

Testado em 31 out 2026 com Python 3.13, dissmodel 0.6.6, dissmodel-abm 0.2.0 e terrame-goldens 0.1.0. O notebook roda sem erro em cerca de 11 s; as 50 rodadas do Schelling levam 2 a 3 s.

1. **A ordem de execução no acoplamento é implícita:** os modelos rodam na ordem em que foram criados no `Environment`. Funciona e o notebook explica, mas um erro de ordem passa em silêncio (a alocação usaria a demanda do ano anterior). Vale documentar no `dissmodel` e, talvez, aceitar uma prioridade explícita.
2. **Schelling tem dois indicadores de insatisfação:** `unhappy` (tamanho do grupo, o que o TerraME mostra) e `percent_unhappy()` (todos os insatisfeitos de fato). O notebook usa o primeiro para comparar com o TerraME e o segundo nas tabelas; o aluno precisa saber qual é qual.
3. **O mesmo `@track_plot` do encontro 5:** as 50 rodadas acumulam valores na série da classe `Schelling`. Não muda o resultado, mas reforça a correção pedida no encontro 5.
4. **O `dissmodel-abm` ainda não está no PyPI**, o que obriga a instalar pelo GitHub e impede um `requirements.txt` só com pacotes do PyPI.
