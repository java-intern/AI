from collections import deque

def is_goal(state):
    return state == '123456780'

def get_neighbors(state):
    moves = []
    idx = state.index('0')
    swap = lambda i: state[:i] + state[idx] + state[i+1:idx] + state[i] + state[idx+1:]
    if idx not in [0, 1, 2]: moves.append(swap(idx - 3))
    if idx not in [6, 7, 8]: moves.append(swap(idx + 3))
    if idx % 3 != 0: moves.append(swap(idx - 1))
    if idx % 3 != 2: moves.append(swap(idx + 1))
    return moves

def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state in visited: continue
        visited.add(state)
        if is_goal(state): return path + [state]
        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))

solution = bfs("123456708")
for s in solution: print(s[:3], s[3:6], s[6:])
