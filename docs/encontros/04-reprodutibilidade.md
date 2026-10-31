# Encontro 4 — Reprodutibilidade e o DisSModel

O aluno sai do encontro sabendo o que precisa guardar de uma execução para outra pessoa repeti-la, e tendo visto o DisSModel guardar isso sozinho. O fio da aula é uma surpresa real: o mesmo modelo, rodado duas vezes com a mesma semente, gera arquivos com hashes diferentes e valores idênticos.

**Notebook:** [encontro04_reprodutibilidade.ipynb](../notebooks/encontro04_reprodutibilidade.ipynb)

| Item | Conteúdo |
| --- | --- |
| Duração | 100 min: 10 de abertura, 25 de exposição, 50 de prática, 15 de fechamento |
| Pré-requisito | Encontros 2 e 3 (rodar células, ler uma tabela, abrir um arquivo vetorial) |
| Material | Notebook `encontro04_reprodutibilidade.ipynb` (41 células, roda em cerca de 30 s); slides da exposição |
| Modelo usado | `FireModel` do `dissmodel-ca` (o `Fire` do TerraME) numa grade de 30 × 30 células |
| Leitura de apoio | Livro *Geospatial Modeling with Python*, Cap. 22 (seção do executor) e Cap. 29 |

**Objetivos**

1. Distinguir reprodutibilidade, replicabilidade e generalização (NASEM, 2019).
2. Nomear o que quebra a repetição de um resultado: entrada sem comprovação, código sem versão, parâmetros esquecidos, sorteio sem semente, ambiente sem registro.
3. Usar um hash para comprovar um arquivo e saber o que ele não comprova.
4. Ler o registro (`.record.json`) de uma execução do DisSModel.
5. Escolher entre hash do arquivo, hash dos valores e tolerância.

## Antes da aula

- [ ] Instalar nas máquinas do laboratório: `pip install "dissmodel==0.6.6" "dissmodel-ca @ git+https://github.com/DisSModel/dissmodel-ca.git@v0.2.0"`, mais `jupyter` e `matplotlib`. No Colab, a primeira célula do notebook faz isso sozinha (cerca de 1 min); o selo **Abrir no Colab** fica no topo do notebook.
- [ ] Rodar o notebook inteiro numa máquina do laboratório e conferir que não há erro. Os identificadores e hashes mudam a cada execução; os números de células queimadas (575 e 443) não.
- [ ] Deixar o notebook **sem saídas** no repositório da turma, para o aluno ver o resultado aparecer.
- [ ] Preparar 6 a 8 slides para a exposição (seção seguinte).
- [ ] Levar um exemplo próprio de algo que não deu para repetir (um script antigo, uma pasta "versao_final_2"): funciona melhor que qualquer estatística.

## Roteiro

| Tempo (min) | Bloco | Atividade | Notebook |
| --- | --- | --- | --- |
| 0–10 | Abertura | Pergunta à turma: "quem já tentou rodar o script de outra pessoa, ou o seu de um ano atrás?" Ouvir dois ou três relatos e anotar no quadro o que deu errado | — |
| 10–35 | Exposição | Crise de reprodutibilidade; os três termos; o que quebra um resultado; como o DisSModel trata cada ponto | — |
| 35–45 | Prática | Hash de um arquivo; mudar uma célula entre 900 e ver o hash mudar inteiro | Parte 1 |
| 45–55 | Prática | O executor (`load`, `run`, `save`) e o `model.toml`; rodar duas vezes | Partes 2 e 3 |
| 55–65 | Prática | A surpresa: hashes diferentes. Investigar em turma: valores iguais, data do GeoPackage diferente; fixar a data e rodar de novo | Parte 4 |
| 65–75 | Prática | Trocar a semente; comparar os três mapas | Parte 5 |
| 75–85 | Prática | Ler o registro; ponto flutuante e tolerância; `pip freeze` | Partes 6, 7 e 8 |
| 85–100 | Fechamento | Voltar à lista do quadro e marcar o que o registro teria evitado; checklist do projeto; exercícios | Parte 9 |

