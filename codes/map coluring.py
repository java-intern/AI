colors = ['Red', 'Green', 'Blue']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

def is_valid(node, color, assignment):
    return all(assignment.get(n) != color for n in neighbors[node])

def csp(assignment={}):
    if len(assignment) == len(neighbors):
        print(assignment)
        return
    node = [n for n in neighbors if n not in assignment][0]
    for color in colors:
        if is_valid(node, color, assignment):
            csp({**assignment, node: color})

csp()
