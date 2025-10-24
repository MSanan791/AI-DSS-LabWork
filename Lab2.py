un_graph = {
    1: [2,5],
    2:[1,5,3],
    3:[4,2],
    4:[3,5,6],
    5:[1,2,4],
    6:[4]
}
print("adjacency list representation of the Graph:")
for edge in un_graph:
    print(f"{edge} --> {un_graph[edge]}")
#%%
directed_graph = {
    "A":["B"],
    'B':['C','D','E'],
    'C':['E'],
    'E':['F'],
    'G':['D']
}

print("Adjacency list representation of the directed graph:")
for edge in directed_graph:
    print(f"{edge} --> {directed_graph[edge]}")

#%%
def path_find(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or path == []:
            new_paths = path_find(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths
#%%
def path_find_any(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = path_find_any(graph, node, end, path)
            if new_path:
                return new_path
    return None
#%%
print("any path from node 1 to 6 in the undirected graph:")
any_path = path_find_any(un_graph, 1, 6)
print(any_path)

print("All paths from node 1 to 6 in the undirected graph:")

all_paths = path_find(un_graph, 6, 1)
print(all_paths)

#%%
print("any path from node A to F in the directed graph:")
any_path = path_find_any(directed_graph, 'A', 'F')
print(any_path)

print("All paths from node A to F in the directed graph:")
all_paths = path_find(directed_graph, 'A', 'F')
print(all_paths)
#%%
def path_find_range(graph, start, end, max_depth, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    if max_depth <= 0:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or path == []:
            new_paths = path_find_range(graph, node, end, max_depth-1, path)
            for p in new_paths:
                paths.append(p)
    return paths


#%%
## TASK 2 4x4 grid graph 4-connectivity, all possible paths from (0,0) to (3,3)

image = [[100, 110, 120, 130],[140,145,45,135],[220,10,165,80],[180,200,191,118]]
rows = len(image)
cols = len(image[0])
grid_graph = {}
for r in range(rows):
    for c in range(cols):
        neighbors = []
        if r > 0:
            neighbors.append((r-1,c))
        if r < rows - 1:
            neighbors.append((r+1,c))
        if c > 0:
            neighbors.append((r,c-1))
        if c < cols - 1:
            neighbors.append((r,c+1))
        grid_graph[(r,c)] = neighbors
print("Adjacency list representation of the 4x4 grid graph:")
for edge in grid_graph:
    print(f"{edge} --> {grid_graph[edge]}")
## find all possible paths between intensity 100 and 118
for edge in grid_graph:
    if image[edge[0]][edge[1]] == 100:
        start = edge
    if image[edge[0]][edge[1]] == 118:
        end = edge
all_paths = path_find(grid_graph, start, end)
print(f"All possible paths from {start} to {end}:")
print(all_paths)
print(len(all_paths))

#%%
## Shortest cost path from 100 to 118
def cost_path_find(graph, image, start, end, path=[], cost=0):
    path = path + [start]
    if start == end:
        return [(path, cost)]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or path == []:
            new_cost = cost + abs(image[start[0]][start[1]] - image[node[0]][node[1]])
            new_paths = cost_path_find(graph, image, node, end, path, new_cost)
            for p in new_paths:
                paths.append(p)
    return paths
all_cost_paths = cost_path_find(grid_graph, image, start, end)
min_cost = float('inf')
min_cost_path = None
for p, c in all_cost_paths:
    if c < min_cost:
        min_cost = c
        min_cost_path = p
print(f"The shortest cost path from {start} to {end} is {min_cost_path} with cost {min_cost}")

#%%
## 5x5 adjacency matrix representation of a graph
import numpy as np
