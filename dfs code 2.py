def dfs(a, b, path):
    if (a, b) in visited:
        return False
    visited.add((a, b))
    path.append((a, b))
    if a == target or b == target:
        print("Path:")
        for p in path:
            print(p)
        return True
    if (dfs(x, b, path) or
        dfs(a, y, path) or
        dfs(0, b, path) or
        dfs(a, 0, path) or
        dfs(a - min(a, y-b), b + min(a, y-b), path) or
        dfs(a + min(b, x-a), b - min(b, x-a), path)):
        return True
    path.pop()
    return False
x, y = 4, 3
target = 2
visited = set()
dfs(0, 0, [])
