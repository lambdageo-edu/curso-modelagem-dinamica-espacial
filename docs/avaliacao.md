# Avaliação e projeto

A nota final combina exercícios práticos (30%), o projeto (50%) e o seminário (20%).

| Componente | Peso | O que se entrega |
| --- | --- | --- |
| Exercícios | 30% | Três notebooks com o "para casa" resolvido: Python (após o encontro 3), dinâmica de sistemas ou autômato celular (após o 6) e a grade do DisSCube (após o 10) |
| Projeto | 50% | Modelo aplicado à área de estudo do aluno, em repositório com instruções para rodar, e relatório de até 8 páginas no formato de artigo curto |
| Seminário | 20% | Apresentação de 15 min nos encontros 14 ou 15 |

## Projeto

Pode ser um modelo LUCC sobre um recorte do Maranhão ou da Amazônia, ou um modelo de autômato celular ou dinâmica de sistemas ligado à dissertação do aluno.

**Calendário.** Esboço no encontro 7 (entregue no 8); grade do DisSCube no 10; regressão do potencial no 11; conferência no 12; validação no 13; apresentação no 14 ou 15; relatório e repositório até duas semanas depois do 15.

**Relatório.** No formato de artigo curto, com a descrição do modelo organizada pelo protocolo ODD (*Overview, Design concepts, Details*; Grimm et al., 2020), que vale também para modelos que não são de agentes: propósito, entidades e variáveis, escalas, processos e ordem, conceitos, inicialização, dados de entrada e submodelos. O relatório pode virar resumo para o SBSR ou o GeoInfo.

### Rubrica do projeto

| Critério | Peso | Insuficiente | Adequado | Muito bom |
| --- | --- | --- | --- | --- |
| Pergunta e paradigma | 15% | pergunta vaga; paradigma sem justificativa | pergunta clara; paradigma justificado | pergunta que o modelo de fato responde, com as alternativas discutidas |
| Dados e grade | 15% | fontes sem versão ou sem hash | grade e fontes declaradas no TOML, com `run.json` | idem, com a escolha da resolução justificada |
| Modelo | 20% | parâmetros sem origem | potencial ajustado e tolerância justificada (não a do lab) | idem, com a descrição ODD completa |
| Validação | 20% | sem comparação com dado observado | quantidade e localização contra um mapa observado, com a persistência ao lado | idem, em várias resoluções e com um ano que não entrou no ajuste |
| Incerteza ou cenários | 15% | uma rodada só | varredura de um parâmetro, ou dois cenários comparados | mapa de concordância, ou cenários com a diferença explicada |
| Reprodutibilidade | 15% | o professor não consegue rodar | um comando no README repete a execução | idem, e o resultado confere com o registro (hash ou tolerância declarada) |

### Esboço (encontro 7, entregue no encontro 8)

Uma página com:

1. **Pergunta.** O que o modelo deve responder?
2. **Área e período.** Onde, quando, e com que tamanho de célula?
3. **Paradigma.** Dinâmica de sistemas, autômato celular, agentes ou acoplamento? Por quê?
4. **Estado e regra.** O que cada célula (ou agente) guarda e como muda?
5. **Dados.** Que mapas e séries você precisa (MapBiomas, PRODES, censo...)?
6. **Como saber se deu certo.** Que resultado observado você compararia com o simulado?

### Checklist de reprodutibilidade (do encontro 4)

- [ ] Parâmetros num arquivo de configuração, não no código.
- [ ] Semente registrada (e várias sementes, se o modelo for estocástico).
- [ ] Hash dos dados de entrada.
- [ ] Registro de cada execução que vai para o relatório.
- [ ] `requirements.lock` e versão do Python.
- [ ] Um comando, escrito no README, que repete a execução.
- [ ] Verificação declarada: hash do arquivo, hash dos valores ou tolerância.

## Seminário

| Critério | Peso |
| --- | --- |
| Pergunta, área e paradigma apresentados em até 3 min | 20% |
| Modelo e dados: o que cada componente faz e de onde vem cada número | 25% |
| Resultados com validação e incerteza (encontros 12 e 13), não só o mapa | 30% |
| Limitações: o que o modelo não representa, dito pelo próprio aluno | 15% |
| Tempo e respostas às perguntas | 10% |

**Formato.** 15 min de apresentação e 5 de perguntas, nos encontros 14 ou 15 (até 8 apresentações por encontro). A escala é definida no encontro 13. Envie os slides até a véspera.

**Estrutura sugerida**

| Parte | Tempo | Conteúdo |
| --- | --- | --- |
| Pergunta | 2 min | O que o modelo responde; área, período e resolução |
| Modelo | 4 min | Paradigma e componentes (demanda, potencial e alocação, ou estado e regra); de onde vem cada parâmetro |
| Dados | 2 min | Fontes, versões e a grade (mapa do `disscube plot`) |
| Resultados | 5 min | Mapa simulado e observado lado a lado; quantidade e localização contra a persistência; incerteza ou cenários |
| Limitações | 2 min | O que o modelo não representa; o que faria com mais tempo |

**Perguntas para se preparar.** As perguntas seguem os temas da disciplina:

- **Verificação:** o programa faz o que o modelo descreve? Algum componente foi comparado com uma referência?
- **Tolerância:** que tolerância da alocação foi usada, e por quê (encontros 9 e 11)?
- **Validação:** o modelo supera a persistência? Em que resolução (encontro 13)? O ano validado entrou no ajuste?
- **Incerteza:** o resultado mudaria com outro valor de parâmetro (encontro 12)?
- **Reprodutibilidade:** outra pessoa roda o projeto com um comando (encontro 4)?

O relatório é entregue duas semanas depois do encontro 15, para incorporar o que surgir nas perguntas.
