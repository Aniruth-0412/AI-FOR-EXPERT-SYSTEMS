def bfs():
    q = [(0, 0)]
    visited = set()
    i = 0  
    while i < len(q):
        a, b = q[i]
        i += 1
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)
        if a == target or b == target:
            print("Target Found")
            return
        q += [
            (x, b), (a, y),
            (0, b), (a, 0),
            (a - min(a, y-b), b + min(a, y-b)),
            (a + min(b, x-a), b - min(b, x-a))
        ]
x, y = 5, 3
target = 4
bfs()
