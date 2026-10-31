"""Gera e executa os notebooks dos encontros.

Cada `build_encontroNN.py` escreve um notebook; este script o executa numa pasta
temporária (os notebooks criam arquivos como `fogo.py` e `saida/`) e grava a versão
executada em `docs/notebooks/`, que é a que o site mostra.

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
    "04": "encontro04_reprodutibilidade",
    "05": "encontro05_dinamica_sistemas",
    "06": "encontro06_automatos_celulares",
    "07": "encontro07_agentes_acoplamento",
}


def executar(numero: str) -> None:
    nome = ENCONTROS[numero]
    gerador = RAIZ / "scripts" / f"build_encontro{numero}.py"
    with tempfile.TemporaryDirectory() as pasta:
        caminho = Path(pasta) / f"{nome}.ipynb"
        subprocess.run([sys.executable, str(gerador), str(caminho)], check=True)
        nb = nbformat.read(caminho, as_version=4)
        inicio = time.perf_counter()
        NotebookClient(nb, timeout=600, kernel_name="python3",
                       resources={"metadata": {"path": pasta}}).execute()
        erros = [o for c in nb.cells for o in c.get("outputs", []) if o.get("output_type") == "error"]
        if erros:
            raise SystemExit(f"{nome}: {len(erros)} célula(s) com erro")
        nbformat.write(nb, SAIDA / f"{nome}.ipynb")
        print(f"{nome}: ok em {time.perf_counter() - inicio:.0f} s")


if __name__ == "__main__":
    for n in sys.argv[1:] or ENCONTROS:
        executar(n)
