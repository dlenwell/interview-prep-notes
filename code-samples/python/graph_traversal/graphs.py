"""
collection of graph traversal examples
"""
from collections import deque


def all_paths_bfs(graph, start, finish):
    """
    path finder breadth first
    """
    visited = set()

    queue = deque([[start]])
    paths = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            if node == finish:
                paths.append(path)

            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(path + [neighbor])

    return paths


def shortest_path_finder_bfs(graph, start, finish):
    """
    path finder breadth first
    """
    visited = set()

    queue = deque([[start]])
    shortest = None

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            if node == finish:
                if shortest is None:
                    shortest = path
                elif len(shortest) > len(path):
                    shortest = path

            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(path + [neighbor])

    return shortest


def path_finder_bfs(graph, start, finish):
    """
    path finder breadth first
    """
    visited = set()

    queue = deque([[start]])

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            if node == finish:
                return path

            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(path + [neighbor])

    return None


def path_finder_dfs(graph, start, finish):
    """
    path finder depth first
    """
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        if node not in visited:
            if node == finish:
                return path

            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


def dfs_traverse(graph, start):
    """
    traverses graph depth first
    """
    visited = set()

    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            # do it
            print('Visiting: ', node)

            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return visited


def bfs_traverse(graph, start):
    """
    traverses graph breadth first
    """
    visited = set()

    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print('Visiting: ', node)
            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited


graph = {
    0: [1, 4, 5],
    1: [0, 2, 3, 4],
    2: [1, 3, 6],
    3: [1, 2, 4],
    4: [0, 1, 3, 5],
    5: [0, 4],
    6: [2],
}

if __name__ == "__main__":
    """
    exercise the above functions
    """
    print()
    print("DFS", dfs_traverse(graph, 0))
    print()
    print()
    print("BFS", bfs_traverse(graph, 0))
    print()
    print()
    print("Path Finder DFS", path_finder_dfs(graph, 5, 6))
    print()
    print()
    print("Path Finder BFS", path_finder_bfs(graph, 5, 6))
    print()
    print()
    print("Shortest Path Finder BFS", shortest_path_finder_bfs(graph, 4, 1))
    print()
    print()
    print("All Paths BFS", all_paths_bfs(graph, 5, 2))
