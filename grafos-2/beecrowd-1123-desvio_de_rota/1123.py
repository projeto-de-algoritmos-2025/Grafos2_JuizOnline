import heapq
import sys

input = sys.stdin.readline

def dijkstra(grafo, N, C, K):
    dist = [float('inf')] * N
    dist[K] = 0
    heap = [(0, K)]

    while heap:
        custo, u = heapq.heappop(heap)
        if custo > dist[u]:
            continue

        for v, p in grafo[u]:
            if u < C and v != u + 1:
                continue  # está na rota, só pode seguir para a próxima

            if dist[v] > custo + p:
                dist[v] = custo + p
                heapq.heappush(heap, (dist[v], v))

    return dist[C - 1]

while True:
    linha = input()
    if not linha:
        break

    N, M, C, K = map(int, linha.strip().split())
    if N == M == C == K == 0:
        break

    grafo = [[] for _ in range(N)]

    for _ in range(M):
        u, v, p = map(int, input().split())
        if u < C and v < C:
            if abs(u - v) == 1:
                grafo[u].append((v, p))
                grafo[v].append((u, p))
        else:
            grafo[u].append((v, p))
            grafo[v].append((u, p))

    print(dijkstra(grafo, N, C, K))
