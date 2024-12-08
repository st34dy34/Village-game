import pprint

class Graph:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def build_graph(self):
        adjacency_list = {}
        for y in range(self.height):  # Loop through rows
            for x in range(self.width):  # Loop through columns
                adjacency_list[(x, y)] = self.get_neighbors(x, y)
        return adjacency_list
    
    def get_neighbors(self,x,y):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                 neighbors.append((nx, ny))
        return neighbors

    def __str__(self):
        grid = ""
        for y in range(self.height):  # Loop through rows
            for x in range(self.width):  # Loop through columns
                grid += f"({x},{y}) "  # Add each cell's coordinates
            grid += "\n"  # New line at the end of each row
        return grid
    