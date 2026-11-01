# Metodologia e ambiente

A maioria dos encontros tem de 20 a 35 min de exposição e de 45 a 65 min de prática guiada num notebook, que o aluno termina em casa. Três encontros têm formato próprio: o 8 (leitura dirigida de dois estudos de cenários), o 13 (demonstração de validação e oficina de projeto) e os seminários (14 e 15). A progressão segue a dos cursos de modelagem do INPE com o TerraME: modelos pequenos e didáticos primeiro, depois dados reais e LUCC.

- **Material-texto:** capítulos do livro *Geospatial Modeling with Python* (Volume I para Python e ferramentas, Volume II para o ecossistema DisSModel), as notas de aula dos encontros 1 e 8 e os notebooks da disciplina, neste repositório. A página [Encontros](encontros/index.md) indica a leitura de apoio de cada encontro.
- **Pacotes por papel:** `dissmodel-ca` e `dissmodel-sysdyn` como coleções de modelos prontos para estudar e modificar; `dissmodel-abm` como extensão de agentes, só apresentada; `disscube` para os dados; `disslucc` para o LUCC.
- **Referência:** o TerraME e o LuccME não são instalados nas máquinas. As saídas deles estão publicadas, com hash e DOI, nos repositórios `terrame-goldens` e `luccme-goldens`, gerados na imagem `terrame-docker`; os notebooks comparam com essas saídas. NetLogo e Dinamica EGO aparecem no encontro 1, sem prática além do NetLogo Web.
- **Dados:** casos pequenos que rodam em segundos (labs do LuccME, exemplos do TerraME, recortes do `disscube-benchmark`); os casos em escala de estado ou país aparecem como resultado já registrado, não executados em aula.

## Como os notebooks são escritos

Como o público não programa, os notebooks de modelagem vêm com o código pronto para ler, rodar e alterar parâmetros. As marcas nas células:

- 🔧 troque um número e rode de novo;
- ✏️ responda à pergunta.

Escrever código do zero fica para o projeto, com apoio.

## Ambiente

Python 3.11 ou mais recente. As versões ficam fixadas durante todo o semestre:

```bash
python -m venv .venv
source .venv/bin/activate          # no Windows: .venv\Scripts\activate
pip install -r requirements-notebooks.txt
jupyter lab
```

| Pacote | Versão | Origem | A partir do encontro |
| --- | --- | --- | --- |
| dissmodel | 0.6.6 | PyPI | 4 |
| dissmodel-ca | 0.2.0 | GitHub, tag `v0.2.0` | 4 |
| dissmodel-sysdyn | 0.2.0 | GitHub, tag `v0.2.0` | 5 |
| dissmodel-abm | 0.2.0 | GitHub, tag `v0.2.0` (ainda não está no PyPI) | 7 |
| disslucc | 0.5.0 | PyPI | 9 |
| disscube | 0.6.0 | PyPI | 10 |
| statsmodels | 0.15.0 | PyPI | 11 |

Os notebooks dos encontros 2 a 7 e 9 a 13 têm um selo **Abrir no Colab** no topo, que abre o notebook no Google Colab direto do GitHub; os dos encontros 3 a 7 e 9 a 13 instalam sozinhos o que falta no Colab (`rasterio`; DisSModel, `dissmodel-ca`, `dissmodel-sysdyn`, `dissmodel-abm`, `disslucc`, `disscube` e `statsmodels`).

## Dados e referências lidos pela internet

Os notebooks baixam os dados de versões fixas e conferem o hash de cada arquivo (encontro 4). Todos precisam de acesso a `raw.githubusercontent.com`:

| Encontros | O que é baixado | Versão |
| --- | --- | --- |
| 3 | focos de queimada e estados do IBGE (repositórios dos livros, por commit); MapBiomas da Ilha do Maranhão (Google Cloud Storage) | commits fixos; Coleção 11 |
| 5, 6, 7 | saídas de referência do TerraME | `terrame-goldens` v0.1.0 |
| 9, 11, 12, 13 | espaços celulares e saídas de referência do LuccME | `luccme-goldens` v1.1.0 |
| 10 | camadas do exemplo Amazônia do TerraME; arquivo TOML; espaço celular do TerraME | TerraME no commit 84faddc; `disscube-benchmark` v1.1.0; `luccme-goldens` v1.1.0 |

O "para casa" do encontro 10 lê o MapBiomas pelo Google Cloud Storage, como a Parte 4 do encontro 3. Se a leitura falhar na sua rede, use o cubo Amazônia do encontro 10 ou um caso pronto do [`disscube-grids`](https://github.com/LambdaGeo/disscube-grids) (BR-163 ou Ilha do Maranhão).
