def dfs(a, b):
    if (a, b) in visited:
        return
    visited.add((a, b))
    print(a, b)
    if a == target or b == target:
        print("Target Reached")
        return
    dfs(x, b)
    dfs(a, y)   
    dfs(0, b)   
    dfs(a, 0)   
    dfs(a - min(a, y-b), b + min(a, y-b))  
    dfs(a + min(b, x-a), b - min(b, x-a))  
x, y = 4, 3
target = 2
visited = set()
dfs(0, 0)
