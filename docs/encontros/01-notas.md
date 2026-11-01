# Encontro 1 — Notas de aula: o que é modelagem dinâmica espacial

Estas notas acompanham o primeiro encontro e dão a visão da disciplina inteira: o que é um modelo dinâmico espacial, os três paradigmas que vamos estudar, as ferramentas da área, os cuidados que atravessam todos os encontros e o caminho até o projeto final. Leia antes da aula ou logo depois. A seção 7 é a prática do dia, no navegador, sem instalar nada. Os termos em **negrito** estão no glossário.

## 1. Modelo como hipótese

Um **modelo dinâmico** descreve como um sistema muda no tempo. Ele tem três partes: um **estado** (o que se guarda: a população de um município, o uso de cada célula, a posição de cada animal), uma **regra** que altera o estado e um **relógio** que diz quando a regra é aplicada. O modelo é **espacial** quando o estado está distribuído no espaço e a regra depende de onde as coisas estão: a célula ao lado, a distância à estrada, o vizinho mais próximo.

Um modelo não é o sistema. É uma **hipótese** sobre o processo que gera o que observamos, escrita de forma precisa o bastante para que um computador a execute. Rodar o modelo é perguntar o que a hipótese implica; comparar o resultado com dados é perguntar se ela se sustenta. Essa leitura muda a pergunta que se faz a um modelo: não "ele está certo?", mas "o que ele explica, e onde falha?".

Modelos dinâmicos espaciais costumam servir a três propósitos, com graus de cautela diferentes:

| Propósito | Pergunta | Exemplo |
| --- | --- | --- |
| Entender | Que mecanismo produz este padrão? | Por que o desmatamento avança em "espinha de peixe" ao longo das estradas? |
| Explorar cenários | O que acontece se...? | E se as unidades de conservação forem respeitadas? |
| Prever | Como estará em 2040? | Quanto do Cerrado maranhense será soja? (com muita cautela; ver seção 5) |

## 2. Espaço, tempo, processo e escala

Quatro conceitos organizam qualquer modelo da disciplina (Couclelis, 2002):

| Conceito | Pergunta | Opções comuns |
| --- | --- | --- |
| **Espaço** | Onde está o estado? | grade regular de células; polígonos (municípios, lotes); rede (estradas, rios); agentes com posição |
| **Tempo** | Quando o estado muda? | passos discretos (um ano, um dia); tempo contínuo aproximado por passos pequenos |
| **Processo** | Como o estado muda? | equação (fluxo proporcional ao estoque); regra local (a célula pega fogo se a vizinha queima); decisão (o agente se muda se está insatisfeito) |
| **Escala** | Com que extensão e resolução? | extensão: a área e o período estudados; resolução: o tamanho da célula e do passo |

A escala não é detalhe técnico: mudar a resolução muda o resultado. Uma célula de 30 m é floresta ou pasto; uma de 5 km tem 40% de floresta e 60% de pasto, e o modelo precisa tratar frações. Um passo anual não vê o ciclo das chuvas. O encontro 8 volta a isso para os modelos de uso da terra, e o encontro 13 mostra que um modelo pode errar na célula e acertar em blocos maiores.

## 3. Três paradigmas

A disciplina estuda três maneiras de escrever a regra, em ordem de complexidade espacial.

| Paradigma | O que representa | Unidade do estado | Exemplo clássico | Encontro |
| --- | --- | --- | --- | --- |
| **Dinâmica de sistemas** | estoques e fluxos, com retroalimentação | quantidades agregadas, sem espaço | predador e presa (Lotka-Volterra); epidemia (SIR) | 5 |
| **Autômato celular** | células com estado, mudando por regra de vizinhança | cada célula da grade | Jogo da Vida; propagação de incêndio | 6 |
| **Modelo baseado em agentes** | indivíduos que percebem, decidem e se movem | cada agente | segregação de Schelling | 7 |

