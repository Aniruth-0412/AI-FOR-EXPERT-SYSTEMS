def dfs_all_paths(graph, start, goal, path=None):
    if path is None:
        path = []

    path = path + [start]

    if start == goal:
        return [path]

    paths = []

    for neighbor in graph[start]:
        if neighbor not in path:
            new_paths = dfs_all_paths(graph, neighbor, goal, path)
            for p in new_paths:
                paths.append(p)

    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

print(dfs_all_paths(graph, 'A', 'D'))
