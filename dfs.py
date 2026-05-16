# dfs.py — Depth First Search (DFS)
# Explores as deep as possible before backtracking
# Uses a STACK: Last In, First Out (LIFO)
# Same graph as BFS so you can compare the two search paths.
# Each key is a node, value is a list of its neighbours.

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

def dfs(graph, start, goal):
    """
    Performs Depth First Search from start node to goal node.
    """

    # The stack holds paths (not just nodes).
    # We start with a path containing only the start node.
    stack = [[start]]

    # We keep track of nodes we have already visited
    visited = set()
    visited.add(start)

    print(f"\n Starting DFS from '{start}' to '{goal}'")
    print(f" Graph has {len(graph)} nodes: {list(graph.keys())}")
    print("-" * 45)

    while stack:
        # Take the last path from the top of the stack (LIFO)
        current_path = stack.pop()

        # The current node is the last node in this path
        current_node = current_path[-1]

        print(f" Visiting: {current_node}  |  Path so far: {' -> '.join(current_path)}")

        # Check if we have reached the goal
        if current_node == goal:
            print("-" * 45)
            print(f" Goal '{goal}' found!")
            return current_path

        # Explore all neighbours of the current node
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)

                # Build a new path by extending the current path
                new_path = current_path + [neighbour]
                stack.append(new_path)

    print(f" Goal '{goal}' not reachable from '{start}'.")
    return None

# MAIN — Run the search and show the result

if __name__ == "__main__":
    start_node = 'A'
    goal_node  = 'G'

    result = dfs(graph, start_node, goal_node)

    if result:
        print(f"\n DFS path found: {' -> '.join(result)}")
        print(f" Total steps: {len(result) - 1}")