Se o tempo apertar, a Parte 8 (`pip freeze`) pode ir para casa. A Parte 4 não deve ser cortada: é o momento em que a turma entende que hash comprova o arquivo, não o resultado.

## Exposição (25 min, cerca de 7 slides)

**1. O problema (5 min).** Num levantamento com 1.576 pesquisadores, mais de 70% já tinham tentado e falhado em reproduzir o experimento de outro, e mais da metade, o próprio (Baker, 2016). Em modelagem a causa raramente é má-fé: é o que não foi anotado no momento da execução.

**2. Três palavras (4 min).** Pelas definições da NASEM (2019):

- *reprodutível*: mesmos dados, mesmo código, mesmo resultado;
- *replicável*: outro estudo, com dados próprios, chega à mesma conclusão;
- *generalizável*: o resultado vale em outro contexto.

A disciplina trata da primeira. As outras duas dependem dela.

**3. O que quebra um resultado (6 min).** Cinco causas, cada uma com um exemplo da área:

| Causa | Exemplo |
| --- | --- |
| Entrada sem comprovação | o mapa de uso foi corrigido depois da rodada e o arquivo manteve o nome |
| Código sem versão | o script mudou entre a figura do artigo e a resposta ao revisor |
| Parâmetros esquecidos | coeficientes escritos dentro do código, alterados à mão a cada teste |
| Sorteio sem semente | o modelo dá um mapa diferente a cada rodada e não se sabe qual foi publicado |
| Ambiente sem registro | outra versão do GDAL ou do NumPy muda o último dígito, e um limiar muda a decisão |

**4. Como o DisSModel trata cada uma (10 min).** O ponto a passar: a ferramenta foi desenhada para registrar isso por padrão, não como etapa extra que o pesquisador lembra de fazer.

| Causa | Mecanismo no DisSModel | Onde aparece na prática |
| --- | --- | --- |
| Entrada | `load()` calcula o SHA-256 do arquivo lido e grava em `source.checksum` | Parte 1 e Parte 6 |
| Código | `code_version` (versão do dissmodel) e `model_commit` (pacote e versão do modelo) | Parte 6 |
| Parâmetros | ficam no `model.toml`; `--param` sobrescreve e o valor usado vai para o registro | Partes 2 e 5 |
| Sorteio | a semente é um parâmetro como outro qualquer | Parte 5 |
| Saída | `save()` grava o hash de cada arquivo em `artifacts` | Partes 3 e 4 |
| Organização | `load` e `save` fazem a leitura e a gravação; `run` só simula, o que permite trocar a fonte de dados sem mexer no modelo | Parte 2 |
| Ambiente | registro parcial: versão do dissmodel; o resto vem do `requirements.lock` | Parte 8 |

Fechar com a ponte: o DisSCube (encontro 10) faz o mesmo com a preparação dos dados, no `run.json`, e o DisSLUCC herda o executor do DisSModel.

## Prática (50 min)

O aluno não escreve código: roda as células, troca um número e responde quatro perguntas (✏️). O professor projeta o próprio notebook e para nos pontos marcados abaixo.

