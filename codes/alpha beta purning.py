def alphabeta(depth, node, maxT, values, alpha, beta):
    if depth == 3: return values[node]
    if maxT:
        val = float('-inf')
        for i in range(2):
            val = max(val, alphabeta(depth+1, node*2+i, False, values, alpha, beta))
            alpha = max(alpha, val)
            if beta <= alpha: break
        return val
    else:
        val = float('inf')
        for i in range(2):
            val = min(val, alphabeta(depth+1, node*2+i, True, values, alpha, beta))
            beta = min(beta, val)
            if beta <= alpha: break
        return val

values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Alpha-Beta Result:", alphabeta(0, 0, True, values, float('-inf'), float('inf')))
