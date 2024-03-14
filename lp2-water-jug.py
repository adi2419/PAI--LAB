# # DFS function to solve the water jug problem
# from collections import deque

# def water_jug_dfs(capacity_a, capacity_b, target):
#     stack = [((0, 0), [])]  # Each stack element is a tuple containing current state and path
#     visited = set()

#     while stack:
#         (current_state, path) = stack.pop()
#         if current_state in visited:
#             continue

#         visited.add(current_state)

#         a, b = current_state

#         # Check if the target is reached
#         if a == target or b == target:
#             return path + [current_state]

#         # Pour water from jug A to jug B
#         stack.append(((0, b) if a == 0 else (max(0, a - (capacity_b - b)), min(b + a, capacity_b)), path + [current_state]))

#         # Pour water from jug B to jug A
#         stack.append(((min(a + b, capacity_a), 0) if b == 0 else (min(a + b, capacity_a), max(0, b - (capacity_a - a))), path + [current_state]))

#         # Fill jug A
#         stack.append(((capacity_a, b), path + [current_state]))

#         # Fill jug B
#         stack.append(((a, capacity_b), path + [current_state]))

#         # Empty jug A
#         stack.append(((0, b), path + [current_state]))

#         # Empty jug B
#         stack.append(((a, 0), path + [current_state]))

#     return False

# # Get user input for capacities and target
# capacity_a = int(input("Enter the capacity of jug A: "))
# capacity_b = int(input("Enter the capacity of jug B: "))
# target = int(input("Enter the target amount: "))

# # Call the water_jug_dfs function with user input
# result = water_jug_dfs(capacity_a, capacity_b, target)
# if result:
#     print("DFS: Can reach target")
#     print("Path Followed:")
#     for step in result:
#         print(step)
# else:
#     print("DFS: Cannot reach target")


#bfs
from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    queue = deque([(0, 0, [])])  # Each queue element is a tuple containing current state and path
    visited = set()

    while queue:
        a, b, path = queue.popleft()
        current_state = (a, b)

        if current_state in visited:
            continue

        visited.add(current_state)

        # Check if the target is reached
        if a == target or b == target:
            return path + [current_state]

        # Pour water from jug A to jug B
        new_state = (0, b) if a == 0 else (max(0, a - (capacity_b - b)), min(b + a, capacity_b))
        queue.append((new_state[0], new_state[1], path + [current_state]))

        # Pour water from jug B to jug A
        new_state = (min(a + b, capacity_a), 0) if b == 0 else (min(a + b, capacity_a), max(0, b - (capacity_a - a)))
        queue.append((new_state[0], new_state[1], path + [current_state]))

        # Fill jug A
        new_state = (capacity_a, b)
        queue.append((new_state[0], new_state[1], path + [current_state]))

        # Fill jug B
        new_state = (a, capacity_b)
        queue.append((new_state[0], new_state[1], path + [current_state]))

        # Empty jug A
        new_state = (0, b)
        queue.append((new_state[0], new_state[1], path + [current_state]))

        # Empty jug B
        new_state = (a, 0)
        queue.append((new_state[0], new_state[1], path + [current_state]))

    return False

def print_steps(path):
    for step in path:
        print(step)

# Get user input for capacities and target
capacity_a = int(input("Enter the capacity of jug A: "))
capacity_b = int(input("Enter the capacity of jug B: "))
target = int(input("Enter the target amount: "))

# Call the water_jug_bfs function with user input
result = water_jug_bfs(capacity_a, capacity_b, target)
if result:
    print("BFS: Can reach target")
    print("Path Followed:")
    print_steps(result)
else:
    print("BFS: Cannot reach target")
