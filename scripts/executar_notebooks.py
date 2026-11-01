"""Gera e executa os notebooks dos encontros.

Cada `build_encontroNN.py` escreve um notebook; este script o executa numa pasta
temporária (os notebooks criam arquivos como `fogo.py` e `saida/`) e grava a versão
executada em `docs/notebooks/`, que é a que o site mostra.

Células com a tag `raises-exception` mostram um erro de propósito. Células com a
tag `sem-saida-no-site` leem dados de fora (MapBiomas) e ficam sem saída no site.

Uso:
    python scripts/executar_notebooks.py            # todos
    python scripts/executar_notebooks.py 05 06      # só alguns
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "docs" / "notebooks"

ENCONTROS = {
    "02": "encontro02_python_basico",
    "03": "encontro03_python_dados_espaciais",
    "04": "encontro04_reprodutibilidade",
    "05": "encontro05_dinamica_sistemas",
    "06": "encontro06_automatos_celulares",
    "07": "encontro07_agentes_acoplamento",
    "09": "encontro09_disslucc",
    "10": "encontro10_disscube",
    "11": "encontro11_potencial_alocacao",
    "12": "encontro12_incerteza_sensibilidade",
}


def executar(numero: str) -> None:
    nome = ENCONTROS[numero]
    gerador = RAIZ / "scripts" / f"build_encontro{numero}.py"
    with tempfile.TemporaryDirectory() as pasta:
        caminho = Path(pasta) / f"{nome}.ipynb"
        subprocess.run([sys.executable, str(gerador), str(caminho)], check=True)
        nb = nbformat.read(caminho, as_version=4)
        inicio = time.perf_counter()
        NotebookClient(nb, timeout=600, kernel_name="python3", allow_errors=True,
                       resources={"metadata": {"path": pasta}}).execute()
        erros = 0
        for c in nb.cells:
            tags = c.get("metadata", {}).get("tags", [])
            if "sem-saida-no-site" in tags:        # dependem de rede externa (MapBiomas)
                c.outputs, c.execution_count = [], None
            elif "raises-exception" not in tags:   # erros de propósito ficam
                erros += sum(o.get("output_type") == "error" for o in c.get("outputs", []))
        if erros:
            raise SystemExit(f"{nome}: {erros} célula(s) com erro")
        nbformat.write(nb, SAIDA / f"{nome}.ipynb")
        print(f"{nome}: ok em {time.perf_counter() - inicio:.0f} s")


if __name__ == "__main__":
    for n in sys.argv[1:] or ENCONTROS:
        executar(n)
