"""Gera o notebook do encontro 4 (reprodutibilidade e DisSModel).

Usa os comandos `dissmodel verify`, `reproduce` e `compare` (DisSModel 0.7).
"""
import sys
import nbformat as nbf
from colab import selo

md = nbf.v4.new_markdown_cell
code = nbf.v4.new_code_cell
cells = []

cells.append(md("""# Encontro 4 — Reprodutibilidade e o DisSModel

**Modelagem Dinâmica Espacial · LambdaGeo/UFMA**

""" + selo("encontro04_reprodutibilidade") + """

Neste notebook você **não precisa escrever código**: rode as células na ordem (Shift+Enter), leia as saídas e responda às perguntas marcadas com ✏️. Em alguns lugares você vai trocar um número e rodar de novo.

A ideia é simples. Uma execução do modelo deixa um **registro**. Com o registro, três comandos respondem a três perguntas:

| Pergunta | Comando |
|---|---|
| Este arquivo é o que o registro diz que a execução gerou? | `dissmodel verify` |
| Se eu rodar de novo, sai o mesmo resultado? | `dissmodel reproduce` |
| Estes dois resultados são o mesmo? | `dissmodel compare` |

Ao final, você deve saber responder:

1. O que significa dizer que um resultado é *reprodutível*?
2. Quais informações de uma execução precisam ser guardadas para outra pessoa repeti-la?
3. Por que dois arquivos com o mesmo conteúdo podem ter "impressões digitais" diferentes?
4. Como o DisSModel registra essas informações sem que você precise lembrar delas, e como outra pessoa as usa?
5. Por que os critérios de aceitação se escrevem **antes** de rodar?

As [notas de aula](https://lambdageo-edu.github.io/curso-modelagem-dinamica-espacial/encontros/04-notas/) deste encontro reúnem o método de conferência usado em toda a disciplina."""))

cells.append(md("""## 0. Preparação

No Colab, a célula abaixo instala o DisSModel e o pacote de autômatos celulares (cerca de 1 minuto). No laboratório o ambiente já está instalado e ela não instala nada."""))

cells.append(code("""import sys
if "google.colab" in sys.modules:
    %pip install -q "dissmodel==0.7.0" "dissmodel-ca @ git+https://github.com/DisSModel/dissmodel-ca.git@v0.2.0" rasterio

import hashlib, json, glob, os
import numpy as np
import rasterio
import dissmodel, dissmodel_ca

print("dissmodel", dissmodel.__version__)"""))

cells.append(md("""## 1. Impressão digital de um arquivo (hash)

Um *hash* (aqui, SHA-256) é um código calculado a partir de **todos os bytes** de um arquivo. Arquivos iguais têm o mesmo hash; se um único byte muda, o hash muda por completo.

Vamos criar uma "floresta" de 50 × 50 células, toda de árvores (estado 0), e calcular o hash do arquivo. O arquivo é um **GeoTIFF**, o formato de raster que o DisSModel usa."""))

cells.append(code("""from dissmodel.geo import raster_grid
from dissmodel.io import load_dataset, save_dataset

floresta = raster_grid(rows=50, cols=50, attrs={"state": 0})     # 0 = floresta
save_dataset(floresta, "floresta.tif")

_, hash_antes = load_dataset("floresta.tif")
print("hash da floresta:", hash_antes[:16], "...")"""))

cells.append(md("""Agora mudamos **uma única célula** de uma cópia e comparamos."""))

cells.append(code("""(copia, _), _ = load_dataset("floresta.tif")
estado = copia.get("state").copy()
estado[0, 0] = 1                       # uma célula entre 2500
copia.set("state", estado)
save_dataset(copia, "floresta_copia.tif")

_, hash_copia = load_dataset("floresta_copia.tif")
print("original:", hash_antes[:16], "...")
print("cópia   :", hash_copia[:16], "...")
print("mesmo arquivo?", hash_antes == hash_copia)"""))

