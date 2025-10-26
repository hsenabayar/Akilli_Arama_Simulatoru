from maze import Maze
from algorithms import bfs, dfs, astar
from visualizer import draw_maze, draw_maze_step
import csv
import time

maze_files = ["data/maze1.txt"]
start_goal_list = [((0,0),(6,4))]

results = []

for maze_file in maze_files:
    maze = Maze(maze_file)
    for start, goal in start_goal_list:
        maze.start, maze.goal = start, goal
        for name, func in {"BFS": bfs, "DFS": dfs, "A*": astar}.items():
            start_time = time.time()
            # Adım adım görselleştirme
            path, expanded = func(maze, visualize=True)
            elapsed = (time.time() - start_time) * 1000  # ms

    
            draw_maze(maze, path, algo_name=f"{name} | Start:{start} Goal:{goal}")

            print(f"{name} - Start: {start}, Goal: {goal}, Path Length: {len(path)}, Expanded: {expanded}, Time(ms): {elapsed:.2f}")
            results.append([name, start, goal, len(path), expanded, elapsed])

# CSV kaydı
with open("results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Algorithm","Start","Goal","Path Length","Expanded Nodes","Time(ms)"])
    writer.writerows(results)

# -----------------------------
# Terminalde tablo 
# -----------------------------
from tabulate import tabulate

headers = ["Algorithm","Start","Goal","Path Length","Expanded Nodes","Time(ms)"]
print("\n=== Algoritma Sonuçları Tablosu ===\n")
print(tabulate(results, headers=headers, tablefmt="grid"))
