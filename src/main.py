from maze import Maze
from algorithms import bfs, dfs, astar
from visualizer import draw_maze, draw_maze_step
import csv
import time

# Test senaryoları listesi: (maze_dosya_yolu, başlangıç_noktası, hedef_noktası)
# Bu yapı, hem farklı labirentleri hem de aynı labirentteki farklı noktaları kapsar.
test_scenarios = [
    # 1. Senaryo (Mevcut labirentte kısa yol):
    ("data/maze1.txt", (0, 0), (6, 4)), 
    
    # 2. Senaryo (Yeni, karmaşık labirent)
    ("data/maze2.txt", (1, 1), (9, 9)),
]

results = []

# Tüm test senaryolarını tek bir döngüde çalıştırın
for maze_file, start, goal in test_scenarios: # Eğer senaryo yapısını değiştirdiyseniz
    
    maze = Maze(maze_file)
    maze.start, maze.goal = start, goal
    
    for name, func in {"BFS": bfs, "DFS": dfs, "A*": astar}.items():
        
        # BURADAN İTİBAREN TRY...EXCEPT BLOĞUNU EKLEYİN
        try:
            start_time = time.time()
            
            # Adım adım görselleştirme
            path, expanded = func(maze, visualize=True)
            elapsed = (time.time() - start_time) * 1000  # ms
        
            draw_maze(maze, path, algo_name=f"{name} | Start:{start} Goal:{goal}")

            print(f"{name} - Maze: {maze_file}, Start: {start}, Goal: {goal}, Path Length: {len(path)}, Expanded: {expanded}, Time(ms): {elapsed:.2f}")
            results.append([name, start, goal, len(path), expanded, elapsed])
        
        except Exception as e:
            # Hata oluşursa, asıl hatayı yazdırın
            print(f"\n!!!!!!!!!!!!!! HATA !!!!!!!!!!!!!!")
            print(f"[{name}] algoritması {maze_file} için çalışırken bir hata oluştu: {e}")
            print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            # Yeni Hali (Algorithm sütununa maze_file bilgisini ekler):
            results.append([f"{name} ({maze_file.split('/')[-1]})", start, goal, 0, 0, 0])
            continue # Hata oluşan senaryoyu atla ve bir sonrakine geç


# CSV kaydı ve tablo başlıklarını güncelleyin
with open("results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Algorithm","Start","Goal","Path Length","Expanded Nodes","Time(ms)"]) # Başlıklar değişmedi
    writer.writerows(results)

# Terminalde tablo başlıklarını güncelleyin
from tabulate import tabulate

headers = ["Algorithm","Start","Goal","Path Length","Expanded Nodes","Time(ms)"]
print("\n=== Algoritma Sonuçları Tablosu ===\n")
print(tabulate(results, headers=headers, tablefmt="grid"))