import pygame
import sys
from collections import deque
from graph import Graph

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 50
PADDING = 50
BACKGROUND_COLOR = (173, 216, 230)  # Light blue
NODE_COLOR = (1, 100, 32)  # Green for normal nodes
SELECTED_NODE_COLOR = (255, 0, 0)  # Red for selected nodes
GRID_LINE_GAP = 2  # Gap for gridlines

# Initialize Pygame
def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Graph Visualization")
    return screen, pygame.time.Clock()

# Convert graph node to screen coordinates
def node_to_pixel(node, cell_size, padding):
    x, y = node
    return x * cell_size + padding, y * cell_size + padding

# Visualize the graph
def draw_graph(screen, graph, selected_nodes, cell_size, padding):
    for node, properties in graph.adjacency_list.items():
        node_pos = node_to_pixel(node, cell_size, padding)
        if node in selected_nodes:
            color = SELECTED_NODE_COLOR  # Red for selected nodes
        elif properties["type"] == "village":
            color = (255, 255, 0)  # Yellow for villages
        elif properties["type"] == "mountain":
            color = (104, 104, 104)  # Gray for mountains
        else:
            color = NODE_COLOR  # Green for normal nodes
        pygame.draw.rect(
            screen, color, (node_pos[0], node_pos[1], cell_size - GRID_LINE_GAP, cell_size - GRID_LINE_GAP)
        )

# Get the graph node from mouse position
def get_node_from_mouse(pos, cell_size, padding):
    mouse_x, mouse_y = pos
    node_x = (mouse_x - padding) // cell_size
    node_y = (mouse_y - padding) // cell_size
    return node_x, node_y



# Main game loop
def main():
    # Initialize Pygame and graph
    screen, clock = initialize_pygame()
    graph = Graph(width=10, height=10)

    # Place random entities
    village, mountain = graph.set_random_entities()
    print(f"Village set at: {village.pos}")  # Debugging output
    print(f"Mountain set at: {mountain.pos}")  # Debugging output
    selected_nodes = set()  # Track selected nodes
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                clicked_node = get_node_from_mouse(mouse_pos, CELL_SIZE, PADDING)
                if clicked_node in graph.adjacency_list:
                    # Toggle selection state
                    if clicked_node in selected_nodes:
                        selected_nodes.remove(clicked_node)
                    else:
                        selected_nodes.add(clicked_node)

        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        draw_graph(screen, graph, selected_nodes, CELL_SIZE, PADDING)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