**Dinâmica de sistemas** (Ford, 2009; Sterman, 2000) olha o sistema de cima: quanto há em cada estoque e com que taxa ele enche ou esvazia. É o modo natural de calcular *quanto* muda (quantos hectares por ano, quantos infectados por semana).

**Autômatos celulares** (Toffoli e Margolus, 1987) põem a regra em cada célula. Regras locais simples produzem padrões globais que nenhuma célula "conhece": manchas, frentes, limiares. O Jogo da Vida, de John Conway, divulgado por Gardner (1970), é o exemplo mais conhecido.

**Agentes** (Railsback e Grimm, 2019) representam indivíduos com comportamento próprio. Schelling (1971) mostrou que preferências individuais moderadas podem gerar segregação forte no agregado, um resultado que não se tira olhando um agente só.

Modelos de mudança de uso da terra combinam os três: uma dinâmica de sistemas calcula **quanto** muda (a demanda), e uma regra espacial decide **onde** (a alocação), às vezes com agentes tomando as decisões (Verburg et al., 2004). O encontro 7 acopla os dois primeiros num modelo pequeno; os encontros 8 a 12 fazem isso com dados reais.

## 4. Ferramentas

A área tem muitas ferramentas, com propósitos, linguagens e licenças diferentes:

| Ferramenta | Origem | Paradigma principal | Linguagem | Licença |
| --- | --- | --- | --- | --- |
| TerraME e LuccME | INPE | os três; uso da terra | Lua | aberta |
| NetLogo | Northwestern University | agentes e autômatos | linguagem própria (Logo) | aberta |
| Dinamica EGO | UFMG | autômatos; uso da terra | interface gráfica | gratuita, proprietária |
| CLUE-S | Universidade de Wageningen | uso da terra | programa para Windows | gratuita |
| lulcc | Imperial College London | uso da terra | R | aberta |
| Mesa | comunidade | agentes | Python | aberta |
| PySD | comunidade | dinâmica de sistemas | Python | aberta |
| PCRaster | Universidade de Utrecht | processos em grade | Python e C++ | aberta |
| DisSModel, DisSCube e DisSLUCC | LambdaGeo/UFMA | os três; dados; uso da terra | Python | aberta |

As referências de cada uma estão na [bibliografia](../bibliografia.md): Carneiro et al. (2013) e Aguiar et al. (2012) para TerraME e LuccME; Wilensky (1999) para o NetLogo; Soares-Filho, Cerqueira e Pennachin (2002) para o Dinamica; Verburg et al. (2002) para o CLUE-S; Moulds, Buytaert e Mijic (2015) para o lulcc; Kazil, Masad e Crooks (2020) para o Mesa; Martin-Martinez et al. (2022) para o PySD; Karssenberg et al. (2010) para o PCRaster.

**Por que Python e por que o DisSModel.** O TerraME e o LuccME, do INPE, são a referência da modelagem dinâmica espacial no Brasil, e os cursos de modelagem do INPE seguem a progressão que esta disciplina adota. A disciplina usa Python porque é a linguagem em que os alunos já fazem análise de dados, e usa o DisSModel, o DisSCube e o DisSLUCC porque foram construídos para reproduzir esses modelos: cada notebook compara o resultado com a saída publicada do TerraME ou do LuccME. Assim, além de aprender a modelar, o aluno vê como se confere um programa contra uma referência.

Ferramentas da mesma família nem sempre dão o mesmo resultado com os mesmos dados (Mas et al., 2014). Saber qual programa, qual versão e quais escolhas internas produziram um mapa é parte do método, e não detalhe.

## 5. Três cuidados que atravessam a disciplina

Três palavras aparecem em quase todos os encontros. Vale separá-las desde já.

**Verificação** é conferir que o programa faz o que o modelo descreve: o código está certo? Nos encontros 5 a 7 e 9 a 11, cada modelo do DisSModel é comparado com a saída do TerraME ou do LuccME para os mesmos dados. Verificar não diz nada sobre o mundo.

