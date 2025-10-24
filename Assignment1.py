from collections import deque

def bfs_find_path(graph, start, goal):
    # The queue now only needs to store the nodes to visit
    queue = deque([start])
    visited = {start}
    # This dictionary will store the path: {child_node: parent_node}
    parents = {start: None}

    while queue:
        vertex = queue.popleft()

        if vertex == goal:
            path = []

            while vertex is not None:
                path.append(vertex)
                vertex = parents[vertex]

            return path[::-1]

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                queue.append(neighbor)

    return []

graph = {
    'Tottenham Court Road': {'Oxford Circus': 9, 'Goodge Street': 7, 'Holborn': 10},
    'Oxford Circus': {'Tottenham Court Road': 9, 'Regent\'s Park': 15, 'Goodge Street': 18},
    'Regent\'s Park': {'Oxford Circus': 15, 'Baker Street': 10},
    'Baker Street': {'Regent\'s Park': 10, 'Great Portland Street': 13},
    'Great Portland Street': {'Baker Street': 13, 'Euston Square': 10},
    'Euston Square': {'Great Portland Street': 10, 'King\'s Cross St. Pancras': 15},
    'Goodge Street': {'Tottenham Court Road': 7, 'Oxford Circus': 18, 'Warren Street': 7},
    'Warren Street': {'Goodge Street': 7, 'Euston': 9, 'King\'s Cross St. Pancras': 9},
    'Euston': {'Warren Street': 9, 'King\'s Cross St. Pancras': 2},
    'Holborn': {'Tottenham Court Road': 10, 'Russell Square': 9},
    'Russell Square': {'Holborn': 9, 'King\'s Cross St. Pancras': 1},
    'King\'s Cross St. Pancras': {'Warren Street': 9, 'Euston': 2, 'Euston Square': 15, 'Russell Square': 1}
}

start_node = 'Tottenham Court Road'
goal_node = 'King\'s Cross St. Pancras'
path = bfs_find_path(graph, start_node, goal_node)
if path:
    # The depth is the number of connections, which is len(path) - 1
    depth = len(path) - 1
    print("Start Node:", start_node)
    print("Goal Node:", goal_node)
    print("Shortest Path:", " -> ".join(path))
    print("Depth:", depth)
else:
    print(f"No path found from {start_node} to {goal_node}.")