# Modelagem Dinâmica Espacial

**De autômatos celulares a modelos de mudança de uso da terra**

Proposta de disciplina eletiva de pós-graduação, elaborada no grupo LambdaGeo (UFMA). Os encontros começam com modelos pequenos e didáticos (dinâmica de sistemas, autômatos celulares, agentes) e terminam num modelo de mudança de uso e cobertura da terra (LUCC) sobre dados reais. Tudo é feito em Python, com o [DisSModel](https://github.com/DisSModel/dissmodel), o [DisSCube](https://github.com/DisSModel/disscube) e o [DisSLUCC](https://github.com/DisSModel/disslucc), comparados com o TerraME e o LuccME, que continuam sendo a referência.

!!! note "Estado deste material"
    Proposta em elaboração. Os roteiros e o material dos encontros 2 a 12 estão prontos (notebooks testados nos encontros 2 a 7 e 9 a 12; notas de aula e ficha de leitura no 8); os demais encontros têm só o tema no [cronograma](cronograma.md).

## Identificação

| Campo | Proposta |
| --- | --- |
| Nome | Modelagem Dinâmica Espacial: de autômatos celulares a modelos de mudança de uso da terra |
| Oferta | Pós-graduação, eletiva; programa e semestre a definir |
| Carga horária | 30 horas-aula (15 encontros de 1h40, isto é, 2 aulas de 50 min por encontro) |
| Créditos | 2 |
| Formato | Presencial, em laboratório, com notebooks Jupyter |
| Público | Mestrandos e doutorandos com interesse em modelagem ambiental e geoinformática |
| Pré-requisitos | Noções de SIG; não exige programação (os encontros 2 e 3 introduzem Python) |
| Responsável | Sérgio Souza Costa |

Os 15 encontros somam 25 horas de relógio; a conta de 30 horas usa a hora-aula de 50 min.

## Ementa

Conceitos de modelagem dinâmica espacial: espaço, tempo, processo e escala. Paradigmas: dinâmica de sistemas, autômatos celulares e agentes. Panorama das ferramentas (TerraME/LuccME, Dinamica EGO, NetLogo, CLUE/CLUE-S, Mesa, PySD, PCRaster). Modelagem em Python com o DisSModel. Construção de grades e cubos de dados espaciais com o DisSCube. Modelos de mudança de uso e cobertura da terra (LUCC) com o DisSLUCC: demanda, potencial e alocação. Verificação contra implementação de referência, calibração, validação e reprodutibilidade.

## Justificativa

A modelagem dinâmica é central em estudos de desmatamento, expansão urbana, zona costeira e cenários de política ambiental, temas frequentes em dissertações e teses da área ambiental. O ensino na área se apoiou por muito tempo no TerraME e nos cursos do INPE, que continuam sendo a referência; a disciplina segue a mesma progressão didática (modelos pequenos primeiro, LUCC depois), mas em Python, a linguagem que os alunos já usam em análise de dados. O DisSModel, o DisSCube e o DisSLUCC são desenvolvidos no LambdaGeo, têm versões publicadas com DOI e foram comparados com o TerraME e o LuccME, o que permite mostrar ao aluno não só como construir um modelo, mas como verificar e repetir o resultado.

## Objetivos

**Geral.** Capacitar o aluno a conceber, implementar, executar e verificar modelos dinâmicos espaciais em Python, até um modelo LUCC sobre dados reais.

**Específicos.** Ao final, o aluno deve ser capaz de:

1. Distinguir os paradigmas de modelagem dinâmica e escolher o adequado a uma pergunta de pesquisa.
2. Situar as principais ferramentas da área e saber o que cada uma oferece.
3. Implementar modelos de dinâmica de sistemas e autômatos celulares no DisSModel.
4. Montar uma grade regular com variáveis derivadas de fontes abertas (MapBiomas, PRODES, BDC) no DisSCube.
5. Construir e executar um modelo LUCC com o DisSLUCC, separando demanda, potencial e alocação.
6. Verificar um modelo contra uma referência e validar seus resultados, distinguindo as duas coisas.
7. Registrar uma execução de modo que outra pessoa consiga repeti-la.