**Validação** é conferir se o modelo se parece com o mundo: o mapa simulado bate com o observado? Para isso se compara com um período que não entrou no ajuste, e com um modelo nulo, como "nada muda" (Pontius et al., 2008). É o tema do encontro 13. Um modelo pode estar perfeitamente verificado e mal validado.

**Reprodutibilidade** é obter o mesmo resultado com os mesmos dados, o mesmo código e as mesmas condições; **replicabilidade** é chegar a resultados compatíveis com dados novos (NASEM, 2019). O encontro 4 mostra como registrar uma execução (versões, semente, hash dos dados) para que outra pessoa a repita, e isso é cobrado no projeto.

Um quarto tema, a **incerteza**, aparece no encontro 12: o quanto o resultado muda quando os parâmetros mudam dentro do que é plausível.

## 6. O percurso da disciplina

A disciplina tem 15 encontros de 1h40, em cinco módulos. Os modelos começam pequenos e didáticos e terminam num modelo de mudança de uso da terra sobre dados reais, aplicado à área de cada aluno.

| Encontros | Módulo | Ao final, o aluno sabe |
| --- | --- | --- |
| 1 | Fundamentos | o que é um modelo dinâmico espacial e em que paradigma uma pergunta se encaixa |
| 2 e 3 | Python | ler e alterar um notebook; trabalhar com grades, tabelas, rasters e vetores |
| 4 a 7 | Reprodutibilidade e paradigmas | registrar uma execução; rodar e modificar modelos de dinâmica de sistemas, autômatos e agentes no DisSModel, comparando com o TerraME |
| 8 a 12 | Mudança de uso da terra | ler um estudo de cenários; rodar um modelo LUCC no DisSLUCC; montar a grade de dados com o DisSCube; ajustar o potencial; avaliar a incerteza |
| 13 a 15 | Projeto | validar o próprio modelo contra o mapa observado e apresentá-lo |

O [cronograma](../cronograma.md) detalha cada encontro.

**Como os encontros funcionam.** A maioria tem uma exposição curta seguida de prática num notebook Jupyter, que o aluno termina em casa. Os notebooks vêm com o código pronto: não é preciso saber programar para começar. Duas marcas indicam o que fazer: 🔧 troque um número e rode de novo; ✏️ responda à pergunta. Todos abrem no Google Colab pelo selo no topo, sem instalar nada; quem preferir instala o ambiente descrito em [Metodologia e ambiente](../metodologia.md). O encontro 8 é diferente: leitura e comparação de dois estudos publicados.

**Avaliação.** Exercícios (30%, três notebooks com o "para casa"), projeto (50%) e seminário (20%). Os critérios estão em [Avaliação e projeto](../avaliacao.md).

**O projeto.** Cada aluno constrói um modelo ligado à sua pesquisa: de preferência um modelo de uso da terra sobre um recorte do Maranhão ou da Amazônia, ou um autômato celular ou modelo de dinâmica de sistemas ligado à dissertação. O projeto cresce junto com a disciplina:

| Encontro | Etapa do projeto |
| --- | --- |
| 1 | a ideia, em três linhas (o "para casa" de hoje) |
| 7 | esboço de uma página (entregue no 8) |
| 10 | a grade de dados da área, com o DisSCube |
| 11 | a regressão do potencial |
| 12 | primeira conferência com o professor |
| 13 | validação contra o mapa observado |
| 14 ou 15 | seminário |
| duas semanas depois do 15 | relatório (descrição pelo protocolo ODD; Grimm et al., 2020) e repositório |

## 7. Prática: três modelos no NetLogo Web

Em duplas. Abra o NetLogo Web em <https://www.netlogoweb.org/launch> e escolha os modelos na biblioteca (*Sample Models*). Em cada um, clique em **setup** e depois em **go**; mude um controle e repita. Anote o que observar: os três modelos voltam nos encontros 5 a 7, escritos em Python.

