Pseudocode:
start from state (0, 0)
create an empty queue and visited set
add (0, 0) to queue
while queue is not empty:
       take first state (a, b) from queue
    if this state is already visited:
        skip to next
    mark (a, b) as visited
    display the state (a, b)
    if jug1 or jug2 has target:
        stop the process
    perform all possible operations:
        fill jug1 completely → (x, b)
        fill jug2 completely → (a, y)
        empty jug1 → (0, b)
        empty jug2 → (a, 0)
        pour jug1 to jug2
        pour jug2 to jug1
    add all new states to queue

    Pseudocode:
start from state (0, 0) with empty path
create queue and visited set
add ((0, 0), empty path) to queue
while queue is not empty:
    take first element → (state, path)
    let state be (a, b)
    if (a, b) already visited:
        skip to next
    mark (a, b) as visited
    add (a, b) to path
    if a or b equals target:
        print the path
        stop
    perform all operations and add to queue with updated path:
        fill jug1 → (x, b)
        fill jug2 → (a, y)
        empty jug1 → (0, b)
        empty jug2 → (a, 0)
        pour jug1 to jug2
        pour jug2 to jug1

        Pseudocode:
start from state (0, 0)
create a list as queue and visited set
set index i = 0
while i is less than length of queue:
    take state (a, b) from queue using index i
    increase i by 1
    if (a, b) already visited:
        skip to next
    mark (a, b) as visited
    display (a, b)
    if a or b equals target:
        print target found
        stop
    perform all operations and add to queue:
        fill jug1 → (x, b)
        fill jug2 → (a, y)
        empty jug1 → (0, b)
        empty jug2 → (a, 0)
        pour jug1 to jug2
        pour jug2 to jug1

        
Pseudocode:
start from state (0, 0) with step = 0
create queue and visited set
add (0, 0, 0) to queue
while queue is not empty:
    take first element (a, b, step)
    if (a, b) already visited:
        skip to next
    mark (a, b) as visited
    display (a, b) and step
    if a or b equals target:
        print target reached with steps
        stop
    perform all operations and add to queue with step + 1:
        fill jug1 → (x, b, step+1)
        fill jug2 → (a, y, step+1)
        empty jug1 → (0, b, step+1)
        empty jug2 → (a, 0, step+1)
        pour jug1 to jug2
        pour jug2 to jug1

        Pseudocode:
start from state (0, 0)
create an empty visited set
define dfs(a, b):
    if (a, b) is already visited:
        return
    mark (a, b) as visited
    print the state (a, b)
    if a or b is equal to target:
        print target reached
        stop the program
    try all possible operations:
        fill jug1 completely → call dfs(x, b)
        fill jug2 completely → call dfs(a, y)
        empty jug1 → call dfs(0, b)
        empty jug2 → call dfs(a, 0)
        pour water from jug1 to jug2 → call dfs(new state)
        pour water from jug2 to jug1 → call dfs(new state)
call dfs(0, 0)

Pseudocode:
start from state (0, 0) with empty path
create an empty visited set
define dfs(a, b, path):
    if (a, b) is already visited:
        return false
    mark (a, b) as visited
    add (a, b) to path
    if a or b is equal to target:
        print the path
        return true
    try all possible operations:
        fill jug1 → dfs(x, b, path)
        fill jug2 → dfs(a, y, path)
        empty jug1 → dfs(0, b, path)
        empty jug2 → dfs(a, 0, path)
        pour jug1 to jug2 → dfs(new state, path)
        pour jug2 to jug1 → dfs(new state, path)
    if any operation returns true:
        return true
    remove last state from path
    return false
call dfs(0, 0, empty path)

Pseudocode:
start from state (0, 0) with empty path
create queue and visited set
add ((0, 0), empty path) to queue
while queue is not empty:
    take first element (state, path)
    let state be (a, b)
    if (a, b) is already visited:
        continue
    mark (a, b) as visited
    create new path by adding (a, b)
    if a or b is equal to target:
        print the path
        stop
    perform all operations and add to queue with updated path:
        fill jug1 → ((x, b), path)
        fill jug2 → ((a, y), path)
        empty jug1 → ((0, b), path)
        empty jug2 → ((a, 0), path)
        pour jug1 to jug2 → ((new state), path)
        pour jug2 to jug1 → ((new state), path)

        Pseudocode:
start from state (0, 0) with depth = 0
create an empty visited set
set a maximum depth limit
define dfs(a, b, depth):
    if depth is greater than limit or (a, b) is already visited:
        return
    mark (a, b) as visited
    print (a, b) with depth
    if a or b is equal to target:
        print target found
        stop
    try all possible operations with increased depth:
        fill jug1 → dfs(x, b, depth + 1)
        fill jug2 → dfs(a, y, depth + 1)
        empty jug1 → dfs(0, b, depth + 1)
        empty jug2 → dfs(a, 0, depth + 1)
        pour jug1 to jug2 → dfs(new state, depth + 1)
        pour jug2 to jug1 → dfs(new state, depth + 1)
call dfs(0, 0, 0)



