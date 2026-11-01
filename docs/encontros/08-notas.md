# Encontro 8 — Notas de aula: modelos de mudança de uso e cobertura da terra

Estas notas acompanham a exposição do encontro 8 e servem de referência para os encontros 9 a 12. Leia antes da aula ou logo depois; os termos em **negrito** voltam ao longo da disciplina.

## 1. O que um modelo de mudança da terra responde

Um modelo de mudança de uso e cobertura da terra (LUCC, do inglês *land use and cover change*) simula como a ocupação de um território muda ao longo do tempo. As perguntas típicas são quatro:

| Pergunta | Exemplo |
| --- | --- |
| **Quanto** muda? | Quantos km² de floresta serão convertidos em pastagem até 2040? |
| **Onde** muda? | Quais áreas do Cerrado maranhense são mais prováveis de virar soja? |
| **Por quê** muda? | Que peso têm a distância a estradas e o preço da soja no desmatamento? |
| **E se...?** | O que acontece se as unidades de conservação forem respeitadas, ou se uma estrada for asfaltada? |

Vale separar duas palavras que o nome junta. **Cobertura** é o que está sobre o terreno e se vê do satélite (floresta, campo, água, área construída). **Uso** é o que as pessoas fazem com ele (pecuária, agricultura, conservação). Uma mesma cobertura (campo) pode ter usos diferentes (pastagem ou área de proteção). O MapBiomas mapeia sobretudo cobertura, com algumas classes de uso (pastagem, soja).

## 2. Forças motrizes

Mudanças de uso não acontecem ao acaso. Geist e Lambin (2002), ao revisar estudos de desmatamento tropical, separaram dois níveis de causa:

- **Causas diretas** (*proximate*): as atividades que transformam o terreno. Expansão agrícola e pecuária, extração de madeira, abertura de estradas e infraestrutura.
- **Forças subjacentes** (*underlying*): o que leva as pessoas a essas atividades. Fatores econômicos (preços, crédito, mercados), políticos e institucionais (regularização fundiária, fiscalização), tecnológicos, demográficos e culturais.

Um modelo espacial raramente representa as forças subjacentes diretamente. Usa **variáveis explicativas** mensuráveis em cada célula, que funcionam como aproximações (*proxies*):

| Variável explicativa (driver) | O que aproxima |
| --- | --- |
| Distância a estradas ou rios | acesso, custo de transporte |
| Distância a cidades ou portos | mercado |
| Área protegida (unidade de conservação, terra indígena) | restrição institucional |
| Declividade, tipo de solo, altitude | aptidão agrícola |
| Fração já desmatada na vizinhança | contágio, frente de ocupação |
| Assentamentos rurais | política fundiária |

No encontro 9, o modelo do lab do LuccME usa algumas dessas variáveis. No encontro 10, o DisSCube as monta para a área de cada aluno.

## 3. Escala: extensão e resolução

Todo modelo escolhe uma **extensão** (a área inteira estudada) e uma **resolução** (o tamanho de cada célula). As duas mudam o resultado:

- **Resolução fina** (30 m a 1 km) mostra onde exatamente cada mudança acontece, mas exige dados detalhados e torna a localização exata difícil de acertar.
- **Resolução grossa** (5 km a 25 km) suaviza a localização e permite trabalhar com frações: uma célula pode ter 40% de floresta e 60% de pastagem.

Muitos modelos combinam escalas. A demanda é calculada para a região inteira (por exemplo, a área desmatada por ano no estado), e a alocação distribui essa demanda pelas células. Essa separação é a origem da família CLUE (Veldkamp e Fresco, 1996), que Verburg et al. (1999) levaram para a alocação espacial em células e Verburg et al. (2002) adaptaram para células com uma classe só (CLUE-S).

A resolução também afeta a avaliação: um modelo que erra a célula exata pode acertar a quantidade na vizinhança. Por isso a validação compara em mais de uma resolução (seção 7).

## 4. Abordagens e ferramentas

Os modelos LUCC diferem em como estimam onde a mudança é provável e em como decidem quais células mudam.

| Abordagem | Como funciona | Exemplos |
| --- | --- | --- |
| Empírica-estatística | ajusta uma regressão entre o uso observado e os drivers; usa o resultado como potencial de cada célula | CLUE, CLUE-S, LuccME, DisSLUCC |
| Autômato celular com pesos de evidência | calcula, para cada faixa de cada variável, quanto ela aumenta a chance de transição; aloca com regras de vizinhança | Dinamica EGO |
| Aprendizado de máquina | uma rede neural ou outro classificador aprende o potencial de transição a partir dos mapas | Land Change Modeler (TerrSet) |
| Autômato celular de crescimento urbano | regras de difusão, crescimento de bordas e influência de estradas, calibradas com mapas históricos | SLEUTH |
| Baseada em agentes | produtores, famílias ou empresas decidem o uso do lote | modelos acadêmicos específicos; o encontro 7 mostrou a ideia |
| Econômica | o uso resulta do equilíbrio entre oferta, demanda e preços de produtos agrícolas | modelos de equilíbrio parcial ou geral |