cells.append(md("""✏️ **Pergunta 1.** Se um colega diz "usei o mesmo arquivo `floresta.tif` que você", o que você pediria para ter certeza?"""))

cells.append(md("""## 2. Um modelo de incêndio, escrito como *executor*

No DisSModel, um modelo que vai gerar resultado para um trabalho é escrito como um **executor**: uma classe com três passos separados.

| Passo | O que faz | O que registra |
|---|---|---|
| `load` | lê os dados de entrada | o hash da entrada |
| `run` | roda a simulação (sem ler nem gravar arquivos) | as métricas |
| `save` | grava o resultado | o hash da saída |

O modelo é o `FireModelRaster` do pacote `dissmodel-ca` (o mesmo `Fire` do TerraME): cada célula é floresta ou vazia, o fogo começa em algumas células sorteadas e se espalha para a floresta vizinha. A célula que queimou não queima de novo. Como há sorteio, o modelo recebe uma **semente** (`seed`): com a mesma semente, o sorteio é o mesmo."""))

cells.append(code("""%%writefile fogo.py
from dissmodel.executor import ModelExecutor
from dissmodel.io import load_dataset, save_dataset


class FogoExecutor(ModelExecutor):
    name = "fogo"

    def load(self, record):
        (dados, _meta), checksum = load_dataset(record.source.uri)
        record.source.checksum = checksum          # hash da entrada
        return dados

    def run(self, dados, record):
        from dissmodel.core import Environment
        from dissmodel_ca.models import FireModelRaster, FireState
        p = record.parameters                       # vêm do model.toml
        env = Environment(start_time=0, end_time=p["end_time"])
        modelo = FireModelRaster(backend=dados,
                                 initial_fire_density=p["initial_fire_density"],
                                 seed=p["seed"])
        modelo.initialize()
        env.run()
        record.metrics["celulas_queimadas"] = int((dados.get("state") == FireState.BURNED).sum())
        return dados

    def save(self, resultado, record):
        record.output_sha256 = save_dataset(resultado, record.output_path)   # hash da saída
        record.status = "completed"
        return record


if __name__ == "__main__":
    from dissmodel.executor.cli import run_cli
    run_cli(FogoExecutor)"""))

cells.append(md("""Os **parâmetros não ficam no código**. Ficam num arquivo de configuração, `model.toml`, que você pode abrir e editar como texto."""))

cells.append(code("""%%writefile model.toml
[model]
name = "fogo"

[model.parameters]
initial_fire_density = 0.005  # fração de células que começam queimando
end_time = 8                  # número de passos
seed = 7                      # semente do sorteio inicial"""))

cells.append(md("""**Antes de rodar, os critérios.** Escrevemos agora, antes de ver qualquer resultado, o que uma rodada precisa cumprir para ser aceita. No projeto, este arquivo entra no git **antes** da rodada final, e o commit prova quando foi escrito (as [notas de aula](https://lambdageo-edu.github.io/curso-modelagem-dinamica-espacial/encontros/04-notas/) explicam por quê)."""))

cells.append(code("""%%writefile aceitacao.toml
# Critérios escritos ANTES de rodar o modelo.

[entrada]
mesma_entrada = true                  # todas as rodadas leram o mesmo arquivo (mesmo hash)

[repeticao]
mesma_semente_mesmos_valores = true   # mesma semente -> mesmo hash dos valores

[resultado]
min_celulas_queimadas = 100           # o fogo precisa passar das células onde começou"""))

cells.append(md("""## 3. Rodar e conferir

Rodamos o modelo. A linha começa com `!` porque é um comando do terminal, o mesmo que você usaria fora do notebook. A opção `--preserve-output-name` mantém o nome `fogo.tif`; sem ela, o DisSModel acrescenta um identificador de 8 letras ao nome, para que duas rodadas nunca se sobrescrevam."""))

cells.append(code("""!python fogo.py run --input floresta.tif --toml model.toml --output saida/fogo.tif --preserve-output-name"""))

