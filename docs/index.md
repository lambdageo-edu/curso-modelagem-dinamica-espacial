# Modelagem Dinâmica Espacial

**De autômatos celulares a modelos de mudança de uso da terra**

Proposta de disciplina eletiva de pós-graduação, elaborada no grupo LambdaGeo (UFMA). Os encontros começam com modelos pequenos e didáticos (dinâmica de sistemas, autômatos celulares, agentes) e terminam num modelo de mudança de uso e cobertura da terra (LUCC) sobre dados reais. Tudo é feito em Python, com o [DisSModel](https://github.com/DisSModel/dissmodel), o [DisSCube](https://github.com/DisSModel/disscube) e o [DisSLUCC](https://github.com/DisSModel/disslucc), comparados com o TerraME e o LuccME, que continuam sendo a referência.

!!! note "Estado deste material"
    Proposta em elaboração. Os encontros 2 a 7 e 9 a 13 têm notebooks testados; os encontros 1 e 8 têm notas de aula; os seminários (14 e 15) seguem o que está em [Avaliação e projeto](avaliacao.md#seminario).

## Identificação

| Campo | Proposta |
| --- | --- |
| Nome | Modelagem Dinâmica Espacial: de autômatos celulares a modelos de mudança de uso da terra |
| Oferta | Pós-graduação, eletiva; programa e semestre a definir |
| Carga horária | 30 horas-aula (15 encontros de 1h40, isto é, 2 aulas de 50 min por encontro) |
| Créditos | 2 |
| Formato | Presencial, em laboratório, com notebooks Jupyter; os notebooks também abrem no Google Colab |
| Público | Mestrandos e doutorandos com interesse em modelagem ambiental e geoinformática |
| Pré-requisitos | Noções de SIG; não exige programação (os encontros 2 e 3 introduzem Python) |
| Responsável | Sérgio Souza Costa |

Os 15 encontros somam 25 horas de relógio; a conta de 30 horas usa a hora-aula de 50 min.

## Ementa

Conceitos de modelagem dinâmica espacial: espaço, tempo, processo e escala. Paradigmas: dinâmica de sistemas, autômatos celulares e agentes. Panorama das ferramentas (TerraME/LuccME, Dinamica EGO, NetLogo, CLUE/CLUE-S, lulcc, Mesa, PySD, PCRaster). Reprodutibilidade de experimentos computacionais. Modelagem em Python com o DisSModel. Construção de grades e cubos de dados espaciais com o DisSCube. Modelos de mudança de uso e cobertura da terra (LUCC) com o DisSLUCC: demanda, potencial e alocação contínua e discreta, restrições e cenários. Verificação contra implementação de referência, calibração do potencial, validação contra mapas observados, incerteza e sensibilidade.

## Justificativa

A modelagem dinâmica espacial é central em estudos de desmatamento, expansão urbana, zona costeira e cenários de política ambiental, temas frequentes em dissertações e teses da área ambiental. Revisões da área mostram a variedade de abordagens e ferramentas, e apontam como desafios a validação dos resultados e a transparência dos modelos (Verburg et al., 2004; Ren et al., 2019). Comparações entre programas mostram também que ferramentas da mesma família podem produzir mapas diferentes a partir dos mesmos dados (Mas et al., 2014; Mazy e Longaretti, 2023). Aprender a modelar inclui, portanto, aprender a verificar, validar e documentar o que se fez.

No Brasil, o ensino se apoiou por muito tempo no TerraME (Carneiro et al., 2013) e no LuccME (Aguiar et al., 2012), desenvolvidos no INPE e usados em cenários para a Amazônia e para o país (Aguiar et al., 2016; Bezerra et al., 2022). Eles continuam sendo a referência. A disciplina segue a progressão didática dos cursos do INPE (modelos pequenos primeiro, LUCC depois), mas em Python, a linguagem que os alunos já usam em análise de dados, e com dados abertos brasileiros (MapBiomas, PRODES, Brazil Data Cube; Souza et al., 2020; Ferreira et al., 2020).

O DisSModel, o DisSCube e o DisSLUCC são desenvolvidos no LambdaGeo, têm versões publicadas com DOI e foram comparados, componente a componente, com o TerraME e o LuccME. Isso permite mostrar ao aluno não só como construir um modelo, mas como conferir que o programa faz o que o modelo descreve e como registrar a execução para que outra pessoa a repita, no sentido de reprodutibilidade das Academias Nacionais dos EUA (NASEM, 2019). As referências estão na [bibliografia](bibliografia.md).

## Objetivos

**Geral.** Capacitar o aluno a conceber, implementar, executar e verificar modelos dinâmicos espaciais em Python, até um modelo LUCC sobre dados reais.

**Específicos.** Ao final, o aluno deve ser capaz de:

1. Distinguir os paradigmas de modelagem dinâmica e escolher o adequado a uma pergunta de pesquisa.
2. Situar as principais ferramentas da área e saber o que cada uma oferece.
3. Implementar modelos de dinâmica de sistemas e autômatos celulares no DisSModel.
4. Montar uma grade regular com variáveis derivadas de fontes abertas (MapBiomas, PRODES, BDC) no DisSCube.
5. Construir e executar um modelo LUCC com o DisSLUCC, separando demanda, potencial e alocação.
6. Verificar um modelo contra uma referência e validar seus resultados contra um mapa observado, distinguindo as duas coisas.
7. Avaliar a incerteza de um resultado por varredura de parâmetros, sensibilidade e simulações repetidas.
8. Registrar uma execução de modo que outra pessoa consiga repeti-la, e descrever um modelo de forma padronizada.
