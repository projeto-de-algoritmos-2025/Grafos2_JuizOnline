import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def dijkstra(start_nodes, graph, n):
    dist = [float('inf')] * (n + 1)
    heap = []
    for node in start_nodes:
        dist[node] = 0
        heapq.heappush(heap, (0, node))
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

while True:
    line = ''
    while line.strip() == '':
        line = sys.stdin.readline()
        if not line:
            sys.exit(0)

    N, C, S, B = map(int, line.strip().split())
    
    bino_graph = [[] for _ in range(N + 1)]
    full_graph = [[] for _ in range(N + 1)]
    
    for _ in range(C):
        a, b, v = map(int, sys.stdin.readline().split())
        bino_graph[a].append((b, v))
        bino_graph[b].append((a, v))
        full_graph[a].append((b, v))
        full_graph[b].append((a, v))
    
    for _ in range(S):
        a, b, v = map(int, sys.stdin.readline().split())
        full_graph[a].append((b, v))
        full_graph[b].append((a, v))

    loc_criminosos = list(map(int, sys.stdin.readline().split()))
    K, F = map(int, sys.stdin.readline().split())

    # Tempo mínimo que qualquer criminoso chega em cada nó
    tempo_criminoso = dijkstra(loc_criminosos, full_graph, N)

    # Bino tenta chegar antes dos criminosos
    dist = [float('inf')] * (N + 1)
    heap = []
    dist[K] = 0
    heapq.heappush(heap, (0, K))
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in bino_graph[u]:
            if dist[v] > dist[u] + w:
                chegada_bino = dist[u] + w
                if chegada_bino <= tempo_criminoso[v]:
                    dist[v] = chegada_bino
                    heapq.heappush(heap, (dist[v], v))

    # A quantidade mínima de criminosos que Bino encontrará é:
    # Aqueles que ele encontra nos pontos onde ele chega no mesmo tempo ou antes.
    # Basta contar quantos criminosos estão em locais que ele visitou.

    # Criminosos nos locais visitados por Bino
    local_bino_passou = set()
    for i in range(1, N + 1):
        if dist[i] <= tempo_criminoso[i]:
            local_bino_passou.add(i)
    
    resposta = sum(1 for c in loc_criminosos if c in local_bino_passou)

    print(resposta)
