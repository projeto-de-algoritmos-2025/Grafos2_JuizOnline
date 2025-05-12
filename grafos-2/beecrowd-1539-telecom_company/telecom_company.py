import math
import heapq

# Calcula a distância Euclidiana entre duas antenas
def distancia(a, b):
    x1, y1, _ = a
    x2, y2, _ = b
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Dijkstra para menor caminho entre duas antenas
def dijkstra(grafo, inicio, fim, N):
    dist = [math.inf] * N
    dist[inicio] = 0
    heap = [(0, inicio)]

    while heap:
        d, u = heapq.heappop(heap)
        if u == fim:
            return int(d)  # Trunca para inteiro, como exigido
        if d > dist[u]:
            continue
        for v, peso in grafo[u]:
            if dist[v] > dist[u] + peso:
                dist[v] = dist[u] + peso
                heapq.heappush(heap, (dist[v], v))
    return -1  # Não há caminho

# Processamento de múltiplos casos
while True:
    try:
        N = int(input())  # Número de antenas
        antenas = []

        for _ in range(N):
            X, Y, R = map(int, input().split())  # Posição e raio
            antenas.append((X, Y, R))

        # Monta o grafo: se uma antena alcança outra, adiciona aresta direcionada
        grafo = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                dist = distancia(antenas[i], antenas[j])
                if dist <= antenas[i][2]:  # Se antena i alcança j
                    grafo[i].append((j, dist))  # Aresta com peso = distância

        # Leitura das consultas
        C = int(input())
        for _ in range(C):
            A1, A2 = map(int, input().split())
            resposta = dijkstra(grafo, A1 - 1, A2 - 1, N)
            print(resposta if resposta != -1 else -1)

    except EOFError:
        break
