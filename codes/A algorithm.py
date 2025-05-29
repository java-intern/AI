from queue import PriorityQueue

def a_star(start, goal, graph, h):
    pq = PriorityQueue()
    pq.put((h[start], 0, start, []))
    visited = set()
    while not pq.empty():
        f, g, node, path = pq.get()
        if node in visited: continue
        visited.add(node)
        path = path + [node]
        if node == goal: print("Path:", path); return
        for neighbor, cost in graph[node]:
            pq.put((g + cost + h[neighbor], g + cost, neighbor, path))

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 5)],
    'D': []
}
h = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
a_star('A', 'D', graph, h)
