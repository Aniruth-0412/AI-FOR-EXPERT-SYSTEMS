def water_jug_dfs(x, y, target, a=0, b=0, visited=None):
    if visited is None:
        visited = set()

    if (a, b) in visited:
        return False

    print(a, b)
    visited.add((a, b))

    if a == target or b == target:
        print("Target reached!")
        return True
    
    return (
        water_jug_dfs(x, y, target, x, b, visited) or
        water_jug_dfs(x, y, target, a, y, visited) or
        water_jug_dfs(x, y, target, 0, b, visited) or
        water_jug_dfs(x, y, target, a, 0, visited) or
        water_jug_dfs(x, y, target,
                      a - min(a, y - b),
                      b + min(a, y - b), visited) or
        water_jug_dfs(x, y, target,
                      a + min(b, x - a),
                      b - min(b, x - a), visited)
    )



water_jug_dfs(4, 3, 2)
