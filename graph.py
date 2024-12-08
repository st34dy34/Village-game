import random
from entities import Village, Mountain

class Graph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.adjacency_list = self.build_graph()  # Initialize adjacency list

    def build_graph(self):
        adjacency_list = {}
        for y in range(self.height):
            for x in range(self.width):
                adjacency_list[(x, y)] = {
                    "neighbors": self.get_neighbors(x, y),
                    "type": "empty"  # Default type
                }
        return adjacency_list

    def get_neighbors(self, x, y):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append((nx, ny))
        return neighbors

    def set_random_entities(self):
        random_village_node = random.choice(list(self.adjacency_list.keys()))  # Pick a random tile
        self.adjacency_list[random_village_node]["type"] = "village"  # Set its type to "village"

        # Ensure the mountain is placed on a different node
        random_mountain_node = random.choice(list(self.adjacency_list.keys()))
        while random_mountain_node == random_village_node:
            random_mountain_node = random.choice(list(self.adjacency_list.keys()))
        self.adjacency_list[random_mountain_node]["type"] = "mountain"

        return Village(pos=random_village_node), Mountain(pos=random_mountain_node)
    

    