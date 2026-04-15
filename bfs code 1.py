def bfs():
    q = [(0, 0)]
    visited = set()
    while q:
        a, b = q.pop(0)
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)
        if a == target or b == target:
            print("Target Reached")
            return
        q.append((x, b))   
        q.append((a, y))   
        q.append((0, b))
        q.append((a, 0))   
        q.append((a - min(a, y-b), b + min(a, y-b)))  
        q.append((a + min(b, x-a), b - min(b, x-a)))  
x, y = 4, 3
target = 2
bfs()
