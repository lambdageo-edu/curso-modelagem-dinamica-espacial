# Encontro 4 — Notas de aula: como conferir um modelo

Estas notas reúnem o método que a disciplina usa para conferir um modelo e o resultado dele. São lidas no encontro 4, junto com o notebook, e voltam nos encontros 7, 9, 12 e 13 e no projeto. Cada ideia vem com um exemplo real, tirado de repositórios abertos do ecossistema DisSModel, que você pode clonar e rodar. Os termos em **negrito** estão no glossário.

## 1. Três perguntas que não se confundem

O encontro 1 separou três palavras. Elas viram três perguntas, e cada uma pede um tipo de evidência:

| Pergunta | Nome | Evidência típica |
| --- | --- | --- |
| O programa faz o que o modelo descreve? | **verificação** | comparação com uma implementação de referência, com os mesmos dados |
| O modelo se parece com o mundo? | **validação** | comparação com um mapa observado que não entrou no ajuste |
| Outra pessoa obtém o mesmo resultado? | **reprodutibilidade** | os mesmos dados, o mesmo código e o registro da execução |

Uma quarta pergunta é a **replicação**: outra equipe, com outro código escrito a partir da descrição publicada, chega a resultados compatíveis? (NASEM, 2019). A iniciativa ReScience C publica exatamente isso, replicações de modelos computacionais escritas do zero (Rougier et al., 2017).

As seções seguintes tratam da verificação e da reprodutibilidade. A validação tem o encontro 13.

## 2. Cada etapa deixa um arquivo que alguém confere

Um resultado de modelo é o fim de uma cadeia: dados de origem, grade de entrada, modelo, saída. Se uma etapa não deixa rastro, ninguém consegue dizer onde um erro entrou. A regra prática é que **cada etapa deixe um arquivo com nome, e que algum teste leia esse arquivo**.

