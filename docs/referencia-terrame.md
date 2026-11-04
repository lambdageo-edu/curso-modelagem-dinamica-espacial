# O TerraME como referência

Esta disciplina se apoia no trabalho de quem construiu a modelagem dinâmica espacial no Brasil. A progressão dos encontros, a maior parte dos modelos e o modo de pensar um modelo de mudança de uso da terra vêm do **ecossistema TerraME**, desenvolvido no INPE, e dos cursos que o acompanham. O DisSModel, o DisSCube e o DisSLUCC são propostos como uma **alternativa em Python** a esse ecossistema. Por isso a disciplina busca, de propósito, as mesmas ideias, os mesmos modelos e, sempre que possível, os mesmos resultados.

## O curso de referência

O roteiro dos encontros 5 a 7 e a ordem geral da disciplina seguem o curso de modelagem do INPE com o TerraME:

> ANDRADE, P. R.; CÂMARA, G.; BEZERRA, F. G. *CST-323: Introduction to Earth System Modelling / CAP-465: Modelling and Simulation of Earth Systems*. São José dos Campos: INPE. Material na wiki do TerraME: <https://github.com/TerraME/terrame/wiki/course>.

O curso apresenta três paradigmas, dinâmica de sistemas, autômatos celulares e agentes, com exemplos da literatura escritos no TerraME, para alunos sem formação em programação nem em ciências naturais. Termina com um projeto que implementa um modelo publicado e sugere submeter a replicação ao ReScience C. A disciplina adota a mesma progressão, a mesma ideia de começar com modelos pequenos e didáticos e o mesmo tipo de projeto final.

A parte de mudança de uso da terra (encontros 8 a 13) segue a estrutura do **LuccME** e dos cursos de modelagem de mudança de uso da terra do INPE, que usam o LuccME e os seus labs: demanda, potencial e alocação; componentes contínuos e discretos; calibração e validação; cenários.

## O ecossistema TerraME

| Componente | O que é | Referência |
| --- | --- | --- |
| TerraLib | biblioteca de geoprocessamento do INPE, base do TerraME | Câmara et al. (2008) |
| TerraME | ambiente de modelagem dinâmica espacial (INPE e TerraLAB/UFOP), com espaços celulares, agentes, sociedades e relógio | Carneiro et al. (2013) |
| `fill` do TerraME | preenchimento das células com dados de mapas | Carneiro et al. (2013) |
| Pacotes `sysdyn`, `ca` e `logo` | modelos didáticos de dinâmica de sistemas, autômatos celulares e agentes | <https://github.com/TerraME/terrame> |
| LuccME | arcabouço para modelos de mudança de uso da terra sobre o TerraME (INPE/CCST), com os labs usados nos encontros 9 a 13 | Aguiar et al. (2012) |

## O que o DisSModel busca reproduzir

O DisSModel não pretende substituir o TerraME, que continua sendo a referência. Ele leva as mesmas ideias para o Python, a linguagem em que os alunos já analisam dados. Para isso:

- **Mesmos conceitos e nomes.** Ambiente e relógio, espaço celular, vizinhança, agentes e sociedades, demanda, potencial e alocação têm nomes próximos aos do TerraME e do LuccME, para que quem conhece um reconheça o outro.
- **Mesmos modelos.** Quase todos os modelos de `dissmodel-sysdyn`, `dissmodel-ca` e `dissmodel-abm` são portes documentados dos pacotes do TerraME, regra a regra. O DisSLUCC implementa os componentes do LuccME, e o DisSCube, os operadores do `fill`.
- **Mesmos resultados, conferidos.** As saídas do TerraME e do LuccME foram geradas numa imagem Docker fixada (`terrame-docker`) e publicadas com hash (`terrame-goldens`, `luccme-goldens`). Os notebooks comparam o DisSModel com elas: célula a célula nos modelos determinísticos, pela distribuição de muitas rodadas nos estocásticos ([notas de aula do encontro 4](encontros/04-notas.md)). O porte reproduz até as peculiaridades do original, como o grupo de insatisfeitos do Schelling (encontro 7) e a correção de célula que o LuccME não executa (encontro 9), e as documenta.
- **O que ainda não cobre.** Nem todo o TerraME foi portado: o modelo de escoamento (*Runoff*), os componentes do LuccME usados em 11 dos 21 labs e o módulo de redes do `fill` (este parcialmente, no operador `network_cost`) ainda faltam ou estão em andamento. Quem depende deles continua no software original.

