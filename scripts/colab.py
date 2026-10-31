"""Selo "Abrir no Colab" para a primeira célula dos notebooks."""

REPO = "lambdageo-edu/curso-modelagem-dinamica-espacial"
RAMO = "main"


def selo(nome: str) -> str:
    """Markdown do selo que abre docs/notebooks/<nome>.ipynb no Google Colab."""
    url = f"https://colab.research.google.com/github/{REPO}/blob/{RAMO}/docs/notebooks/{nome}.ipynb"
    return (f"[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)]({url})\n\n"
            "Sem Python instalado? O selo acima abre este notebook no Google Colab, no navegador. "
            "Lá, use *Arquivo → Salvar uma cópia no Drive* antes de mudar qualquer coisa: "
            "sem a cópia, o que você escrever se perde ao fechar a página.")