cells.append(md("""A rodada deixou a saída e, ao lado dela, o **registro**: `saida/fogo.record.json`. O registro diz qual entrada (com o hash), quais parâmetros (com a semente), qual código e qual ambiente. A seção 6 abre o registro; por enquanto vamos usá-lo.

**Primeira pergunta ao registro: o arquivo de saída é o que a execução gerou?**"""))

cells.append(code("""!dissmodel verify saida/fogo.record.json"""))

cells.append(md("""O comando calculou o hash do arquivo `saida/fogo.tif` e comparou com o hash gravado no registro. Vamos ver o que ele pega. Abaixo, mudamos **uma célula** da saída (como se alguém tivesse "arrumado" o resultado à mão) e conferimos de novo. No fim, devolvemos o arquivo original."""))

cells.append(code("""original = open("saida/fogo.tif", "rb").read()      # guarda o arquivo para devolver depois

with rasterio.open("saida/fogo.tif", "r+") as f:
    banda = f.read(1)
    banda[0, 0] = 3                                  # uma célula "arrumada" à mão
    f.write(banda, 1)

!dissmodel verify saida/fogo.record.json"""))

cells.append(code("""open("saida/fogo.tif", "wb").write(original)         # devolve o arquivo original
!dissmodel verify saida/fogo.record.json"""))

cells.append(md("""✏️ **Pergunta 2.** O que o `verify` pegou na segunda conferência? E o que ele **não** diz: se o arquivo bate com o registro, isso prova que o modelo está certo?"""))

cells.append(md("""## 4. Repetir a execução

**Segunda pergunta ao registro: se eu rodar de novo, sai o mesmo resultado?** O comando `reproduce` lê o registro, roda o modelo outra vez com a mesma entrada e os mesmos parâmetros (incluindo a semente) e compara a nova saída com a original. A opção `--module fogo` diz onde está o executor."""))

cells.append(code("""!dissmodel reproduce saida/fogo.record.json --module fogo"""))

cells.append(md("""O veredicto `identical` quer dizer que nem os bytes mudaram. A repetição gravou a saída em `saida/fogo.repro.tif` e um novo registro, `saida/fogo.repro.record.json`.

Agora mudamos **de propósito** a semente. O `--param` sobrescreve o valor do `model.toml` só nesta execução, e o registro guarda o valor usado. Troque o `8` por outro número, se quiser."""))

cells.append(code("""!python fogo.py run --input floresta.tif --toml model.toml --output saida/fogo_semente8.tif --preserve-output-name --param seed=8"""))

cells.append(code("""!dissmodel compare saida/fogo.tif saida/fogo_semente8.tif"""))

cells.append(md("""Vamos ver as saídas lado a lado: a original, a repetição e a de outra semente."""))

cells.append(code("""import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

cores = ListedColormap(["#2e7d32", "#e65100", "#424242", "#e0e0e0"])  # floresta, queimando, queimada, vazia
arquivos = {"semente 7": "saida/fogo.tif", "semente 7, repetida": "saida/fogo.repro.tif",
            "semente 8": "saida/fogo_semente8.tif"}
fig, eixos = plt.subplots(1, len(arquivos), figsize=(4 * len(arquivos), 4))
for ax, (titulo, caminho) in zip(eixos, arquivos.items()):
    with rasterio.open(caminho) as f:
        ax.imshow(f.read(1), cmap=cores, vmin=0, vmax=3, interpolation="nearest")
    ax.set_title(titulo)
    ax.set_axis_off()
plt.tight_layout()"""))

cells.append(md("""✏️ **Pergunta 3.** Um modelo com sorteio é reprodutível? Em que condição? Por que a repetição deu `identical` e a de outra semente, `differs`?

> Um modelo estocástico é reprodutível se a semente for registrada. Para tirar conclusões dele, porém, uma rodada não basta: é preciso várias sementes e olhar a distribuição dos resultados (voltamos a isso no encontro 12)."""))

