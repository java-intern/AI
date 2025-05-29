from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited: continue
        visited.add((x, y))
        if x == 4 or y == 4:
            print(f"Solution: {x},{y}"); return
        moves = [(0, y), (x, 0), (3, y), (x, 5),
                 (min(x + y, 3), y - (min(x + y, 3) - x)),
                 (x - (min(x + y, 5) - y), min(x + y, 5))]
        queue.extend(moves)

water_jug()
