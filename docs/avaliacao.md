# Avaliação e projeto

A nota final combina exercícios práticos (30%), o projeto (50%) e o seminário (20%).

| Componente | Peso | O que se entrega |
| --- | --- | --- |
| Exercícios | 30% | Três notebooks: Python (após o enc. 3), dinâmica de sistemas e autômato celular (após o enc. 6), grade do DisSCube (após o enc. 10) |
| Projeto | 50% | Modelo aplicado à área de estudo do aluno, em repositório com instruções para rodar, e relatório de até 8 páginas no formato de artigo curto |
| Seminário | 20% | Apresentação de 15 min nos encontros 14 ou 15 |

## Projeto

Pode ser um modelo LUCC sobre um recorte do Maranhão ou da Amazônia, ou um modelo de autômato celular ou dinâmica de sistemas ligado à dissertação do aluno.

**Critérios:** pergunta clara; escolha do paradigma justificada; dados e grade descritos; resultados com análise de sensibilidade ou de cenários; limitações; e repetibilidade, isto é, outra pessoa consegue rodar a partir do repositório e obter o mesmo resultado.

O relatório no formato de artigo pode virar resumo para o SBSR ou o GeoInfo.

### Esboço (entregue no encontro 8)

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