cells.append(md("""## 5. Mesmos valores, arquivo diferente

Às vezes dois arquivos têm hashes diferentes e **o mesmo conteúdo**. O caso clássico é o mesmo raster gravado com outra compressão. Vamos gravar os mesmos valores de `fogo.tif` com uma compressão diferente e perguntar ao DisSModel."""))

cells.append(code("""with rasterio.open("saida/fogo.tif") as origem:
    banda, perfil = origem.read(1), origem.profile
print("compressão do original:", perfil.get("compress"))

perfil.update(compress="lzw" if perfil.get("compress") != "lzw" else "deflate")
with rasterio.open("saida/fogo_outra_compressao.tif", "w", **perfil) as destino:
    destino.write(banda, 1)
print("compressão da cópia   :", perfil["compress"])"""))

cells.append(code("""!dissmodel compare saida/fogo.tif saida/fogo_outra_compressao.tif"""))

cells.append(md("""Os bytes diferem (`DIFFERS`), mas os valores decodificados, não. O veredicto é `values_identical`: o arquivo mudou, o resultado não. O `compare` olha em degraus, do mais exigente ao menos:

| Veredicto | O que quer dizer |
|---|---|
| `identical` | os mesmos bytes |
| `values_identical` | bytes diferentes, mesmos valores, mesma georreferência |
| `equivalent` | valores diferentes, mas dentro de uma **tolerância que você declarou** (`--atol`) |
| `differs` | diferença que a tolerância (se houver) não cobre, ou raster em outro lugar do mapa |
| `unverified` | algo que importava não pôde ser conferido (arquivo ilegível, formato que o comando não decodifica) |

O `equivalent` nunca aparece sozinho: sem tolerância declarada, o comando não decide por você que uma diferença é "pequena". Veja por quê. O computador arredonda cada conta, e a ordem das contas muda o último dígito:"""))

cells.append(code("""a = (0.1 + 0.2) + 0.3
b = 0.1 + (0.2 + 0.3)
print(a, b, "iguais?", a == b, " diferença:", abs(a - b))"""))

cells.append(md("""Dois rasters com essa diferença, no último dígito, são o mesmo resultado? Sem tolerância, o comando diz `differs`. Com uma tolerância declarada e justificada, `equivalent`:"""))

cells.append(code("""from rasterio.transform import from_origin

for nome, soma in (("a", (0.1 + 0.2) + 0.3), ("b", 0.1 + (0.2 + 0.3))):
    with rasterio.open(f"{nome}.tif", "w", driver="GTiff", height=4, width=4, count=1,
                       dtype="float64", crs="EPSG:4326", transform=from_origin(0, 4, 1, 1)) as f:
        f.write(np.full((4, 4), soma), 1)

!dissmodel compare a.tif b.tif
!dissmodel compare a.tif b.tif --atol 1e-9"""))

cells.append(md("""Por isso há três tipos de verificação, e o trabalho deve dizer qual usou:

| Pergunta | Verificação | Veredicto |
|---|---|---|
| É o arquivo arquivado? | hash do arquivo | `identical` |
| São os mesmos dados, em outra máquina? | hash dos valores | `values_identical` |
| É o mesmo resultado, calculado de novo? | tolerância (maior diferença ≤ ε, com ε justificado) | `equivalent` |

O próprio TerraME, rodado oito vezes na mesma máquina, gravou o primeiro lab do LuccME com hashes diferentes, todos a menos de 10⁻¹² um do outro.

> **Outros formatos.** O `compare` decodifica GeoTIFF. Um GeoPackage (`.gpkg`), por exemplo, guarda dentro do arquivo a hora em que foi gravado; duas rodadas idênticas dão arquivos com hashes diferentes, e o comando responde `unverified`, e não `differs`, porque não conferiu os valores. Para esses formatos, compare os valores com o seu próprio código e declare qual verificação usou.

✏️ **Pergunta 4.** Um colega rodou o seu modelo no computador dele e o `compare` deu `values_identical`. Isso basta para dizer que ele reproduziu o seu resultado? E se tivesse dado `equivalent` com `--atol 0.5`?"""))

