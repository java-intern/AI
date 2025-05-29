from collections import deque

def is_safe(m, c): return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

def mc():
    visited = set()
    q = deque([((3, 3, 1), [])])
    moves = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]
    while q:
        (m, c, b), path = q.popleft()
        if (m, c, b) in visited: continue
        visited.add((m, c, b))
        if (m, c, b) == (0, 0, 0): print(path + [(m, c, b)]); return
        for dm, dc in moves:
            nm, nc, nb = (m - dm, c - dc, 0) if b else (m + dm, c + dc, 1)
            if is_safe(nm, nc): q.append(((nm, nc, nb), path + [(m, c, b)]))

mc()
