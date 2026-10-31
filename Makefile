.PHONY: serve build notebooks

serve:        ## site local em http://127.0.0.1:8000
	mkdocs serve

build:        ## gera o site em site/, falhando em qualquer aviso
	mkdocs build --strict

notebooks:    ## regenera e executa os notebooks (precisa de requirements-notebooks.txt e rede)
	python scripts/executar_notebooks.py