## Correspondência com o curso do TerraME

| Aula do curso do TerraME | Encontro | No DisSModel | Comparação com o TerraME |
| --- | --- | --- | --- |
| 1–2. Introdução à computação; Lua para o TerraME | 2 e 3 (Python) | — | — |
| 3–4. Dinâmica de sistemas; retroalimentação | 5 | `dissmodel-sysdyn`: `Tub`, `PopulationGrowth`, `LimitedGrowth` | `terrame-goldens` |
| 5. Epidemias | 5 | `SIR` | `terrame-goldens` |
| 6. Caos | demo do encontro 5 | `Lorenz`, `ChaoticGrowth` | `terrame-goldens` |
| 7. Predador-presa | 5 | `PredatorPrey` | `terrame-goldens` |
| 8. Daisyworld | demo do encontro 5 | `Daisyworld` | `terrame-goldens` |
| 9. Autômato celular | 6 | `dissmodel-ca`: `GameOfLife` e outros | `terrame-goldens` |
| 10. Incêndio na floresta | 6 (e 4) | `FireModel` | `terrame-goldens` (grade e 100 rodadas) |
| 11. Escoamento | — | não portado | — |
| 12. Dados celulares | 10 | DisSCube: operadores do `fill` | `disscube-benchmark` |
| 13. Desmatamento | 7 a 9 | acoplamento demanda e alocação; DisSLUCC | `luccme-goldens`, `disslucc-benchmark` |
| 14–15. Agentes; predador-presa com agentes | 7 | `dissmodel-abm`: `Schelling`, `PredatorPrey` e outros | `terrame-goldens` (50 rodadas) |
| Projeto: implementar um modelo publicado | 13 a 15 | projeto da disciplina | exemplo: `rescience-lulcc` (encontro 4) |

O que a disciplina acrescenta ao curso de referência vem do próprio ecossistema DisSModel: a reprodutibilidade como tema (encontro 4), a montagem de dados abertos numa grade (DisSCube, encontro 10), o modelo de mudança de uso da terra com dados reais (DisSLUCC, encontros 9 a 13) e a validação contra mapas observados (encontro 13).

## Referências

- AGUIAR, A. P. D.; CARNEIRO, T.; ANDRADE, P.; ASSIS, T. LuccME-TerraME: an open-source framework for spatially explicit land use change modelling. *GLP News*, v. 8, p. 21–23, 2012.
- ANDRADE, P. R.; CÂMARA, G.; BEZERRA, F. G. *CST-323: Introduction to Earth System Modelling / CAP-465: Modelling and Simulation of Earth Systems*. São José dos Campos: INPE. Disponível em: <https://github.com/TerraME/terrame/wiki/course>.
- CÂMARA, G. et al. TerraLib: an open source GIS library for large-scale environmental and socio-economic applications. In: HALL, G. B.; LEAHY, M. G. (org.). *Open Source Approaches in Spatial Data Handling*. Berlin: Springer, 2008. p. 247–270. DOI: 10.1007/978-3-540-74831-1_12.
- CARNEIRO, T. G. S.; ANDRADE, P. R.; CÂMARA, G.; MONTEIRO, A. M. V.; PEREIRA, R. R. An extensible toolbox for modeling nature–society interactions. *Environmental Modelling & Software*, v. 46, p. 104–117, 2013. DOI: 10.1016/j.envsoft.2013.03.002.
- TerraME. Código-fonte e pacotes: <https://github.com/TerraME/terrame>.