cells.append(md("""## 6. O que o registro guarda

Abra o registro de uma execução. Você não escreveu nada disso: o DisSModel preencheu sozinho."""))

cells.append(code("""r = json.load(open("saida/fogo.record.json"))
campos = ["experiment_id", "created_at", "model_name", "model_commit", "code_version",
          "source", "parameters", "output_path", "artifacts", "status"]
print(json.dumps({k: r[k] for k in campos}, indent=2, ensure_ascii=False))"""))

cells.append(md("""| Campo | Pergunta que responde |
|---|---|
| `experiment_id`, `created_at` | Qual execução é esta, e quando rodou? |
| `model_name`, `model_commit`, `code_version` | Qual modelo e qual versão do código? |
| `source` (com `checksum`) | Qual arquivo de entrada, comprovado pelo hash? |
| `parameters` | Com quais parâmetros, incluindo a semente? |
| `artifacts` | Qual o hash de cada arquivo gerado? |
| `metrics` | O que foi medido, quanto tempo levou cada passo e em que **ambiente**? |

✏️ **Pergunta 5.** O campo `model_commit` diz `local-cli`. Por quê? O que mudaria se o executor viesse de um pacote instalado com versão (por exemplo, `disslucc==0.5.1`)?"""))

cells.append(md("""### O ambiente

O mesmo código pode dar outro resultado com outras versões das bibliotecas. Por isso o registro guarda, em `metrics["environment"]`, a versão do Python, do sistema e das bibliotecas, incluindo o GDAL, que é quem grava o arquivo:"""))

cells.append(code("""amb = r["metrics"]["environment"]
print("Python  :", amb["python"], "|", amb["platform"], amb["machine"])
print("GDAL    :", amb["native"]["gdal"])
print("pacotes :", {k: v for k, v in amb["packages"].items() if k in ("dissmodel", "numpy", "rasterio")})
print("tempo   :", r["metrics"]["time_total_sec"], "s |", "queimadas:", r["metrics"]["celulas_queimadas"])"""))

cells.append(md("""Isso já responde a maior parte de "em que máquina isto rodou?". Para o projeto, guarde também a lista completa do que está instalado, que é o que alguém usaria para recriar o ambiente:"""))

cells.append(code("""!pip freeze > requirements.lock
!grep -i -E "^(dissmodel|rasterio|numpy)" requirements.lock"""))

cells.append(md("""## 7. Conferir os critérios sem rodar o modelo

Os registros das rodadas guardam tudo o que os critérios pedem. A função abaixo lê o `aceitacao.toml` e os registros, e diz se cada critério passou. Ela **não roda o modelo**: leva menos de um segundo. É o que se chama de **nível 0** de conferência, a auditoria do registro."""))

cells.append(code("""import tomllib
from collections import defaultdict
from dissmodel.executor.compare import decoded_values_sha256

def hash_dos_valores(caminho):
    return decoded_values_sha256(caminho)     # hash dos valores, não dos bytes do arquivo

def conferir(registros, arquivo="aceitacao.toml"):
    crit = tomllib.load(open(arquivo, "rb"))
    resultado = {}
    if crit["entrada"]["mesma_entrada"]:
        resultado["mesma entrada"] = len({r["source"]["checksum"] for r in registros}) == 1
    if crit["repeticao"]["mesma_semente_mesmos_valores"]:
        por_semente = defaultdict(set)
        for r in registros:
            por_semente[r["parameters"]["seed"]].add(hash_dos_valores(r["output_path"]))
        resultado["mesma semente, mesmos valores"] = all(len(v) == 1 for v in por_semente.values())
    minimo = crit["resultado"]["min_celulas_queimadas"]
    resultado[f"queimadas >= {minimo}"] = all(r["metrics"]["celulas_queimadas"] >= minimo for r in registros)
    for nome, ok in resultado.items():
        print(f"{'OK     ' if ok else 'FALHOU '} {nome}")
    return all(resultado.values())

registros = [json.load(open(f)) for f in ("saida/fogo.record.json", "saida/fogo.repro.record.json",
                                          "saida/fogo_semente8.record.json")]
for r in registros:
    print(r["experiment_id"][:8], " seed =", r["parameters"]["seed"], " queimadas:", r["metrics"]["celulas_queimadas"])
print()
conferir(registros)"""))