Diferenças práticas entre as ferramentas mais usadas no Brasil:

| Ferramenta | Origem | Linguagem e licença |
| --- | --- | --- |
| LuccME | INPE | Lua, sobre o TerraME; código aberto |
| Dinamica EGO | UFMG | interface gráfica própria; gratuito, mas com licença proprietária (sem modificação nem redistribuição) |
| CLUE-S | Universidade de Wageningen | programa para Windows; gratuito |
| lulcc | Imperial College London | pacote R; código aberto (Moulds et al., 2015) |
| Land Change Modeler | Clark Labs | módulo do TerrSet; comercial |
| DisSLUCC | LambdaGeo/UFMA | Python, sobre o DisSModel; código aberto; comparado com o LuccME |

Ferramentas da mesma família não dão necessariamente o mesmo mapa: comparando quatro programas com os mesmos dados, Mas et al. (2014) encontraram diferenças de método que mudam o resultado, e Mazy e Longaretti (2023) mostraram que as descrições publicadas deixam escolhas de alocação em aberto. É uma das razões pelas quais a disciplina compara cada componente com uma implementação de referência.

## 5. Demanda, potencial e alocação

A maior parte dos modelos da família CLUE, incluindo o LuccME e o DisSLUCC, divide o problema em três componentes. É a estrutura que o encontro 7 mostrou em miniatura e que o encontro 9 roda com dados.

**Demanda (quanto).** A área de cada classe em cada ano, calculada fora do espaço. Pode vir de uma tendência histórica (a taxa do PRODES nos últimos anos), de um modelo econômico ou de um cenário (seção 6). No DisSLUCC é uma tabela: ano × classe × área.

**Potencial (onde é mais provável).** Um número por célula e por classe, que diz o quanto ela é apta a ter aquele uso. No LuccME e no DisSLUCC, o potencial vem de uma regressão sobre os drivers, ajustada com dados de um período passado. Uma regressão com coeficiente negativo para "distância a estradas" diz que, quanto mais longe da estrada, menor a chance de desmatamento.

**Alocação (onde de fato muda).** Um procedimento iterativo que distribui a demanda pelas células, em ordem de potencial, até que a soma de cada classe bata com a demanda do ano. As variantes:

- **contínua:** cada célula guarda frações das classes (40% floresta, 60% pastagem), como no CLUE e no lab01 do LuccME (encontro 9);
- **discreta:** cada célula tem uma classe só, como no CLUE-S e no lab15 do LuccME (encontro 11);
- **com restrições:** células em áreas protegidas não mudam, ou mudam menos;
- **com inércia:** algumas classes resistem a mudar (uma área urbana raramente volta a ser floresta).

A separação tem uma consequência importante: **a demanda decide a quantidade e o potencial decide a localização.** Um modelo pode acertar uma e errar a outra, e por isso as duas são avaliadas separadamente. Como o potencial é especificado (que regressão, que variáveis) também muda o resultado: com a mesma alocação, duas especificações diferentes chegaram a mapas diferentes em 15% das células num estudo nas Filipinas (Overmars et al., 2007).

## 6. Cenários

Um **cenário** é uma história coerente e plausível sobre o futuro, traduzida em números que o modelo usa. Não é uma previsão: ninguém afirma que o futuro será assim, e sim "se as condições forem estas, o resultado tende a ser este".

O caminho vai da narrativa aos parâmetros:

| Narrativa | Vira, no modelo |
| --- | --- |
| "O desmatamento segue a média dos últimos dez anos" | demanda extrapolada da série do PRODES |
| "A fiscalização reduz o desmatamento à metade" | demanda com taxa reduzida |
| "As unidades de conservação são respeitadas" | restrição na alocação |
| "A estrada X é asfaltada em 2030" | driver "distância a estradas" recalculado a partir de 2030 |

Os estudos costumam comparar pelo menos dois cenários, por exemplo um de **tendência** (*business as usual*) e um de **governança**. Soares-Filho et al. (2006) fizeram isso para a bacia amazônica com o Dinamica EGO, e Aguiar et al. (2016) usaram o LuccME para cenários de emissões na Amazônia brasileira; são os dois artigos da ficha de leitura. Em escala global, as narrativas dos *Shared Socioeconomic Pathways* (SSPs), usadas pelo IPCC, seguem a mesma lógica.

O valor de um cenário está na **diferença** entre eles: o que muda, e onde, se a política X for adotada. O número absoluto de um cenário isolado vale pouco.

## 7. Calibração, validação e verificação

**Calibrar** é ajustar o modelo com dados de um período passado: por exemplo, estimar os coeficientes do potencial com os mapas de 2008 e 2016. **Validar** é rodar o modelo calibrado para um período seguinte, que ele não viu (2016 a 2024), e comparar o simulado com o observado. Validar com os mesmos dados da calibração não prova nada.

Duas cautelas:

