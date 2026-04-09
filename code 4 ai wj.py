from collections import deque

def water_jug_bfs(x, y, target):
    visited = set()
    queue = deque([(0, 0)])  
    a, b = queue.popleft()

        if (a, b) in visited:
            continue

        print(a, b)
        visited.add((a, b))

        
        if a == target or b == target:
            print("Target reached!")
            return True

        
        next_states = [
            (x, b),      
            (a, y),      
            (0, b),      
            (a, 0),      
            (a - min(a, y - b), b + min(a, y - b)),  
            (a + min(b, x - a), b - min(b, x - a))   
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    return False



water_jug_bfs(4, 3, 2)
