# Modelagem Dinâmica Espacial

Material da disciplina de pós-graduação **Modelagem Dinâmica Espacial: de autômatos celulares a modelos de mudança de uso da terra** (proposta, LambdaGeo/UFMA). Proposta, cronograma, notas de aula e notebooks, publicados como site MkDocs.

Estado: proposta em elaboração. Notebooks testados nos encontros 2 a 7 e 9 a 13; notas de aula nos encontros 1 e 8, com ficha de leitura no 8. O encontro 1 (NetLogo Web) ainda não foi testado em sala.

## Conteúdo

```
docs/
  index.md                 proposta: identificação, ementa, objetivos
  cronograma.md            os 15 encontros
  metodologia.md           formato das aulas e ambiente (versões fixadas)
  avaliacao.md             pesos, projeto, esboço e checklist de reprodutibilidade
  bibliografia.md
  encontros/               índice dos encontros, notas de aula (1 e 8) e ficha de leitura (8)
  notebooks/               os notebooks dos encontros, já executados
scripts/
  build_encontroNN.py      gera o notebook de cada encontro
  executar_notebooks.py    gera, executa e grava em docs/notebooks/
```

O site traz só o material do aluno. Os roteiros dos encontros, as respostas esperadas e a preparação da oferta ficam num documento à parte, do professor.

## Ver o site localmente

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make serve            # http://127.0.0.1:8000
make build            # mkdocs build --strict
```

O site não executa os notebooks: mostra as saídas gravadas.

## Rodar ou regenerar os notebooks

```bash
pip install -r requirements-notebooks.txt
jupyter lab docs/notebooks/           # para rodar em aula
make notebooks                        # regenera a partir de scripts/ e reexecuta
```

Os notebooks dos encontros 5, 6 e 7 leem saídas de referência do TerraME do repositório [`terrame-goldens`](https://github.com/LambdaGeo/terrame-goldens) v0.1.0 e precisam de acesso a `raw.githubusercontent.com`. O do encontro 9 baixa os dados e as saídas do LuccME do [`luccme-goldens`](https://github.com/LambdaGeo/luccme-goldens) v1.1.0; o do encontro 10, as camadas do exemplo Amazônia do TerraME e o TOML do [`disscube-benchmark`](https://github.com/LambdaGeo/disscube-benchmark) v1.1.0.

Testado em 31 out 2026 com Python 3.13, dissmodel 0.6.6 e dissmodel-ca, dissmodel-sysdyn e dissmodel-abm 0.2.0, disslucc 0.5.0, disscube 0.6.0 e statsmodels 0.15.0.

## Publicação

O workflow `.github/workflows/site.yml` roda `mkdocs build --strict` em todo pull request e, a cada push na `main`, publica o site na branch `gh-pages` (ativar o GitHub Pages a partir dessa branch nas configurações do repositório).