- **Compare com o modelo nulo.** O modelo nulo é "nada muda": o mapa final é igual ao inicial. Como as mudanças anuais costumam ser pequenas, ele acerta a maior parte das células. Um modelo só tem mérito se fizer melhor que isso. Comparações de vários modelos publicadas por Pontius et al. (2008) mostraram que superar o modelo nulo na resolução original é mais difícil do que parece.
- **Separe quantidade de localização** (Pontius e Millones, 2011), e avalie em mais de uma resolução: o erro de localização diminui quando a célula de comparação cresce (Pontius, Huffaker e Denman, 2004).

O encontro 13 faz essa validação com um lab do LuccME e o mapa observado, e o encontro 12 trata da incerteza que vem dos parâmetros.

**Verificar** é outra coisa: conferir se o programa faz o que o modelo descreve. Foi o que os encontros 5 a 7 fizeram ao comparar o DisSModel com o TerraME, e o que os encontros 9 a 11 fazem com o DisSLUCC e o DisSCube. Verificação mostra que o código está certo; validação, que o modelo representa o território.

## 8. Limites

- **Extrapolação:** um modelo calibrado num período só sabe o que aconteceu nele. Mudanças de política, preço ou tecnologia rompem a relação ajustada.
- **Equifinalidade:** modelos diferentes podem reproduzir igualmente bem o mesmo mapa observado e divergir no futuro.
- **Dados:** a qualidade do mapa de uso (acurácia do MapBiomas na região, por exemplo) limita o que o modelo pode acertar.
- **Correlação não é causa:** um driver com coeficiente forte pode estar apenas acompanhando a causa real.

## Glossário

| Termo | Significado |
| --- | --- |
| Alocação | procedimento que distribui a demanda pelas células |
| Calibração | ajuste dos parâmetros com dados de um período passado |
| Cenário | narrativa sobre o futuro traduzida em parâmetros do modelo |
| Demanda | área de cada classe por ano, definida fora do espaço |
| Driver (variável explicativa) | variável espacial que explica onde a mudança ocorre |
| Modelo nulo | modelo em que nada muda; referência mínima de desempenho |
| Potencial | aptidão de cada célula para cada classe |
| Resolução | tamanho da célula |
| Validação | comparação com dados observados de um período não usado na calibração |
| Verificação | conferência de que o programa implementa corretamente o modelo |

## Referências

Estas referências estão também na [bibliografia](../bibliografia.md), com a situação de cada uma.

- AGUIAR, A. P. D. et al. Land use change emission scenarios: anticipating a forest transition process in the Brazilian Amazon. *Global Change Biology*, v. 22, n. 5, p. 1821–1840, 2016. DOI: 10.1111/gcb.13134.
- GEIST, H. J.; LAMBIN, E. F. Proximate causes and underlying driving forces of tropical deforestation. *BioScience*, v. 52, n. 2, p. 143–150, 2002.
- MAS, J.-F. et al. Inductive pattern-based land use/cover change models: a comparison of four software packages. *Environmental Modelling & Software*, v. 51, p. 94–111, 2014. DOI: 10.1016/j.envsoft.2013.09.010.
- MAZY, F.-R.; LONGARETTI, P.-Y. Towards a generic theoretical framework for pattern-based LUCC modeling: allocation revisited. *Environmental Modelling & Software*, v. 166, 105706, 2023. DOI: 10.1016/j.envsoft.2023.105706.
- MOULDS, S.; BUYTAERT, W.; MIJIC, A. An open and extensible framework for spatially explicit land use change modelling: the lulcc R package. *Geoscientific Model Development*, v. 8, p. 3215–3229, 2015. DOI: 10.5194/gmd-8-3215-2015.
- OVERMARS, K. P.; VERBURG, P. H.; VELDKAMP, T. A. Comparison of a deductive and an inductive approach to specify land suitability in a spatially explicit land use model. *Land Use Policy*, v. 24, n. 3, p. 584–599, 2007.
- PONTIUS JR., R. G. et al. Comparing the input, output, and validation maps for several models of land change. *The Annals of Regional Science*, v. 42, n. 1, p. 11–37, 2008. DOI: 10.1007/s00168-007-0138-2.
- PONTIUS JR., R. G.; HUFFAKER, D.; DENMAN, K. Useful techniques of validation for spatially explicit land-change models. *Ecological Modelling*, v. 179, n. 4, p. 445–461, 2004.
- PONTIUS JR., R. G.; MILLONES, M. Death to Kappa: birth of quantity disagreement and allocation disagreement for accuracy assessment. *International Journal of Remote Sensing*, v. 32, n. 15, p. 4407–4429, 2011.
- SOARES-FILHO, B. S. et al. Modelling conservation in the Amazon basin. *Nature*, v. 440, p. 520–523, 2006.
- VELDKAMP, A.; FRESCO, L. O. CLUE: a conceptual model to study the conversion of land use and its effects. *Ecological Modelling*, v. 85, p. 253–270, 1996.
- VERBURG, P. H. et al. A spatial explicit allocation procedure for modelling the pattern of land use change based upon actual land use. *Ecological Modelling*, v. 116, n. 1, p. 45–61, 1999.
- VERBURG, P. H. et al. Modeling the spatial dynamics of regional land use: the CLUE-S model. *Environmental Management*, v. 30, n. 3, p. 391–405, 2002. DOI: 10.1007/s00267-002-2630-x.
