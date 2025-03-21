import sys

graph = {}
start_sets = []

reading_graph = True

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    # Identify if the graph input has ended
    if line == '#':
        reading_graph = False
        continue
    
    if reading_graph:
        # Handle '->' format for graph input
        if '->' in line:
            u, v = line.split('->')
            graph[u.strip()] = v.strip()
        else:
            print(f"Invalid graph input: {line}")
    else:
        # Handle start sets separated by commas
        start_sets.append(line.split(','))

def detect_cycle(start, graph):
    slow, fast = start, start
    while fast in graph and graph[fast] in graph:
        slow = graph[slow]
        fast = graph[graph[fast]]
        if slow == fast:
            return True
    return False

def detect_intersection(start_node, graph):
    visited = set()
    for start in start_node:
        node = start
        while node in graph:
            if node in visited:
                return True
            visited.add(node)
            node = graph[node]
    return False

global_visited = set()
results = []

# Process each start set
for s in start_sets:
    for st in s:
        if detect_cycle(st, graph):
            results.append("CYCLE")
            break
    else:
        if detect_intersection(s, graph) or any(node in global_visited for node in s):
            results.append("INTERSECTION")
        else:
            results.append("OK")
    global_visited.update(s)

print("\n".join(results))
