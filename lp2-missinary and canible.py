#dfs
def is_valid_state(state):
    missionaries, cannibals, boat_side = state
    # Check if the state is valid (no more cannibals than missionaries on either side)
    return (missionaries >= 0 and missionaries <= 3 and
            cannibals >= 0 and cannibals <= 3 and
            (missionaries == 0 or missionaries >= cannibals) and
            (3 - missionaries == 0 or (3 - missionaries) >= (3 - cannibals)) and
            (boat_side == 0 or boat_side == 1))

def is_goal_state(state):
    return state == (0, 0, 1)  # Goal state: (0 missionaries, 0 cannibals, boat on the right bank)

def generate_successors(state):
    successors = []
    missionaries, cannibals, boat_side = state

    # Define possible actions
    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for action in actions:
        move_m, move_c = action

        # Check if the boat can move without violating constraints
        new_boat_side = 1 - boat_side  # Toggle boat side (0 to 1, 1 to 0)
        new_state = (
            missionaries - move_m if boat_side == 0 else missionaries + move_m,
            cannibals - move_c if boat_side == 0 else cannibals + move_c,
            new_boat_side
        )

        if is_valid_state(new_state):
            successors.append((new_state, action))

    return successors

def dfs(current_state, path, visited):
    if is_goal_state(current_state):
        return path + [current_state]

    visited.add(current_state)

    for successor, action in generate_successors(current_state):
        if successor not in visited:
            result = dfs(successor, path + [current_state, action], visited)
            if result:
                return result

    return None

def print_solution(solution):
    for step in solution:
        print(step)

# Initial state: (3 missionaries, 3 cannibals, boat on the left bank)
initial_state = (3, 3, 0)

# Run DFS to find a solution
visited_states = set()
solution = dfs(initial_state, [], visited_states)

# Print the solution
if solution:
    print("DFS: Solution found!")
    print_solution(solution)
else:
    print("DFS: No solution found.")


# bfs
