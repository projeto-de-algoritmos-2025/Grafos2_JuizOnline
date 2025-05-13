# Agente 004

![agente_004](../..\assets\agente004\agente_questao.png)

## Contextualiação

Bino é um agente secreto encarregado de entregar uma mensagem entre dois pontos da cidade. A cidade, no entanto, está cheia de criminosos que tentam interceptá-lo. Ele pode eliminar qualquer número de criminosos, desde que os encontre antes ou ao mesmo tempo em que eles cheguem em um local. Caso os criminosos cheguem antes, o local se torna perigoso e ele não pode passar por lá.

Existem dois tipos de rotas:

Rotas conhecidas por Bino, que ele pode utilizar.

Rotas secretas, conhecidas apenas pelos criminosos.

Bino e os criminosos se movem à mesma velocidade (12 m/s), e os criminosos podem usar todas as rotas, enquanto Bino está limitado às suas.

O objetivo é encontrar a quantidade mínima de criminosos que Bino terá que enfrentar ao seguir o caminho mais seguro até o destino.


## Estratégia

Simulei o movimento dos criminosos:

Utilizei o algoritmo de Dijkstra com múltiplas fontes (os locais onde os criminosos estão) e todas as rotas para calcular o tempo mínimo que os criminosos levam para chegar a cada ponto da cidade.

Simular o movimento de Bino:

Rodei Dijkstra apenas com as rotas conhecidas por Bino.

Bino só pode passar por um ponto se chegar antes ou ao mesmo tempo que os criminosos.

Contar os criminosos enfrentados:

Verificando, entre os locais onde Bino passou, quantos criminosos estavam presentes inicialmente nesses locais.

O total representa os criminosos que ele terá que eliminar.



# Resultado


O resultado infelizmente não foi satisfatório tendo em vista que atingi apenas 80% de acerto.

![Resultado](../..\assets\agente004\agente_80%.png)