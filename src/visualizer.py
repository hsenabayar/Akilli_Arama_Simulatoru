import matplotlib.pyplot as plt
import numpy as np

def draw_maze(maze, path=None, algo_name="Path"):
    """Son yolu gösterir (kırmızı çizgiyle), kullanıcı kapatınca diğerine geçer"""
    rows, cols = maze.rows, maze.cols
    img = np.zeros((rows, cols, 3))
    for r in range(rows):
        for c in range(len(maze.grid[r])):
            if maze.grid[r][c] == "#":
                img[r, c] = [0, 0, 0]
            else:
                img[r, c] = [1, 1, 1]

    plt.imshow(img, origin='upper')

    sr, sc = maze.start
    gr, gc = maze.goal
    plt.scatter([sc], [sr], c='green', s=200, label='Start')
    plt.scatter([gc], [gr], c='blue', s=200, label='Goal')

    if path:
        pr, pc = zip(*path)
        plt.plot(pc, pr, color='red', linewidth=2, label='Path')

    plt.title(f"{algo_name} | Start: {maze.start} | Goal: {maze.goal}")
    plt.xticks([])
    plt.yticks([])
    plt.legend(loc='upper right')

    plt.show(block=True)
    plt.close('all')




def draw_maze_step(maze, path=None, current=None, visited=None, algo_name="Path"):
    """Adım adım görselleştirme (çizgi yerine noktalarla)"""
    rows, cols = maze.rows, maze.cols
    img = np.zeros((rows, cols, 3))
    for r in range(rows):
        for c in range(len(maze.grid[r])):  
            if maze.grid[r][c] == "#":
                img[r, c] = [0, 0, 0]
            else:
                img[r, c] = [1, 1, 1]
        plt.imshow(img, origin='upper')

    sr, sc = maze.start
    gr, gc = maze.goal
    plt.scatter([sc], [sr], c='green', s=200, label='Start')
    plt.scatter([gc], [gr], c='blue', s=200, label='Goal')

    
    if visited:
        for (vr, vc) in visited:
            plt.scatter([vc], [vr], c='orange', s=30, alpha=0.6)

    # Genişletilen düğüm
    if current:
        plt.scatter([current[1]], [current[0]], c='yellow', s=80)


    if path:
        pr, pc = zip(*path)
        plt.scatter(pc, pr, c='red', s=40, label='Path')

    plt.title(f"{algo_name} | Start: {maze.start} | Goal: {maze.goal}")
    plt.xticks([])
    plt.yticks([])
    plt.legend(loc='upper right')
    plt.pause(0.05)
    plt.clf()
