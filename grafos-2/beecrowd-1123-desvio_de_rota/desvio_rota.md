# Desvio rota

![questao_desvio_rota](../../assets\desvio_de_rota\desvio_questao.png)

## Contextualização

O país tem várias cidades conectadas por estradas com pedágio. Uma transportadora faz entregas seguindo uma rota fixa entre algumas dessas cidades. Um dia, o veículo da entrega quebrou e foi consertado em uma cidade fora dessa rota. Agora, ele precisa voltar a seguir a rota exatamente como ela foi definida, mas pode usar outras estradas para chegar até o ponto inicial da rota.

A tarefa é descobrir qual é o menor custo em pedágios para que o veículo, começando da cidade onde foi consertado, consiga entregar a encomenda no destino final da rota — respeitando que, ao entrar na rota, ele só pode seguir por ela até o fim.


## Estratégia utilizada

A ideia é usar o algoritmo de Dijkstra para encontrar o caminho mais barato com pedágios. Mas como há uma regra especial, ao entrar na rota fixa o veículo só pode seguir adiante nesta.

- Construi o grafo com todas as cidades e estradas.
- Para as cidades dentro da rota (de 0 até C−1), só permitimos conexões entre vizinhas diretas (ex: de 0 para 1, de 1 para 2 etc.), porque a ordem deve ser seguida.
- Para o resto das cidades (fora da rota), as conexões são normais, como num grafo comum.
- Por fim, apliquei o Dijkstra a partir da cidade em que o veículo foi consertado (cidade K), buscando o menor custo para chegar até a última cidade da rota (C−1), obedecendo essas restrições. 