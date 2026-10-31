# Encontro 2 — Python I: notebook, variáveis, listas, laços e funções

O aluno sai do encontro sabendo rodar e editar um notebook, guardar valores em variáveis e listas, repetir uma conta com um laço e dar nome a ela com uma função, e ler as quatro mensagens de erro mais comuns. O fio da aula é um modelo de crescimento populacional, escrito em partes e terminado como modelo logístico: o primeiro modelo dinâmico da disciplina, antes de ter esse nome.

**Notebook:** [encontro02_python_basico.ipynb](../notebooks/encontro02_python_basico.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 10 de abertura, 15 de exposição, 65 de prática, 10 de fechamento |
| Pré-requisito | Nenhum. Saber abrir um navegador e entrar no Colab ou no Jupyter do laboratório |
| Material | Notebook `encontro02_python_basico.ipynb` (48 células, roda em cerca de 2 s); folha de consulta com os erros comuns |
| Bibliotecas | Só Python e `matplotlib` |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, Caps. 1 e 2 |

**Objetivos**

1. Rodar células, distinguir células de texto e de código, e entender que a ordem de execução importa.
2. Guardar valores em variáveis e reconhecer os tipos `int`, `float`, `str` e `bool`.
3. Criar listas, acessar elementos pelo índice (a partir de 0) e usar `len`, `sum`, `max` e `append`.
4. Repetir uma conta com `for` e `while`, e decidir com `if`.
5. Escrever e chamar uma função com parâmetros e `return`.
6. Fazer um gráfico de linhas com `matplotlib`.
7. Ler uma mensagem de erro e corrigir a causa.

## Antes da aula

- [ ] Decidir o ambiente: Jupyter no laboratório ou Colab (só precisa de conta Google). O notebook não instala nada além do que o Colab já tem. O selo **Abrir no Colab**, no topo do notebook, abre direto do GitHub; lembrar a turma de salvar uma cópia no Drive antes de mexer.
- [ ] Rodar o notebook uma vez no ambiente escolhido. As quatro células da Parte 8 dão erro **de propósito**; as demais não podem dar.
- [ ] Imprimir ou projetar a tabela de erros da Parte 8 como folha de consulta, para os próximos encontros.
- [ ] Combinar com a turma como pedir ajuda: primeiro ler a última linha do erro, depois perguntar ao colega, depois ao professor.

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–10 | Abertura | Por que programar para modelar: um modelo é uma regra repetida no tempo, e a regra cabe em poucas linhas. Todos abrem o notebook e rodam a primeira célula | Parte 1 |
| 10–25 | Exposição | O que é Python; notebook × script; a ordem de execução; como ler um erro | — |
| 25–40 | Prática | Calculadora, variáveis, tipos, f-strings; pergunta 1 (densidade) | Partes 2 e 3 |
| 40–50 | Prática | Listas e índices; pergunta 2 | Parte 4 |
| 50–65 | Prática | `for` que simula o tempo; `while` e `if`: em quantos anos a população dobra | Parte 5 |
| 65–72 | Prática | A primeira função: `crescimento(inicial, taxa, anos)` | Parte 6 |
| 72–82 | Prática | Gráficos; crescimento logístico; pergunta 3 | Parte 7 |
| 82–90 | Prática | Os quatro erros; pergunta 4 (corrigir) | Parte 8 |
| 90–100 | Fechamento | O esqueleto de todo modelo dinâmico: estado, regra, laço. Exercícios | Para casa |

Se o tempo apertar, a Parte 7 pode terminar em casa. A Parte 5 não deve ser cortada: o laço que avança o tempo é a estrutura de todos os modelos da disciplina.

## Exposição (15 min, cerca de 4 slides)

**1. Python e o notebook (5 min).** Python é a linguagem que a maioria das bibliotecas de dados geoespaciais usa (GeoPandas, rasterio, xarray) e a do DisSModel. O notebook mistura texto, código e resultado num só documento; um script é só o código, e roda do começo ao fim. A disciplina usa notebooks para aprender e scripts quando o resultado precisa ser repetido (encontro 4).

**2. A ordem de execução (5 min).** O notebook guarda o estado de tudo que já rodou, na ordem em que rodou, não na ordem da página. Mostrar ao vivo: rodar duas vezes a célula que atualiza `populacao` e ver o valor mudar. Quando algo parecer estranho, reiniciar e rodar tudo de cima para baixo.

**3. Como ler um erro (5 min).** A última linha diz o tipo (`NameError`, `TypeError`...) e o motivo; as linhas acima mostram onde. Mostrar um `NameError` e localizar a linha. Assistentes de IA explicam bem uma mensagem de erro, mas o aluno precisa entender a correção antes de aceitá-la: a disciplina vai pedir que o código do projeto seja explicado no seminário.

## Prática (65 min)

O aluno roda as células em ordem e escreve código em quatro pontos (as perguntas ✏️ e os 🔧). O professor projeta o notebook e para nos pontos abaixo.

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 1. Notebook | Primeira célula; a última linha aparece sem `print` | Shift + Enter; o número entre colchetes é a ordem |
| 2. Calculadora | 1.000 × 1,015 dá `1014.9999999999999` | Não é erro: decimais em binário. Volta no encontro 4 |
| 3. Variáveis | `populacao`, `taxa`; rodar duas vezes a atualização; tipos; f-strings | `=` guarda, não compara; a ordem de execução importa |
| 4. Listas | Anos e áreas desmatadas de exemplo; índices, `sum`, `max`, `append` | A contagem começa em 0; `[-1]` é o último |
| 5. Laços | Dez anos de crescimento a 1,5%: 1.160.541 habitantes; dobra em 47 anos | Estado, regra, laço: o esqueleto de todo modelo dinâmico |
| 6. Funções | `crescimento(1_000_000, 0.015, 30)`: 1.563.080 | Uma função dá nome a um procedimento e evita copiar código |
| 7. Gráficos | Três taxas; taxa constante × logístico com capacidade de 3 milhões | O logístico é um estoque que se aproxima de um limite: volta no encontro 5 |
| 8. Erros | `NameError`, `TypeError`, `IndexError`, `IndentationError` | Ler a última linha primeiro |

**Para casa**

1. Função `anos_para_dobrar(taxa)`, testada com 1%, 2% e 5%, comparada com a "regra do 70".
2. Floresta de 800 km² perdendo 3% ao ano: em que ano fica abaixo de 400 km²? Com gráfico.
3. Modelo logístico com capacidades de 2, 3 e 5 milhões: o que a capacidade muda na curva?

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Densidade de São Luís | `densidade = populacao / area_km2`, em habitantes por km². Com `populacao` igual a 1.015.000 (depois de rodar a atualização uma vez) e 583,063 km², cerca de 1.741 hab/km². O valor depende de quantas vezes a célula de atualização rodou: bom momento para lembrar a ordem de execução |
| 2. Área desmatada em 2022 | `area_desmatada[2]`: 2022 é o terceiro ano da lista, e o índice começa em 0. `area_desmatada[2022]` pede o elemento de posição 2022, que não existe (`IndexError`) |
| 3. Logístico começando acima da capacidade | A população **diminui** até a capacidade: com p maior que a capacidade, o termo (1 − p/capacidade) fica negativo e o "crescimento" vira perda |
| 4. Corrigir os erros | `print(populacao)` (sem cedilha); `ano = 2024` ou `int(ano) + 1`; `area_desmatada[5]` ou `[-1]`; recuar o `print` dentro do `for` |

**Para casa, com os números do teste**

1. Dobra em 70 anos a 1%, 36 a 2% e 15 a 5%. A regra do 70 dá 70, 35 e 14: funciona bem para taxas pequenas e erra por pouco nas maiores.
2. A floresta fica abaixo de 400 km² no 23º ano.
3. A capacidade muda a altura do patamar e o tempo para chegar a ele; a forma em S é a mesma.

## Achados ao testar

Testado em 31 out 2026 com Python 3.13 e matplotlib. O notebook roda em cerca de 2 s. As quatro células de erro da Parte 8 têm a marca `raises-exception`, que deixa a execução automática seguir (o script `scripts/executar_notebooks.py` as aceita); no Jupyter ou no Colab a marca não muda nada.

O separador de milhar das f-strings (`{valor:,.0f}`) segue o padrão inglês (1,015,000). O notebook avisa num comentário; trocar por ponto exigiria configurar o *locale*, o que não vale a complicação nesta aula.
