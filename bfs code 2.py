def bfs():
    q = [((0, 0), [])]
    visited = set()
    while q:
        (a, b), path = q.pop(0)
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]
        if a == target or b == target:
            print("Path:")
            for p in path:
                print(p)
            return
        q.append(((x, b), path))
        q.append(((a, y), path))
        q.append(((0, b), path))
        q.append(((a, 0), path))
        q.append(((a - min(a, y-b), b + min(a, y-b)), path))
        q.append(((a + min(b, x-a), b - min(b, x-a)), path))
x, y = 4, 3
target = 2
bfs()
