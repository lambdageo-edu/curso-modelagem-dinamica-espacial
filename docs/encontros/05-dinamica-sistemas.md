# Encontro 5 — Dinâmica de sistemas

O aluno sai do encontro lendo e alterando modelos de estoque e fluxo, encontrando o equilíbrio pela conta e pela simulação, e tendo visto o DisSModel dar o mesmo número que o TerraME. É o primeiro encontro em que o aluno escreve um modelo (oito linhas, de floresta e desmatamento); ainda não há espaço, que entra no encontro 6.

**Notebook:** [encontro05_dinamica_sistemas.ipynb](../notebooks/encontro05_dinamica_sistemas.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 5 de abertura, 25 de exposição, 55 de prática, 15 de fechamento |
| Material | Notebook `encontro05_dinamica_sistemas.ipynb` (32 células, roda em cerca de 6 s) |
| Modelos | `Tub`, `SIR` e `PredatorPrey` do `dissmodel-sysdyn` v0.2.0; `Floresta`, escrito no notebook |
| Referência | Saídas do TerraME no `terrame-goldens` v0.1.0, lidas direto do GitHub |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, Cap. 23; Ford (2010), caps. 1–4 |

**Objetivos**

1. Identificar estoques, fluxos e parâmetros num modelo.
2. Reconhecer retroalimentação de reforço e de equilíbrio.
3. Calcular o equilíbrio de um modelo simples e confirmá-lo simulando.
4. Distinguir equilíbrio estável (floresta) de oscilação em torno do equilíbrio (predador-presa).
5. Comparar uma simulação com uma implementação de referência.

## Antes da aula

- [ ] Instalar `dissmodel-sysdyn` pela tag: `pip install "dissmodel-sysdyn @ git+https://github.com/DisSModel/dissmodel-sysdyn.git@v0.2.0"`. O resto já veio do encontro 4.
- [ ] Conferir que o laboratório acessa `raw.githubusercontent.com` (Parte 5). Sem rede, copiar `sir.csv.gz`, `tub.csv.gz` e `predator_prey.csv.gz` do `terrame-goldens` v0.1.0 para a pasta da turma e trocar a `URL` por um caminho local.
- [ ] Rodar o notebook do professor uma vez. Os números da Parte 3 (picos de 3.558, 1.733 e 677 pessoas) e da Parte 5 (diferença zero) não mudam.
- [ ] Desenhar no quadro, antes da aula, o diagrama de estoque e fluxo da banheira (uma caixa, uma torneira, um ralo): é a imagem que a aula inteira reaproveita.
- [ ] Opcional: rodar o `Tub` no TerraME pela imagem `terrame-docker` para projetar o mesmo modelo em Lua ao lado do Python (5 min da exposição).

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–5 | Abertura | Retomar o encontro 4 em uma frase: "hoje os modelos são pequenos, mas cada número deles vai bater com o do TerraME" | — |
| 5–30 | Exposição | Estoque e fluxo; retroalimentação; equilíbrio; o relógio do DisSModel; `Model` com `setup` e `execute` | — |
| 30–40 | Prática | Banheira: ler a tabela, o gráfico e o relógio; mudar a entrada | Parte 1 |
| 40–55 | Prática | Escrever o modelo `Floresta`; calcular o equilíbrio (250 km²) antes de rodar; dois começos, um equilíbrio | Parte 2 |
| 55–70 | Prática | SIR: as duas retroalimentações; distanciamento com 6, 4 e 3 contatos | Parte 3 |
| 70–80 | Prática | Predador-presa: oscilação, gráfico de fase, começar no equilíbrio | Parte 4 |
| 80–85 | Prática | Comparar com o TerraME: diferença zero no SIR, banheira e predador-presa | Parte 5 |
| 85–100 | Fechamento | Pergunta 5 em turma ("igual ao TerraME prova que está certo?"); diagrama de estoque e fluxo para casa | Para casa |

Se o tempo apertar, a Parte 4 pode ser só demonstrada pelo professor. A Parte 2 não deve ser cortada: é o primeiro modelo escrito pelo aluno e a base do equilíbrio que volta no encontro 8 (demanda de um modelo LUCC).

## Exposição (25 min, cerca de 6 slides)

**1. Estoque e fluxo (7 min).** Estoque é o que se acumula e pode ser medido num instante (água, floresta, carbono, pessoas); fluxo é o que muda o estoque por unidade de tempo. Toda a disciplina usa a mesma regra de atualização:

$$
E_{t+1} = E_t + \text{entradas}_t - \text{saídas}_t
$$

Exemplos da área: floresta (saída: desmatamento; entrada: regeneração), estoque de carbono, área urbana. Lembrar que DisSModel e TerraME usam tempo discreto (um passo por vez); Vensim, Stella e PySD tratam o tempo como contínuo e integram com passo pequeno.

**2. Retroalimentação (7 min).** Quando um fluxo depende do próprio estoque, há um laço:

| Tipo | Efeito | Exemplo |
| --- | --- | --- |
| Reforço | o estoque alimenta o próprio crescimento | contágio: mais infectados, mais contatos infecciosos |
| Equilíbrio | o estoque freia a própria mudança | regeneração; fim dos suscetíveis numa epidemia |

Um laço de equilíbrio com atraso produz oscilação (predador-presa). Desenhar o diagrama causal do SIR com os sinais + e −.

**3. Equilíbrio (5 min).** O ponto em que entradas e saídas se igualam. Insistir no hábito de calcular antes de rodar: se a simulação não chega ao número da conta, ou a conta ou o modelo está errado. Distinguir equilíbrio estável (volta a ele depois de uma perturbação) de neutro (oscila em torno dele, como no predador-presa discreto).

**4. O relógio e o modelo no DisSModel (6 min).**

| Conceito | DisSModel | TerraME |
| --- | --- | --- |
| Relógio | `Environment(start_time=1, end_time=20)`; o último passo é executado | `Timer` com `Event`; `timer:run(20)` |
| Modelo | classe que herda de `Model` | `Model{...}` |
| Valores iniciais e parâmetros | `setup(self, ...)`, roda uma vez | atributos do `Model` e `init` |
| Regra de cada passo | `execute(self)` | `action` do `Event` |

Vários modelos podem compartilhar o mesmo `Environment` e rodam na ordem em que foram criados; é assim que o notebook anota os valores a cada passo, e é a base do acoplamento do encontro 7.

## Prática (55 min)

O notebook traz uma função `simular(Modelo, passos, variaveis, **parâmetros)` que roda o modelo e devolve uma tabela com um passo por linha. O aluno só a usa; o professor mostra em um minuto que ela é um segundo `Model` que anota os valores depois de cada passo.

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 1. Banheira | 40 litros, saem 5 por passo: zera no passo 8. Com 20 litros a cada 10 passos, volta a zerar | O passo 0 é o estado inicial; o `end_time` é executado |
| 2. Floresta | O aluno lê (e depois altera) um modelo de 8 linhas: desmatamento de 2% ao ano, 5 km² de regeneração. A floresta tende a 250 km², vindo de 1.000 ou de 100 | Calcular o equilíbrio antes de rodar; depois conferir na simulação |
| 3. SIR | Pico de 3.558 infectados no dia 13 com 6 contatos; 1.733 no dia 20 com 4; 677 no dia 32 com 3. Os que nunca se infectam passam de 249 para 4.005 | O distanciamento não só achata o pico: muda o tamanho final da epidemia |
| 4. Predador-presa | Ciclos de cerca de 170 passos; no gráfico de fase, uma curva fechada. Começando em (1000, 80), nada muda; em (1000, 70), um ciclo pequeno | Equilíbrio sem retorno: perturbação não se desfaz |
| 5. TerraME | Lê a saída do TerraME do `terrame-goldens` e compara: diferença zero nos três modelos | Igualdade bit a bit só veio depois de seguir a ordem das contas do TerraME |

**Para casa**

1. Acrescentar ao `Floresta` uma saída fixa de 3 km² por ano (estradas). Novo equilíbrio: (5 − 3) / 0,02 = 100 km². Escrever a conta antes de rodar.
2. No SIR, `duration` de 2 para 4 dias com 6 contatos: o que muda no pico, e por quê.
3. Desenhar à mão o diagrama de estoque e fluxo de um processo da própria pesquisa. Os diagramas abrem o encontro 6.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Que `in_flow` repete o ciclo a cada 10 passos? | 50 litros: é o que sai em 10 passos (5 × 10). O nível passa a ir de 50 a 5 e voltar. Entrada igual à saída no período é um equilíbrio de ciclo |
| 2. Taxa de 2% para 1%: novo equilíbrio e tempo | 5 / 0,01 = 500 km². Partindo de 1.000 km², chega a 5% do equilíbrio em cerca de 300 anos (com 2%, cerca de 200). Taxa menor, equilíbrio maior e mais lento |
| 3. O que o distanciamento muda além do pico? | O total de infectados: os que nunca se infectam passam de 249 (6 contatos) para 4.005 (3 contatos). Com menos contágio, a epidemia perde força antes de esgotar os suscetíveis; é o laço de equilíbrio agindo mais cedo |
| 4. Começar fora do equilíbrio, no predador-presa | As populações não voltam ao equilíbrio: ficam num ciclo cujo tamanho depende do ponto de partida. Uma previsão depende do estado inicial, que nunca se conhece com precisão |
| 5. Igual ao TerraME prova que o SIR está certo? | Não. Prova que as duas implementações fazem as mesmas contas (verificação). Se o modelo representa uma epidemia real é outra pergunta (validação), que pede dados observados. Assunto do encontro 13 |

Para casa, exercício 2: com `duration=4` o pico sobe para 6.233 infectados e vem antes (dia 11), e ninguém escapa. A doença fica mais tempo transmitindo, o que reforça o laço de contágio.

## Achados ao testar

Testado em 31 out 2026 com Python 3.13, dissmodel 0.6.6, dissmodel-sysdyn 0.2.0 e terrame-goldens 0.1.0. O notebook roda sem erro em cerca de 6 s, e os três modelos comparados dão diferença zero com o TerraME. Três pontos valem para os pacotes:

1. **O notebook de exemplo `examples/notebooks/sysdyn_tub.ipynb` do `dissmodel-sysdyn` v0.2.0 ainda redefine o `Tub` com `self._step`**, o erro corrigido no pacote (o intervalo do agendamento cresce: passos 1, 2, 4, 7, 11…). Quem copiar o exemplo herda o erro. Trocar por `_tick` ou importar a classe do pacote.
2. **Os dados do `@track_plot` ficam na classe, não na instância.** Dois `Tub` no mesmo `Environment` gravam na mesma série: o `Chart` mostra 35, 95, 30, 90… intercalados. Por isso o notebook não usa o `Chart` e anota os valores com um `Model` próprio. Vale corrigir no `dissmodel` antes do encontro 7 (acoplamento), onde é natural ter duas instâncias.
3. **`env.run()` sempre imprime "Running from … to …".** Numa varredura de parâmetros isso enche a saída; o notebook redireciona. Um parâmetro `verbose=False` resolveria.