cells.append(md("""✏️ **Pergunta 6.** Depois de ver quantas células cada rodada queimou, suponha que você mudasse o mínimo do `aceitacao.toml` para um número que uma das rodadas não alcança. O que aconteceria com essa rodada? Por que isso não vale como critério?

Repetir um experimento inteiro pode levar horas. Por isso um projeto bem montado oferece caminhos mais curtos para quem confere, cada um mostrando uma parte da evidência:

| Nível | O que faz | O que mostra | Neste notebook |
|---|---|---|---|
| 0. Auditar o registro | confere os critérios a partir dos registros | que o resultado relatado cumpre o que foi declarado | `conferir()` e `dissmodel verify` |
| 1. Teste rápido | roda o modelo num caso pequeno, duas vezes | que o código roda e repete o resultado | `dissmodel reproduce` |
| 2. Dados reais | roda o caso de verdade em outra máquina | que outra pessoa chega ao mesmo resultado | `dissmodel compare` com o registro do colega |
| 3. Rodada completa | tudo, com todos os critérios | o experimento inteiro | — |

O repositório [`open-lucc-workflow`](https://github.com/LambdaGeo/open-lucc-workflow) faz isso para um modelo do Brasil inteiro: o nível 0 leva segundos, o nível 1 cerca de 15 s e a rodada completa 6 horas e meia. Lá também está o caso do Mac em que os valores foram iguais e os hashes dos arquivos não (seção 3 das notas).

## 8. Para levar ao projeto

Checklist de reprodutibilidade do projeto da disciplina:

- [ ] Parâmetros num arquivo de configuração, não no código.
- [ ] Semente registrada (e várias sementes, se o modelo for estocástico).
- [ ] Hash dos dados de entrada.
- [ ] Registro de cada execução que vai para o relatório, e a plataforma (`requirements.lock`, versão do Python, sistema).
- [ ] Critérios no `aceitacao.toml`, no git **antes** da rodada final; os que falharem são relatados, não removidos.
- [ ] Níveis 0 e 1 de conferência, com um comando cada no README (`dissmodel verify` e `dissmodel reproduce`).
- [ ] Verificação declarada: hash do arquivo, hash dos valores ou tolerância.

## Exercícios (entregar até o próximo encontro)

1. Rode o modelo com `initial_fire_density` igual a 0.002, 0.005 e 0.01, com a mesma semente (use `--param initial_fire_density=...` e um `--output` diferente para cada uma). Faça uma tabela com a densidade e as células queimadas, tirada dos registros.
2. Peça a um colega o `floresta.tif` e o `model.toml` dele e rode na sua máquina. Use o `dissmodel compare` entre a saída dele e a sua. Qual veredicto saiu? E os hashes dos arquivos?
3. Em duas ou três frases: que informação da sua dissertação você hoje **não** conseguiria recuperar daqui a um ano?
4. Leia as [notas de aula](https://lambdageo-edu.github.io/curso-modelagem-dinamica-espacial/encontros/04-notas/) e escreva um `aceitacao.toml` com dois ou três critérios para o seu projeto, mesmo que provisórios."""))

nb = nbf.v4.new_notebook()
nb["cells"] = cells
nb["metadata"]["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, sys.argv[1])
print("ok", len(cells), "células")
