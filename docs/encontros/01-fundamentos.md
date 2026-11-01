# Encontro 1 — O que é modelagem dinâmica espacial

O aluno sai do encontro sabendo dizer o que é um modelo dinâmico espacial, com os quatro conceitos que a disciplina usa (espaço, tempo, processo e escala). Ele também sabe em que paradigma se encaixa cada um de três modelos que rodou no navegador e o que a disciplina vai pedir dele. Não há programação: os três modelos do NetLogo Web voltam nos encontros 5 a 7, já em Python.

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 10 de apresentação da disciplina, 35 de exposição, 40 de prática, 15 de fechamento |
| Material | Slides; NetLogo Web (<https://www.netlogoweb.org/launch>), no navegador, sem instalação |
| Modelos | Da biblioteca do NetLogo: Fire (incêndio), Wolf Sheep Predation (predador-presa) e Segregation (segregação) |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, cap. 17 (paradigmas e ferramentas); Couclelis (2002); Verburg et al. (2004) |

**Objetivos**

1. Definir modelo dinâmico espacial: estado, regra de mudança, espaço e tempo.
2. Tratar um modelo como hipótese sobre um processo, e não como retrato do mundo.
3. Distinguir os três paradigmas da disciplina: dinâmica de sistemas, autômatos celulares e agentes.
4. Situar as principais ferramentas (TerraME/LuccME, NetLogo, Dinamica EGO, CLUE-S, lulcc, Mesa, PySD, PCRaster) pela linguagem, pela licença e pelo uso.
5. Conhecer o plano da disciplina, a avaliação e o projeto.

## Antes da aula

- [ ] Abrir os três modelos no NetLogo Web, na rede do laboratório, e conferir os nomes na biblioteca (*Sample Models*): Fire em Earth Science, Wolf Sheep Predation em Biology, Segregation em Social Science. A biblioteca pode mudar de organização entre versões.
- [ ] Testar o acesso a `raw.githubusercontent.com` e ao Colab, que os encontros seguintes usam.
- [ ] Preparar cerca de 10 slides: definição, os quatro conceitos, os três paradigmas, a tabela de ferramentas, o cronograma, a avaliação.
- [ ] Pedir a instalação do ambiente (ver [Metodologia](../metodologia.md)) para o encontro 2, ou indicar o Colab.

## Roteiro

| Tempo (min) | Bloco | Atividade |
| --- | --- | --- |
| 0–10 | Apresentação | A disciplina em uma frase: "de autômatos celulares a um modelo de uso da terra, verificado e repetível". Cronograma, avaliação, projeto |
| 10–45 | Exposição | Modelo como hipótese; espaço, tempo, processo e escala; três paradigmas; panorama das ferramentas |
| 45–85 | Prática | Três modelos no NetLogo Web, em duplas, com as perguntas abaixo |
| 85–100 | Fechamento | Cada dupla diz o paradigma de cada modelo e o que mudou ao variar um parâmetro; ponte para o encontro 2 |

## Exposição (35 min, cerca de 10 slides)

**1. Modelo como hipótese (8 min).** Um modelo dinâmico é uma afirmação sobre como um sistema muda: um estado, uma regra que o altera e um relógio. Ele não é o sistema. Rodar o modelo é perguntar o que a hipótese implica; comparar com dados é perguntar se ela se sustenta. Essa distinção volta nos encontros 9 (verificação) e 13 (validação).

**2. Espaço, tempo, processo e escala (8 min).** O espaço pode ser uma grade de células, uma rede ou um conjunto de agentes; o tempo avança em passos; o processo é a regra; a escala é a extensão e a resolução no espaço e no tempo. Mudar a escala muda o resultado (encontros 8 e 13).

**3. Três paradigmas (9 min).** Dinâmica de sistemas: estoques e fluxos, sem espaço (encontro 5; Ford, 2009). Autômatos celulares: células com estado e regra de vizinhança (encontro 6). Agentes: indivíduos que decidem e se movem (encontro 7; Railsback e Grimm, 2019). Modelos de uso da terra combinam os três (encontro 8; Verburg et al., 2004).

**4. Ferramentas (10 min).** A tabela abaixo, com o recado de que a disciplina usa Python, mas compara com o TerraME e o LuccME, que continuam sendo a referência:

| Ferramenta | Paradigma principal | Linguagem | Licença |
| --- | --- | --- | --- |
| TerraME / LuccME (INPE) | os três; LUCC | Lua | aberta (LGPL) |
| NetLogo | agentes e autômatos | Logo | aberta (GPL) |
| Dinamica EGO (UFMG) | autômatos, LUCC | interface gráfica | gratuita, proprietária |
| CLUE-S (Wageningen) | LUCC | programa para Windows | gratuita |
| lulcc | LUCC | R | aberta (GPL) |
| Mesa | agentes | Python | aberta |
| PySD | dinâmica de sistemas | Python | aberta |
| PCRaster | autômatos e processos em raster | Python e C++ | aberta |
| DisSModel, DisSCube, DisSLUCC | os três; LUCC | Python | aberta (MIT) |

As referências de cada ferramenta estão na [bibliografia](../bibliografia.md) e no capítulo 17 do livro. Rever licenças e versões a cada oferta.

## Prática (40 min)

Em duplas, no NetLogo Web. Cada modelo tem um parâmetro para variar e uma pergunta.

| Modelo | O que fazer | Pergunta | Volta no encontro |
| --- | --- | --- | --- |
| Fire | Rodar com densidade de floresta de 50%, 59% e 70% | O fogo atravessa a floresta em todos os casos? O que muda perto de 59%? | 6 (incêndio e densidade crítica) |
| Wolf Sheep Predation | Rodar com e sem o crescimento da grama; mudar a taxa de reprodução dos lobos | As populações oscilam? Alguma desaparece? | 5 (predador-presa) |
| Segregation | Mudar a porcentagem de vizinhos parecidos desejada de 30% para 50% e 80% | A cidade fica mais segregada do que cada agente quer? | 7 (Schelling) |

Para casa: escolher um processo da própria pesquisa e escrever, em três linhas, o estado, a regra e o espaço que um modelo dele teria. É a semente do esboço do projeto (encontro 7).

## Respostas esperadas

| Modelo | Resposta esperada |
| --- | --- |
| Fire | Abaixo de cerca de 59%, o fogo para antes de atravessar; acima, atravessa quase sempre. É um limiar de conectividade (percolação): uma mudança pequena no parâmetro muda o resultado de natureza. O encontro 6 mostra o mesmo efeito no DisSModel |
| Wolf Sheep Predation | Sem a grama, é comum uma das populações desaparecer; com a grama, as populações tendem a oscilar. O equilíbrio depende dos parâmetros, e o modelo com sorteio dá trajetórias diferentes a cada rodada |
| Segregation | Mesmo com preferências moderadas (30%), surgem manchas homogêneas: o padrão agregado não revela a intenção de cada agente. Com exigências altas, os agentes não acham lugar e o processo não se estabiliza |

Os números exatos dependem da versão dos modelos no NetLogo Web; conferir na preparação.

## Achados ao preparar

1. **O encontro não foi testado em sala.** Os três modelos e os nomes da biblioteca devem ser conferidos no NetLogo Web antes da aula.
2. **O limiar do incêndio do NetLogo (por volta de 59%) não é o mesmo número do encontro 6**, que usa outra regra de vizinhança e outra grade. Dizer isso aos alunos evita que procurem o mesmo número.
