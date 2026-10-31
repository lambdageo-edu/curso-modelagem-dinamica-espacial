# Cronograma

Seis módulos: fundamentos (1), Python (2–3), reprodutibilidade e paradigmas didáticos (4–7), modelos de mudança da terra e dados (8–10), LUCC no DisSLUCC com cenários (11–12), verificação e projeto (13–15). O projeto final começa a ser definido no encontro 7, para haver tempo de montar os dados.

Os encontros com roteiro e notebook prontos têm link.

| Enc. | Módulo | Tema | Prática | Ferramenta |
| --- | --- | --- | --- | --- |
| 1 | Fundamentos | O que é modelagem dinâmica espacial: espaço, tempo, processo, escala; modelo como hipótese; panorama das ferramentas (TerraME, NetLogo, Dinamica EGO, Mesa, PySD) | Explorar modelos prontos no navegador, sem programar | NetLogo Web, demonstrações |
| 2 | Python | Notebook, células, variáveis, tipos, listas, laços, funções; ler mensagens de erro | Calcular e plotar uma série simples (crescimento populacional) | Jupyter/Colab |
| 3 | Python | NumPy (matrizes como grades), pandas (tabelas), gráficos; abrir um raster e um shapefile | Ler um GeoTIFF do MapBiomas e contar pixels por classe | NumPy, pandas, rasterio, geopandas |
| [4](encontros/04-reprodutibilidade.md) | Reprodutibilidade e DisSModel | Por que reprodutibilidade importa: a crise relatada nas ciências, reprodutível × replicável (NASEM), o que quebra um resultado (dados sem origem, versões, aleatoriedade, parâmetros no código). Como o DisSModel trata isso desde o projeto: versões fixadas, configuração separada do código, semente, registro da execução e hash da saída | Rodar o mesmo modelo duas vezes e comparar os hashes; trocar a semente e ver o hash mudar; ler o registro da execução | dissmodel |
| [5](encontros/05-dinamica-sistemas.md) | Dinâmica de sistemas | Estoques, fluxos, retroalimentação, equilíbrio; o ambiente e o relógio do DisSModel | Banheira, SIR e Lotka-Volterra; variar parâmetros; comparar com a saída do TerraME | dissmodel-sysdyn, terrame-docker (demonstração) |
| [6](encontros/06-automatos-celulares.md) | Autômatos celulares | Espaço celular, estado, vizinhança, regra, borda; processos espaciais | Jogo da Vida e modelo de incêndio; densidade crítica; borda fixa × periódica | dissmodel-ca |
| [7](encontros/07-agentes-acoplamento.md) | Agentes e acoplamento | Agentes e sociedades (visão geral); acoplar um AC a uma dinâmica de sistemas | Ler um modelo de agentes pronto; esboço do projeto final | dissmodel-abm (demonstração) |
| 8 | Modelos de mudança da terra | Land change models em geral: forças motrizes, escalas, abordagens; demanda, potencial e alocação; CLUE/CLUE-S, Dinamica EGO, LuccME, Land Change Modeler, SLEUTH. Cenários: narrativa traduzida em números, cenário × previsão; demanda decide quanto, potencial e restrições decidem onde | Ler e comparar dois estudos de cenários na Amazônia ou no Cerrado | — |
| 9 | Dados | Grade como garantia; cubo de dados; o `fill` do TerraME e seus operadores | Arquivo TOML com fontes e derivações sobre um recorte pequeno | disscube |
| 10 | Dados | Fontes abertas: MapBiomas, PRODES, BDC; agregação por classe, percentual, distância | Montar a grade do projeto de cada aluno; conferir com `disscube plot` | disscube |
| 11 | LUCC | Estrutura de um modelo no DisSLUCC; demanda como tabela; dois cenários de demanda | Rodar um lab; cenários "tendência" e "governança" (taxa reduzida); curva de área por ano e mapa das células que mudam só num deles | disslucc |
| 12 | LUCC | Potencial por regressão; alocação contínua, discreta e por saturação; restrições e sensibilidade | Ajustar a regressão nos dados da turma; rodar com e sem áreas protegidas como restrição; varrer um coeficiente e fazer o mapa de concordância | disslucc |
| 13 | Verificação e validação | Verificar × validar; comparação com uma implementação de referência; tolerância para equivalência; validação multiescala | Comparar uma rodada com o golden do LuccME; validar a rodada da turma contra o mapa observado | disslucc-benchmark |
| 14 | Projeto | Seminários: modelo, dados, resultados e limitações | Apresentações de 15 min com discussão | — |
| 15 | Projeto | Seminários e fechamento | Apresentações; avaliação da disciplina | — |