| Parte | O que acontece | O que o professor destaca |
| --- | --- | --- |
| 1. Hash | Cria `floresta.gpkg` (900 células); muda uma célula numa cópia; os hashes saem completamente diferentes | Um nome de arquivo não comprova nada; o hash comprova |
| 2. Executor | Grava `fogo.py` (`load`, `run`, `save`) e o `model.toml` com densidade inicial 0,005, 8 passos e semente 7 | Os parâmetros estão num arquivo de texto, não no código |
| 3. Duas rodadas | `python fogo.py run` duas vezes; cada uma ganha um identificador e um `.record.json` | Perguntar à turma, antes de rodar a célula seguinte: os hashes vão ser iguais? |
| 4. Investigação | Hashes de arquivo diferentes; hash dos valores igual; a tabela `gpkg_contents` mostra datas diferentes; com `OGR_CURRENT_DATE` fixa, os hashes ficam iguais | Hash do arquivo responde "é este arquivo?", não "é o mesmo resultado?" |
| 5. Semente | `--param seed=8`; o registro guarda 8; três mapas lado a lado: 575, 575 e 443 células queimadas | Modelo com sorteio é reprodutível se a semente for registrada; para concluir algo, várias sementes |
| 6. Registro | Lê os campos do `.record.json` e a tabela campo × pergunta | Ninguém digitou nada disso |
| 7. Tolerância | (0,1 + 0,2) + 0,3 ≠ 0,1 + (0,2 + 0,3) | Quando os valores podem diferir no último dígito, compara-se por tolerância declarada |
| 8. Ambiente | `pip freeze > requirements.lock` | O lock guarda até o commit do `dissmodel-ca`, instalado do GitHub |
| 9. Checklist | Sete itens para o projeto e três exercícios | Os itens viram critério do projeto final |

**Para casa**

1. Rodar com densidade 0,002, 0,005 e 0,01, mesma semente, e montar a tabela identificador × densidade × queimadas a partir dos registros.
2. Trocar `floresta.gpkg` e `model.toml` com um colega e rodar na própria máquina: os valores batem? E os hashes dos arquivos?
3. Em duas ou três frases: que informação da própria dissertação o aluno hoje não conseguiria recuperar daqui a um ano.

## Respostas esperadas

| Pergunta | Resposta esperada |
| --- | --- |
| 1. Como ter certeza de que o colega usou o mesmo arquivo? | Pedir o hash (SHA-256) do arquivo dele e comparar com o seu. Nome, tamanho e data não bastam |
| 2. Os hashes das duas rodadas são iguais? A diferença vem do sorteio? | Não são iguais, e não vem do sorteio: a semente é a mesma e os valores são idênticos. Muda só a data de gravação que o GeoPackage guarda dentro do arquivo |
| 3. Modelo com sorteio é reprodutível? | Sim, se a semente for registrada. Mas uma rodada é uma amostra: conclusões pedem várias sementes e a distribuição dos resultados |
| 4. Por que `model_commit` diz `local-cli`? | O executor é um arquivo solto, não um pacote instalado com versão. Num pacote (por exemplo, `disslucc==0.5.0`) o campo traz o nome e a versão, e o código fica identificado |

Alunos costumam perguntar se o hash "garante que o resultado está certo". Não garante: comprova que é o mesmo arquivo. Um modelo errado gera hashes perfeitamente repetíveis; verificar é assunto do encontro 9 (DisSLUCC contra o LuccME), e validar, do projeto (encontro 13).

## Achados ao testar

Testado em 31 out 2026 com Python 3.13, dissmodel 0.6.6, dissmodel-ca 0.2.0, geopandas 1.2.0, pyogrio 0.13.0 e numpy 2.5.4. O notebook roda sem erro em cerca de 30 s. Três pontos valem para o DisSModel, não só para a aula:

1. **O `output_sha256` de uma saída GeoPackage não se repete entre execuções idênticas.** O GDAL grava a hora em `gpkg_contents.last_change`. Com `OGR_CURRENT_DATE` fixa, os hashes coincidem. Para a aula é ótimo; para o DisSModel, vale considerar fixar essa data no `save_dataset` (ou registrar também o hash dos valores), senão a verificação de `output_sha256` do `/reproduce` falha para saídas vetoriais.
2. **`load_dataset` emite um aviso do pyogrio** ("GPKG application_id, but non conformant file extension") ao ler o GeoPackage por `/vsimem` sem extensão. Não muda o resultado; o notebook o esconde. Corrigir passando a extensão no caminho virtual.
3. **O CLI imprime "Validating, Loading, Running, Saving" de uma vez, antes de executar.** É cosmético, mas o aluno lê como se as etapas já tivessem acontecido.

Não usar em aula a história do PRODES do Cap. 29 (corredor da BR-163, 18,1% → 20,5%) antes de conferir os números: o registro de correções do DisSCube conta o caso no Acre, com outros valores.