**Fire** (em *Earth Science*). Uma floresta com uma linha de fogo à esquerda; cada árvore em chamas acende as vizinhas.

- Rode com densidade de floresta de 50%, 59% e 70%, mais de uma vez cada.
- ✏️ O fogo atravessa a floresta em todos os casos? O que acontece perto de 59%?
- ✏️ Em que paradigma está este modelo? Qual é o estado de cada célula, e qual é a regra?

**Wolf Sheep Predation** (em *Biology*). Lobos comem ovelhas, ovelhas comem grama.

- Rode sem o crescimento da grama (opção *sheep-wolves*) e com ele (*sheep-wolves-grass*). Depois mude a taxa de reprodução dos lobos.
- ✏️ As populações oscilam? Alguma desaparece? O resultado é igual em duas rodadas com os mesmos controles?
- ✏️ O gráfico de populações ignora onde estão os animais. Que paradigma descreveria só esse gráfico?

**Segregation** (em *Social Science*). Duas cores de agentes; cada um se muda se tem poucos vizinhos da mesma cor.

- Rode com a porcentagem de vizinhos parecidos desejada (*%-similar-wanted*) em 30%, 50% e 80%.
- ✏️ A cidade final fica mais segregada do que cada agente exige? O que acontece com 80%?
- ✏️ Qual é o estado, a regra e o espaço deste modelo?

Para fechar, cada dupla diz à turma, em uma frase por modelo, o paradigma e o que mudou ao variar o controle.

## 8. Para casa

Escolha um processo ligado à sua pesquisa (o avanço de uma frente de desmatamento, a ocupação de um bairro, a perda de manguezal, a dispersão de uma espécie) e escreva, em três linhas:

1. **Estado:** o que cada célula (ou agente, ou estoque) guarda.
2. **Regra:** como esse estado muda a cada passo.
3. **Espaço e tempo:** a área, o tamanho da célula e o passo.

É a semente do esboço do projeto (encontro 7). Para o encontro 2, abra um notebook no Google Colab, ou instale o ambiente da disciplina.

**Leitura:** livro *Geospatial Modeling with Python*, cap. 17; Couclelis (2002); Verburg et al. (2004).

## Glossário

| Termo | Significado |
| --- | --- |
| Agente | entidade com estado e comportamento próprios, que percebe o entorno e decide |
| Autômato celular | grade de células em que cada uma muda de estado por uma regra que depende das vizinhas |
| Dinâmica de sistemas | modelo de estoques e fluxos, com retroalimentação, sem representar o espaço |
| Escala | extensão (área e período) e resolução (tamanho da célula e do passo) de um modelo |
| Estado | o que o modelo guarda em cada momento |
| Incerteza | o quanto o resultado muda quando parâmetros e dados mudam dentro do plausível |
| Modelo nulo | alternativa simples (por exemplo, "nada muda") com que o modelo é comparado |
| Regra | o procedimento que altera o estado a cada passo |
| Replicabilidade | obter resultados compatíveis num estudo novo, com dados novos |
| Reprodutibilidade | obter o mesmo resultado com os mesmos dados, código e condições |
| Validação | comparação do modelo com dados observados que não entraram no ajuste |
| Verificação | conferência de que o programa implementa corretamente o modelo |

## Referências

Estas referências estão também na [bibliografia](../bibliografia.md), com a situação de cada uma.

