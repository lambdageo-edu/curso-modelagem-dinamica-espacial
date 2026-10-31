# Metodologia e ambiente

Cada encontro tem cerca de 30 min de exposição e 70 min de prática guiada num notebook que o aluno termina em casa. A progressão segue a dos cursos de modelagem do INPE com TerraME: modelos pequenos e didáticos primeiro, depois dados reais e LUCC.

- **Material-texto:** capítulos do livro *Geospatial Modeling with Python* (Volume II) e os notebooks da disciplina, neste repositório.
- **Pacotes por papel:** `dissmodel-ca` e `dissmodel-sysdyn` como coleções de modelos prontos para estudar e modificar; `dissmodel-abm` como extensão de agentes, só apresentada; `disscube` para os dados; `disslucc` para o LUCC.
- **Ferramentas de comparação:** TerraME/LuccME pela imagem `terrame-docker` (demonstração do professor); NetLogo e Dinamica EGO apenas mostrados, sem prática.
- **Dados:** casos pequenos que rodam em segundos ou poucos minutos (Ilha do Maranhão, recortes do `disscube-benchmark`, labs do LuccME); os casos em escala de estado ou país aparecem como resultado já registrado, não executados em aula.

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

| Pacote | Versão | Origem |
| --- | --- | --- |
| dissmodel | 0.6.6 | PyPI |
| dissmodel-ca | 0.2.0 | GitHub, tag `v0.2.0` |
| dissmodel-sysdyn | 0.2.0 | GitHub, tag `v0.2.0` |
| dissmodel-abm | 0.2.0 | GitHub, tag `v0.2.0` (ainda não está no PyPI) |
| disscube | 0.6.0 | PyPI (a partir do encontro 10) |
| disslucc | 0.5.0 | PyPI (a partir do encontro 9) |

Os notebooks dos encontros 2 e 3 têm um selo **Abrir no Colab** no topo, que abre o notebook no Google Colab direto do GitHub; o do encontro 3 instala sozinho o que falta no Colab (`rasterio`). Nos demais encontros, por enquanto, a primeira célula tem o `pip install` comentado: no Colab, basta descomentar e rodar.

Os encontros 5, 6 e 7 leem as saídas de referência do TerraME direto do repositório [`terrame-goldens`](https://github.com/LambdaGeo/terrame-goldens) (versão 0.1.0), e por isso precisam de acesso a `raw.githubusercontent.com`.
