from collections import deque

def water_jug_path(x, y, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            return path

        next_states = [
            (x, b), (a, y),
            (0, b), (a, 0),
            (a - min(a, y - b), b + min(a, y - b)),
            (a + min(b, x - a), b - min(b, x - a))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    return None



result = water_jug_path(4, 3, 2)
print(result)
