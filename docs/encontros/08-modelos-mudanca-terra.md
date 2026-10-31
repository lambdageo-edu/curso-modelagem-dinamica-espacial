# Encontro 8 — Modelos de mudança de uso e cobertura da terra

O aluno sai do encontro com o vocabulário dos modelos LUCC (forças motrizes, drivers, escala, demanda, potencial, alocação, cenários, calibração e validação), tendo comparado dois estudos publicados e listado as variáveis explicativas do próprio projeto. É o único encontro sem notebook: o material é um texto de notas de aula e uma ficha de leitura em grupo.

**Material do aluno:** [Notas de aula](08-notas.md) · [Ficha de leitura](08-ficha.md)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 10 de abertura, 35 de exposição, 30 de leitura dirigida, 15 de comparação, 10 de fechamento |
| Pré-requisito | Encontro 7 (quanto × onde); leitura de um dos dois artigos antes da aula |
| Material | Notas de aula (texto-base, 8 seções); ficha de leitura; slides da exposição |
| Artigos | Soares-Filho et al. (2006), *Nature*; Aguiar et al. (2016), *Global Change Biology* |
| Leitura de apoio | Notas de aula; livro *Geospatial Modeling with Python*, Cap. 26 |

**Objetivos**

1. Distinguir uso de cobertura e causas diretas de forças subjacentes.
2. Explicar como drivers espaciais aproximam as forças motrizes num modelo.
3. Situar as principais ferramentas (CLUE/CLUE-S, LuccME, Dinamica EGO, Land Change Modeler, SLEUTH) pela abordagem que usam.
4. Descrever a estrutura demanda, potencial e alocação.
5. Explicar a diferença entre cenário e previsão, e traduzir uma narrativa em parâmetros.
6. Distinguir calibração, validação e verificação, e explicar o papel do modelo nulo.
7. Ler criticamente o método de um estudo de cenários.

## Antes da aula

- [ ] Uma semana antes: dividir a turma em duas metades, cada uma com um artigo, e pedir a leitura junto com as notas de aula.
- [ ] Conferir as referências dos dois artigos (volume e páginas) e deixar os PDFs na pasta da turma, com o material suplementar.
- [ ] Ler os dois artigos com a ficha em mãos e preencher uma versão do professor, para conduzir a comparação. O material suplementar costuma ter o método completo.
- [ ] Preparar cerca de 10 slides para a exposição, seguindo as seções 2 a 7 das notas.
- [ ] Imprimir a ficha (uma por grupo) ou deixá-la num documento compartilhado.

## Roteiro

| Tempo (min) | Bloco | Atividade | Material |
| --- | --- | --- | --- |
| 0–10 | Abertura | Retomar o "quanto × onde" do encontro 7: o que um modelo de verdade precisa a mais que aquele exemplo? Anotar as respostas no quadro | — |
| 10–45 | Exposição | Forças motrizes; drivers; escala; abordagens e ferramentas; demanda, potencial e alocação; cenários; calibração, validação e modelo nulo | Notas, seções 1 a 7 |
| 45–75 | Leitura dirigida | Grupos de 3 ou 4 preenchem a ficha sobre o artigo que leram | Ficha |
| 75–90 | Comparação | Cada grupo apresenta em 5 min; o professor monta a tabela A × B no quadro e conduz as perguntas da ficha | Ficha |
| 90–100 | Fechamento | Lista de drivers da turma; cada aluno preenche os três drivers do próprio projeto. Ponte para o encontro 9 | Ficha, parte final |

Se a turma não tiver lido os artigos, trocar a leitura dirigida por uma leitura guiada pelo professor, só do resumo, das figuras de cenários e da seção de método, com a ficha projetada.

## Exposição (35 min, cerca de 10 slides)

Os blocos seguem as seções das notas de aula; os tempos são indicativos.

| Seção das notas | Tempo | Ponto central | Exemplo para mostrar |
| --- | --- | --- | --- |
| 1. O que o modelo responde | 3 min | Quanto, onde, por quê, e se; uso × cobertura | Campo nativo × pastagem no MapBiomas |
| 2. Forças motrizes | 6 min | Causas diretas × forças subjacentes; drivers como aproximações | Tabela de drivers e o que cada um aproxima |
| 3. Escala | 4 min | Extensão × resolução; demanda regional, alocação local | Mesma área em células de 30 m e de 5 km |
| 4. Abordagens | 6 min | Estatística, pesos de evidência, aprendizado de máquina, autômato urbano, agentes, econômica | Tabela das ferramentas e licenças |
| 5. Demanda, potencial, alocação | 7 min | A demanda decide quanto; o potencial decide onde | Retomar o notebook do encontro 7 |
| 6. Cenários | 5 min | Narrativa traduzida em números; cenário não é previsão; o valor está na diferença entre cenários | Tabela narrativa → parâmetro |
| 7. Calibração e validação | 4 min | Período de calibração × de validação; modelo nulo; quantidade × localização; verificação é outra coisa | Desenho de linha do tempo com os dois períodos |

## Respostas esperadas para a comparação

As respostas da ficha dependem da leitura dos artigos e devem ser conferidas pelo professor na versão que preparar antes da aula. Pontos que a discussão deve alcançar:

| Pergunta | O que a turma deve perceber |
| --- | --- |
| 1. Mesma pergunta? | Os dois tratam da Amazônia sob cenários de política, mas um enfatiza conservação e áreas protegidas, e o outro, emissões e transição florestal. A pergunta define o que o modelo precisa representar |
| 2. Drivers em comum | Acesso (estradas, distância a mercados) e áreas protegidas costumam aparecer nos dois; diferenças refletem a pergunta, a resolução e os dados disponíveis |
| 3. Diferença entre cenários | Na maior parte dos estudos de política, os cenários diferem sobretudo na demanda e nas restrições, não no potencial |
| 4. Modelo nulo | Se não houver comparação com o modelo nulo, a validação diz pouco sobre o mérito do modelo; é uma prática que a disciplina pede no projeto |
| 5. Repetir o resultado | Ponte com o encontro 4: código, dados, versões e parâmetros publicados? Em geral, falta pelo menos um deles |

## Achados ao preparar

1. **As referências dos dois artigos foram listadas sem consulta às fontes.** Conferir volume, páginas e o acesso aos PDFs (o de *Nature* pode exigir assinatura) antes de distribuir.
2. **Alternativa regional:** se houver interesse em Cerrado ou Maranhão, trocar um dos artigos por um estudo da região; a ficha funciona com qualquer estudo de cenários.
3. **A tabela de ferramentas nas notas** (origem e licença) deve ser revista a cada oferta: licenças e versões mudam.
