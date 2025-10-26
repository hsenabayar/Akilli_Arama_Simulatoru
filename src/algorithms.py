from collections import deque
import heapq
from visualizer import draw_maze_step  

def bfs(maze, visualize=False):
    start, goal = maze.start, maze.goal
    queue = deque([start])
    visited = {start: None}
    expanded = 0
    path_so_far = []

    while queue:
        current = queue.popleft()
        expanded += 1

        if visualize:
            path_so_far.append(current)
            draw_maze_step(maze, path=path_so_far, current=current, algo_name="BFS")

        if current == goal:
            break
        for n in maze.neighbors(current):
            if n not in visited:
                visited[n] = current
                queue.append(n)

    path = []
    node = goal
    if node not in visited:
        print("BFS: Hedefe ulaşılamadı!")
    else:
        while node:
            path.append(node)
            node = visited[node]
        path.reverse()

    return path, expanded


def dfs(maze, visualize=False):
    start, goal = maze.start, maze.goal
    stack = [start]
    visited = {start: None}
    expanded = 0
    path_so_far = []

    while stack:
        current = stack.pop()
        expanded += 1

        if visualize:
            path_so_far.append(current)
            draw_maze_step(maze, path=path_so_far, current=current, algo_name="DFS")

        if current == goal:
            break
        for n in maze.neighbors(current):
            if n not in visited:
                visited[n] = current
                stack.append(n)

    path = []
    node = goal
    if node not in visited:
        print("DFS: Hedefe ulaşılamadı!")
    else:
        while node:
            path.append(node)
            node = visited[node]
        path.reverse()

    return path, expanded


def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar(maze, visualize=False):
    start, goal = maze.start, maze.goal
    heap = [(0, start)]
    visited = {start: None}
    cost_so_far = {start: 0}
    expanded = 0
    path_so_far = []

    while heap:
        _, current = heapq.heappop(heap)
        expanded += 1

        if visualize:
            path_so_far.append(current)
            draw_maze_step(maze, path=path_so_far, current=current, algo_name="A*")

        if current == goal:
            break
        for n in maze.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost + heuristic(goal, n)
                heapq.heappush(heap, (priority, n))
                visited[n] = current

    path = []
    node = goal
    if node not in visited:
        print("A*: Hedefe ulaşılamadı!")
    else:
        while node:
            path.append(node)
            node = visited[node]
        path.reverse()

    return path, expanded
