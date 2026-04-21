from collections import deque

# Graph representing navigation map
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS - Shortest Path
def bfs(start, goal):
    visited = []
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path

            visited.append(node)

# DFS - Depth Search
def dfs(start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for node in graph[start]:
        if node not in path:
            new_path = dfs(node, goal, path)
            if new_path:
                return new_path

# Run program
# Smart Navigation using BFS and DFS
start = 'A'
goal = 'F'

print("BFS Path:", bfs(start, goal))
print("DFS Path:", dfs(start, goal))
Added BFS and DFS Smart Navigation system
Added comments
