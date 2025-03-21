def detect_cycle(start, graph):
    slow, fast = start, start
    while fast in graph and graph[fast] in graph:
        slow = graph[slow]
        fast = graph[graph[fast]]
        if slow == fast:
            return True
    return False

def detect_intersecton(start_node, graph):
    visited = set()
    for start in start_node:
        node = start
        while node in graph:
            if node in visited:
                return True
            visited.add(node)
            node = graph[node]
    return False

def main():
    graph = {
        'a': 'b',
        'b': 'c',
        'x': 'y',
        'y': 'z'
    }
    start_sets = [['a', 'x'], ['a','b']]
    
    global_visited = set()
    
    results = []
    for s in start_sets:
        for st in s:
            if detect_cycle(st, graph):
                results.append("CYCLE")
                break
        else:
            if detect_intersecton(s, graph):
                results.append("INTERSECTION")
            elif any(node in global_visited for node in s):
                results.append("INTERSECTION")
            else:
                results.append("OK")
        global_visited.update(s)
    
    return results

print(main())
