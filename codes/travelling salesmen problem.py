from itertools import permutations

def tsp():
    dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    cities = range(4)
    min_path = float('inf')
    for p in permutations(cities):
        cost = sum(dist[p[i]][p[i+1]] for i in range(3)) + dist[p[3]][p[0]]
        min_path = min(min_path, cost)
    print("Minimum Cost:", min_path)

tsp()
