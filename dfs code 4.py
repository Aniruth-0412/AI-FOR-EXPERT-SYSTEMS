def dfs(a, b, depth):
    if depth > limit or (a, b) in visited:
        return
    visited.add((a, b))
    print(a, b, "Depth:", depth)
    if a == target or b == target:
        print("Target Found")
        return
    dfs(x, b, depth+1)
    dfs(a, y, depth+1)
    dfs(0, b, depth+1)
    dfs(a, 0, depth+1)
    dfs(a - min(a, y-b), b + min(a, y-b), depth+1)
    dfs(a + min(b, x-a), b - min(b, x-a), depth+1)
x, y = 4, 3
target = 2
limit = 10
visited = set()
dfs(0, 0, 0)