- AGUIAR, A. P. D.; CARNEIRO, T.; ANDRADE, P.; ASSIS, T. LuccME-TerraME: an open-source framework for spatially explicit land use change modelling. *GLP News*, v. 8, p. 21–23, 2012.
- CARNEIRO, T. G. S. et al. An extensible toolbox for modeling nature–society interactions. *Environmental Modelling & Software*, v. 46, p. 104–117, 2013. DOI: 10.1016/j.envsoft.2013.03.002.
- COUCLELIS, H. Modeling frameworks, paradigms and approaches. In: CLARKE, K. C.; PARKS, B. O.; CRANE, M. P. (org.). *Geographic Information Systems and Environmental Modeling*. Upper Saddle River: Prentice Hall, 2002.
- FORD, A. *Modeling the Environment*. 2. ed. Washington: Island Press, 2009.
- GARDNER, M. Mathematical games: the fantastic combinations of John Conway's new solitaire game "life". *Scientific American*, v. 223, n. 4, p. 120–123, 1970.
- GRIMM, V. et al. The ODD protocol for describing agent-based and other simulation models: a second update to improve clarity, replication, and structural realism. *Journal of Artificial Societies and Social Simulation*, v. 23, n. 2, 7, 2020. DOI: 10.18564/jasss.4259.
- KARSSENBERG, D. et al. A software framework for construction of process-based stochastic spatio-temporal models and data assimilation. *Environmental Modelling & Software*, v. 25, n. 4, p. 489–502, 2010.
- KAZIL, J.; MASAD, D.; CROOKS, A. Utilizing Python for agent-based modeling: the Mesa framework. In: *Social, Cultural, and Behavioral Modeling (SBP-BRiMS 2020)*. Cham: Springer, 2020. p. 308–317.
- MARTIN-MARTINEZ, E. et al. PySD: System Dynamics Modeling in Python. *Journal of Open Source Software*, v. 7, n. 78, 4329, 2022.
- MAS, J.-F. et al. Inductive pattern-based land use/cover change models: a comparison of four software packages. *Environmental Modelling & Software*, v. 51, p. 94–111, 2014. DOI: 10.1016/j.envsoft.2013.09.010.
- MOULDS, S.; BUYTAERT, W.; MIJIC, A. An open and extensible framework for spatially explicit land use change modelling: the lulcc R package. *Geoscientific Model Development*, v. 8, n. 10, p. 3215–3229, 2015. DOI: 10.5194/gmd-8-3215-2015.
- NATIONAL ACADEMIES OF SCIENCES, ENGINEERING, AND MEDICINE. *Reproducibility and Replicability in Science*. Washington: The National Academies Press, 2019. DOI: 10.17226/25303.
- PONTIUS JR., R. G. et al. Comparing the input, output, and validation maps for several models of land change. *The Annals of Regional Science*, v. 42, n. 1, p. 11–37, 2008. DOI: 10.1007/s00168-007-0138-2.
- RAILSBACK, S. F.; GRIMM, V. *Agent-Based and Individual-Based Modeling: A Practical Introduction*. 2. ed. Princeton: Princeton University Press, 2019.
- SCHELLING, T. C. Dynamic models of segregation. *Journal of Mathematical Sociology*, v. 1, n. 2, p. 143–186, 1971.
- SOARES-FILHO, B. S.; CERQUEIRA, G. C.; PENNACHIN, C. L. DINAMICA: a stochastic cellular automata model designed to simulate the landscape dynamics in an Amazonian colonization frontier. *Ecological Modelling*, v. 154, n. 3, p. 217–235, 2002. DOI: 10.1016/S0304-3800(02)00059-5.
- STERMAN, J. D. *Business Dynamics: Systems Thinking and Modeling for a Complex World*. Boston: McGraw-Hill, 2000.
- TOFFOLI, T.; MARGOLUS, N. *Cellular Automata Machines*. Cambridge: MIT Press, 1987.
- VERBURG, P. H. et al. Modeling the spatial dynamics of regional land use: the CLUE-S model. *Environmental Management*, v. 30, n. 3, p. 391–405, 2002. DOI: 10.1007/s00267-002-2630-x.
- VERBURG, P. H. et al. Land use change modelling: current practice and research priorities. *GeoJournal*, v. 61, n. 4, p. 309–324, 2004. DOI: 10.1007/s10708-004-4946-y.
- WILENSKY, U. *NetLogo*. Evanston: Center for Connected Learning and Computer-Based Modeling, Northwestern University, 1999. Disponível em: <https://ccl.northwestern.edu/netlogo/>.
