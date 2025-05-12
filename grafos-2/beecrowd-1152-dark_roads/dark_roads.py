# Função para encontrar o representante de um conjunto no Union-Find

def find(pai, u):
    if pai[u] != u:
        pai[u] = find(pai, pai[u])  # Path compression
    return pai[u]

# Função para unir dois conjuntos no Union-Find
def union(pai, rank, u, v):
    ru = find(pai, u)
    rv = find(pai, v)
    if ru == rv:
        return False  # Já estão no mesmo conjunto formaria ciclo
    if rank[ru] < rank[rv]:
        pai[ru] = rv
    else:
        pai[rv] = ru
        if rank[ru] == rank[rv]:
            rank[ru] += 1
    return True

while True:
    m, n = map(int, input().split())  # m = número de cidades, n = número de estradas
    if m == 0 and n == 0:
        break  # Fim dos testes

    arestas = []
    total_custo = 0  # Soma de todas as estradas iluminadas

    for _ in range(n):
        x, y, z = map(int, input().split())
        arestas.append((z, x, y))  # adiciona a aresta com custo z
        total_custo += z  # acumula o custo total da rede atual

    # Ordena as arestas pelo custo (crescente)
    arestas.sort()
    pai = list(range(m))  # Union-Find: cada cidade começa em seu próprio conjunto
    rank = [0] * m

    custo_mst = 0  # Soma do custo da Árvore Geradora Mínima (MST)
    for z, u, v in arestas:
        if union(pai, rank, u, v):
            custo_mst += z  # Adiciona à MST

    # tudo o que pode ser apagado mantendo conectividade
    economia = total_custo - custo_mst
    print(economia)