O repositório [`open-lucc-workflow`](https://github.com/LambdaGeo/open-lucc-workflow) (v1.1.0, DOI 10.5281/zenodo.23415814) organiza um experimento de mudança de uso da terra para o Brasil inteiro em cinco etapas:

| Etapa | Arquivo que deixa | Quem confere |
| --- | --- | --- |
| 1. Fontes | lista dos dados abertos, com URL e SHA-256 de cada um | o download recusa um arquivo com outro hash |
| 2. Grade de entrada | o raster com as variáveis, na grade declarada | um teste confere as bandas, a projeção e a máscara |
| 3. Modelo | a saída e os parâmetros declarados em arquivo | — |
| 4. Registro | o registro da execução e um arquivo de métricas | um teste confere os hashes e as versões |
| 5. Aceitação | o relatório dos critérios | um teste compara as métricas com critérios escritos antes |

Na disciplina, a cadeia é a mesma em escala menor: o TOML do DisSCube declara as fontes e a grade (encontro 10), o executor do DisSModel grava o registro (encontro 4) e o projeto termina com os critérios de aceitação (seção 4).

## 3. Identidade e equivalência

Há duas maneiras de dizer que dois resultados "são o mesmo", e o trabalho deve dizer qual usou:

- **Identidade:** os mesmos bytes ou os mesmos valores. Confere-se com o hash (SHA-256): do arquivo, quando a pergunta é "é este o arquivo arquivado?"; dos valores, quando a pergunta é "são os mesmos dados?".
- **Equivalência:** valores que diferem menos que uma **tolerância** declarada e justificada. É o que se usa quando o resultado foi calculado de novo, em outra ordem ou em outra máquina, e o último dígito pode mudar.

O hash do arquivo é a verificação mais forte e a mais frágil. No notebook do encontro 4, duas rodadas idênticas gravam GeoPackages com hashes diferentes porque o arquivo guarda a hora em que foi escrito. O `open-lucc-workflow` registra um caso maior: a mesma rodada, repetida em cinco computadores, deu os mesmos hashes nos quatro com processador x86-64 (Linux e Windows com WSL2). No quinto, um Mac com processador ARM, os critérios de aceitação passaram e as áreas finais de cada classe foram iguais, mas os hashes dos arquivos mudaram. A comparação célula a célula mostrou que os valores da saída eram iguais em todas as células; os bytes diferiam porque cada plataforma comprime o GeoTIFF de um jeito. Lição: **para comparar resultados entre plataformas, use o hash dos valores ou uma tolerância, não o hash do arquivo**.

O mesmo vale para a referência. O próprio TerraME, rodado várias vezes na mesma máquina, grava o primeiro lab do LuccME com diferenças a menos de 10⁻¹² entre execuções. Por isso o `disslucc-benchmark` compara com tolerância, e diz qual.

## 4. Critérios escritos antes de rodar

Quem olha o resultado antes de decidir o que é "bom o bastante" tende a escolher o critério que o resultado já cumpre. A saída é escrever os critérios **antes** da rodada e registrar quando foram escritos. Na pesquisa empírica isso se chama **pré-registro** (Nosek et al., 2018).

Os dois repositórios fazem isso com um arquivo `acceptance.toml`, versionado no git:

- No `open-lucc-workflow`, os critérios são três: a alocação atende à demanda dentro de 1.000 km²; uma rodada repetida dá valores idênticos; as áreas das classes concordam entre as duas resoluções, dentro de 0,5% da área mapeada. O arquivo registra o commit que o congelou, e o comando da rodada completa se recusa a gerar o relatório se os critérios não estiverem congelados. Tempo e memória são registrados, mas não julgados.
- No [`rescience-lulcc`](https://github.com/LambdaGeo/rescience-lulcc) (v0.1.0), uma replicação em Python do pacote lulcc, do R, o commit que cria os critérios vem antes dos commits com resultados. Uma métrica acrescentada depois, ao ver os dados, é publicada à parte, "para informação", fora dos critérios.

Duas cautelas:

- **Um critério cumprido não prova mais do que diz.** "A alocação atendeu à demanda" diz que a conta fechou, não que o mapa está certo.
- **Um critério que falha é relatado, não removido.** O `acceptance.toml` do `rescience-lulcc` diz isso por escrito.

No projeto da disciplina, o `aceitacao.toml` é escrito e entra no git antes da rodada final (encontro 13).

## 5. Níveis de conferência

Repetir um experimento inteiro pode levar horas. Quem confere precisa de caminhos mais curtos, cada um mostrando uma parte da evidência. O `open-lucc-workflow` oferece quatro:

| Nível | O que faz | Tempo | O que mostra |
| --- | --- | --- | --- |
| 0. Auditar o registro | confere os critérios a partir das métricas gravadas, sem rodar o modelo | segundos | que o resultado relatado cumpre os critérios declarados |
| 1. Teste rápido | roda a cadeia num dado sintético pequeno, sem internet, duas vezes | cerca de 15 s | que o código roda e é determinístico |
| 2. Reproduzir com os dados reais | monta a grade a partir das fontes abertas e roda o modelo numa resolução | cerca de 40 min | que outra máquina chega ao mesmo resultado |
| 3. Rodada completa | todas as resoluções e todos os critérios | cerca de 6,5 h | o experimento inteiro |

O nível 1 é também o que a integração contínua roda a cada mudança no código. No projeto da disciplina, pedem-se os níveis 0 e 1, com um comando cada, escritos no README.

## 6. Verificação em camadas

Comparar só o resultado final esconde onde está a diferença. A verificação do DisSLUCC e do DisSCube contra o TerraME e o LuccME foi feita em camadas, cada uma num repositório:

| Camada | Pergunta | Repositório |
| --- | --- | --- |
| Referência | as saídas do TerraME e do LuccME podem ser geradas de novo? | [`terrame-docker`](https://github.com/LambdaGeo/terrame-docker) 0.4.2 (imagem fixada) e [`luccme-goldens`](https://github.com/LambdaGeo/luccme-goldens) 1.1.0 (saídas com hash) |
| Componente espacial | o DisSCube calcula as mesmas variáveis que o `fill` do TerraME? | [`disscube-benchmark`](https://github.com/LambdaGeo/disscube-benchmark) 1.1.0 (encontro 10) |
| Componente dinâmico | o DisSLUCC reproduz os labs do LuccME, ano a ano? | [`disslucc-benchmark`](https://github.com/LambdaGeo/disslucc-benchmark) 0.2.2 (encontros 9 e 11) |
| Cadeia inteira | a cadeia, das fontes aos mapas, cumpre critérios fixados antes? | `open-lucc-workflow` |

Os modelos dos encontros 5 a 7 seguem a mesma ideia com o [`terrame-goldens`](https://github.com/LambdaGeo/terrame-goldens) 0.1.0. Uma diferença encontrada numa camada tem de ter uma causa conhecida. O encontro 9 mostra uma: uma correção de célula que o LuccME nunca executa, por um erro de digitação. Se a causa não é conhecida, a diferença é um problema em aberto, e não um arredondamento.

## 7. Modelos determinísticos e estocásticos

**Determinístico** (sem sorteio, ou com o sorteio fixado): a comparação é feita etapa por etapa, até a igualdade ou até a tolerância. No `rescience-lulcc`, com os mesmos dados de entrada do R, a alocação do CLUE-S dá zero células diferentes em todos os 14 passos, e os coeficientes da regressão logística diferem, em termos relativos, no máximo 1,3 × 10⁻⁹.

**Estocástico:** duas implementações sorteiam números diferentes, e nenhuma rodada de uma é igual a uma rodada da outra. Compara-se a **distribuição** de muitas rodadas de cada lado. O critério do `rescience-lulcc`, para 30 sementes de cada lado e cada métrica, exige duas coisas:

1. as médias diferem menos de 3 erros-padrão da diferença, $|\bar x_1 - \bar x_2| \le 3\sqrt{s_1^2/n_1 + s_2^2/n_2}$;
2. o teste de Kolmogorov–Smirnov de duas amostras não rejeita que as distribuições sejam iguais (p ≥ 0,01).

O encontro 7 aplica esse critério ao modelo de Schelling, contra 50 rodadas do TerraME.

**Uma rodada é um ponto de uma distribuição.** Um número publicado a partir de uma rodada só (um índice, uma área, um mapa) deve ser lido pela posição dele na distribuição de muitas rodadas. O `rescience-lulcc` faz isso com os valores do artigo original: um deles cai no percentil 70 das 30 rodadas do próprio lulcc, outro fica abaixo do mínimo. O encontro 12 faz o mesmo com o lab15.

## 8. Controles negativos: o teste consegue falhar?

Um teste que nunca falha não informa nada. Um **controle negativo** é uma mudança feita de propósito, que *deveria* reprovar o modelo. Se a comparação continua passando, ela não tem poder para ver aquele tipo de erro. A ideia vem da epidemiologia, em que um controle negativo é uma exposição ou um desfecho que não pode ter a relação estudada (Lipsitch, Tchetgen Tchetgen e Cohen, 2010).

O `rescience-lulcc` roda cinco controles negativos: muda a elasticidade, o fator de escala, a tolerância, acrescenta ruído ao potencial ou altera a demanda. Os cinco fazem os mapas diferirem, o que mostra que a comparação teria visto esses erros. Nos encontros:

- no **encontro 9**, aumentar a demanda em 10% quase não muda a comparação do lab01 original com o LuccME, porque a tolerância de 5.000 km² aceita a primeira alocação; a variante com tolerância de 1.643 km² reprova o mesmo erro;
- no **encontro 7**, mudar a fração de células livres do Schelling de 5% para 8% reprova o critério de distribuição; de 5% para 6%, não, porque 50 rodadas não bastam para ver uma diferença tão pequena.

Os dois casos ensinam o limite do teste, e não só o resultado dele.

## 9. A origem de cada parte

Uma replicação mistura partes de origens diferentes, e o leitor precisa saber qual é qual. O `rescience-lulcc` marca cada módulo com uma de três origens: **usado sem mudança** (a alocação do CLUE-S, componente publicado do DisSLUCC), **escrito a partir do artigo** (a regressão, a interpolação da demanda) ou **portado do código original**, quando o artigo deixa uma escolha em aberto. Foi o caso da alocação ordenada, da comparação de três mapas e do arredondamento da demanda. Cada escolha em aberto é listada, com a solução adotada.

Não é excesso de zelo. Uma análise formal dos modelos da família CLUE e do Dinamica EGO concluiu que nenhum deles é descrito com detalhe suficiente para reproduzir as escolhas do algoritmo (Mazy e Longaretti, 2023). O protocolo ODD, usado no relatório do projeto, existe para reduzir esse problema (Grimm et al., 2020).

## 10. Registrar a plataforma

Os resultados dependem do sistema operacional, do processador, da versão do Python e das bibliotecas. O mínimo é um `requirements.lock` (encontro 4). Os dois repositórios vão além e gravam um arquivo com a descrição da máquina a cada rodada: `make platform` no `rescience-lulcc`, `machine.txt` no registro do `open-lucc-workflow`. Foi esse registro que permitiu explicar o caso do Mac da seção 3.

## 11. Para o projeto

O checklist de reprodutibilidade do projeto ([Avaliação e projeto](../avaliacao.md)) resume estas notas:

- dados com hash e parâmetros num arquivo de configuração;
- registro de cada execução e da plataforma;
- critérios escritos no `aceitacao.toml` e no git antes da rodada final, e relatados mesmo que falhem;
- níveis 0 e 1 de conferência, com um comando cada no README;
- verificação declarada: hash do arquivo, hash dos valores ou tolerância;
- se o modelo for estocástico, várias sementes e a leitura pela distribuição.

## Glossário

| Termo | Significado |
| --- | --- |
| Controle negativo | mudança feita de propósito para mostrar que o teste reprova um modelo errado |
| Critério de aceitação | condição, escrita antes da rodada, que o resultado deve cumprir |
| Equivalência | igualdade dentro de uma tolerância declarada |
| Hash (SHA-256) | código calculado a partir de todos os bytes; muda por completo se um byte muda |
| Identidade | mesmos bytes (hash do arquivo) ou mesmos valores (hash dos valores) |
| Nível de conferência | caminho de repetição com custo e alcance definidos (auditar o registro, teste rápido, dados reais, rodada completa) |
| Pré-registro | registro dos critérios e da análise antes de ver os resultados |
| Replicação | resultado compatível obtido por outra equipe, com código novo |
| Reprodutibilidade | o mesmo resultado com os mesmos dados, código e condições |
| Verificação | conferência de que o programa implementa o modelo descrito |

## Referências

Estas referências estão também na [bibliografia](../bibliografia.md).

- GRIMM, V. et al. The ODD protocol for describing agent-based and other simulation models: a second update to improve clarity, replication, and structural realism. *Journal of Artificial Societies and Social Simulation*, v. 23, n. 2, 7, 2020. DOI: 10.18564/jasss.4259.
- LIPSITCH, M.; TCHETGEN TCHETGEN, E.; COHEN, T. Negative controls: a tool for detecting confounding and bias in observational studies. *Epidemiology*, v. 21, n. 3, p. 383–388, 2010. DOI: 10.1097/EDE.0b013e3181d61eeb.
- MAZY, F.-R.; LONGARETTI, P.-Y. Towards a generic theoretical framework for pattern-based LUCC modeling: allocation revisited. *Environmental Modelling & Software*, v. 166, 105706, 2023. DOI: 10.1016/j.envsoft.2023.105706.
- NATIONAL ACADEMIES OF SCIENCES, ENGINEERING, AND MEDICINE. *Reproducibility and Replicability in Science*. Washington: The National Academies Press, 2019. DOI: 10.17226/25303.
- NOSEK, B. A.; EBERSOLE, C. R.; DEHAVEN, A. C.; MELLOR, D. T. The preregistration revolution. *Proceedings of the National Academy of Sciences*, v. 115, n. 11, p. 2600–2606, 2018. DOI: 10.1073/pnas.1708274114.
- ROUGIER, N. P. et al. Sustainable computational science: the ReScience initiative. *PeerJ Computer Science*, v. 3, e142, 2017. DOI: 10.7717/peerj-cs.142.
- SANDVE, G. K.; NEKRUTENKO, A.; TAYLOR, J.; HOVIG, E. Ten simple rules for reproducible computational research. *PLOS Computational Biology*, v. 9, n. 10, e1003285, 2013. DOI: 10.1371/journal.pcbi.1003285.

**Repositórios citados como exemplo**

- COSTA, S. S.; BEZERRA, D. da S.; ALVES, J. M. P. *Open LUCC workflow*. Versão 1.1.0. Zenodo, 2026. DOI: 10.5281/zenodo.23415814.
- COSTA, S. S.; BEZERRA, D. da S.; ALVES, J. M. P.; OLIVEIRA, H. B.; VALE, M. D.; ZHAO, S. K. S. *rescience-lulcc*. Versão 0.1.0. GitHub, 2026. Disponível em: <https://github.com/LambdaGeo/rescience-lulcc>. Saídas de referência do R em *lulcc-goldens*, versão 0.1.0, DOI: 10.5281/zenodo.23866776.
- COSTA, S. S. *terrame-docker*. Versão 0.4.2. Zenodo, 2026. DOI: 10.5281/zenodo.23160784.
- COSTA, S. S. *LuccME goldens*. Versão 1.1.0. Zenodo, 2026. DOI: 10.5281/zenodo.23161342.
- COSTA, S. S. *DisSCube benchmark*. Versão 1.1.0. Zenodo, 2026. DOI: 10.5281/zenodo.23366475.
- COSTA, S. S. *DisSLUCC benchmark*. Versão 0.2.2. Zenodo, 2026. DOI: 10.5281/zenodo.23224097.
- COSTA, S. S. *terrame-goldens*. Versão 0.1.0. Zenodo, 2026. DOI: 10.5281/zenodo.23592970.
