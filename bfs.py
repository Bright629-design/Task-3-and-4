# bfs.py — Breadth First Search (BFS)
# Explores nodes level by level (closest nodes first)
# Uses a QUEUE: First In, First Out (FIFO)

from collections import deque  # deque is an efficient queue

# The graph is represented as a dictionary.
# Each key is a node, and its value is a list of its neighbours.

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

def bfs(graph, start, goal):
    """
    Performs Breadth First Search from start node to goal node.
    """
    # We start with a path containing only the start node.
    queue = deque([[start]])

    # Keep track of nodes we have already visited
    visited = set()
    visited.add(start)

    print(f"\n Starting BFS from '{start}' to '{goal}'")
    print(f" Graph has {len(graph)} nodes: {list(graph.keys())}")
    print("-" * 45)

    while queue:
        # Take the first path from the front of the queue (FIFO)
        current_path = queue.popleft()

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
                queue.append(new_path)

    # If the queue empties and goal wasn't found
    print(f" Goal '{goal}' not reachable from '{start}'.")
    return None

# MAIN

if __name__ == "__main__":
    start_node = 'A'
    goal_node  = 'G'

    result = bfs(graph, start_node, goal_node)

    if result:
        print(f"\n Shortest path (BFS): {' -> '.join(result)}")
        print(f" Total steps: {len(result) - 1}")