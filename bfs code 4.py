def bfs():
    q = [(0, 0, 0)]  
    visited = set()
    while q:
        a, b, step = q.pop(0)
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b, "Step:", step)
        if a == target or b == target:
            print("Target Reached in", step, "steps")
            return
        q.append((x, b, step+1))
        q.append((a, y, step+1))
        q.append((0, b, step+1))
        q.append((a, 0, step+1))
        q.append((a - min(a, y-b), b + min(a, y-b), step+1))
        q.append((a + min(b, x-a), b - min(b, x-a), step+1))
x, y = 4, 3
target = 2
bfs()
