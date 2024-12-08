import pygame
import sys
from graph import Graph

def visualize_graph(graph, cell_size, padding):
    adjacency_list = graph.build_graph()
    for node, neighbors in adjacency_list.items():
            x, y = node
            # Convert graph coordinates to pixel positions
            node_pos = (x * cell_size + padding, y * cell_size + padding)
            pygame.draw.rect(screen, (1, 100, 32), (node_pos[0], node_pos[1], RECT_WIDTH, RECT_HEIGHT))

# /// INIT ////

pygame.init()
width, height = 800, 600  
screen = pygame.display.set_mode((width, height))  
pygame.display.set_caption("My Pygame Window") 
clock = pygame.time.Clock()
graph1 = Graph(width= 10, height=10)

# /// VARIABLES ///
RECT_WIDTH = 48
RECT_HEIGHT = 48
cell_size = 50
padding = 50
# /// MAIN ////

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    
    screen.fill((173, 216, 230)) 
    visualize_graph(graph1, cell_size=cell_size,padding=padding)
    pygame.display.flip()
    clock.tick(60)

# //// QUIT /////

pygame.quit()
sys.exit()
