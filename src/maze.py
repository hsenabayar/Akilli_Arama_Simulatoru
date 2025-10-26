class Maze:
    def __init__(self, file_path):
        self.grid = []
        self.start = None
        self.goal = None
        
        with open(file_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                row = line.strip().split()
                self.grid.append(row)
                for j, val in enumerate(row):
                    if val == "S":
                        self.start = (i, j)
                    elif val == "G":
                        self.goal = (i, j)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
    
    def is_valid(self, pos):
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != "#"
    
    def neighbors(self, pos):
        r, c = pos
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if self.is_valid((nr, nc)):
                yield (nr, nc)
