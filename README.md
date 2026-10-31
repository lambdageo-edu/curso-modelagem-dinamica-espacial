# Modelagem Dinâmica Espacial

Material da disciplina de pós-graduação **Modelagem Dinâmica Espacial: de autômatos celulares a modelos de mudança de uso da terra** (PPGC&TAmb/UFMA, LambdaGeo). Proposta, cronograma, roteiros dos encontros e notebooks, publicados como site MkDocs.

Estado: proposta em elaboração. Roteiros e notebooks prontos e testados para os encontros 4 a 7; os demais estão só no cronograma.

## Conteúdo

```
docs/
  index.md                 proposta: identificação, ementa, objetivos
  cronograma.md            os 15 encontros
  metodologia.md           formato das aulas e ambiente (versões fixadas)
  avaliacao.md             pesos, projeto, esboço e checklist de reprodutibilidade
  bibliografia.md
  preparacao.md            riscos e o que preparar
  encontros/               um roteiro por encontro (para o professor)
  notebooks/               os notebooks dos encontros, já executados
scripts/
  build_encontroNN.py      gera o notebook de cada encontro
  executar_notebooks.py    gera, executa e grava em docs/notebooks/
```

Os roteiros trazem as respostas esperadas das perguntas dos notebooks.

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

Os notebooks dos encontros 5, 6 e 7 leem saídas de referência do TerraME do repositório [`terrame-goldens`](https://github.com/LambdaGeo/terrame-goldens) v0.1.0 e precisam de acesso a `raw.githubusercontent.com`.

Testado em 31 out 2026 com Python 3.13, dissmodel 0.6.6 e dissmodel-ca, dissmodel-sysdyn e dissmodel-abm 0.2.0.

## Publicação

O workflow `.github/workflows/site.yml` roda `mkdocs build --strict` em todo pull request e, a cada push na `main`, publica o site na branch `gh-pages` (ativar o GitHub Pages a partir dessa branch nas configurações do repositório).
