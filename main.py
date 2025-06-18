import random
import time
from threading import Thread
import pygame
from SortingVisualizer import SortingVisualizer

screen_w = 1200
screen_h = 600

graphs_wide = 4
graphs_high = 2

padding = 10

graph_width = screen_w / graphs_wide - 2 * padding
graphs_height = screen_h / graphs_high - 2 * padding

surf = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Sorting Algorithm Visualizer")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

x = 0
y = 0

number_of_items = 50

graphs = []
for y_multi in range(graphs_high):
    for x_multi in range(graphs_wide):
        origin_x = screen_w / graphs_wide * x_multi + padding
        origin_y = screen_h / graphs_high * y_multi + padding
        graph = SortingVisualizer(surf, origin_x, origin_y, graph_width, graphs_height, list(range(1, number_of_items + 1)), number_of_items, number_of_items)
        graphs.append(graph)

random.shuffle(graphs[0].arr)

for j in range(number_of_items):
    for i in range(1, graphs_high * graphs_wide):
        graphs[i].arr[j] = graphs[0].arr[j]

for i in range(graphs_high * graphs_wide):
    graphs[i].display()

threads = []
threads.append(Thread(target=graphs[0].bubble_sort))
threads.append(Thread(target=graphs[1].selection_sort))
threads.append(Thread(target=graphs[2].insertion_sort))
threads.append(Thread(target=graphs[3].merge_sort))
threads.append(Thread(target=graphs[4].quick_sort))
threads.append(Thread(target=graphs[5].radix_sort))
threads.append(Thread(target=graphs[6].counting_sort))
threads.append(Thread(target=graphs[7].heap_sort))

conti = True
while conti:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                conti = False
                break

for thread in threads:
    thread.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for graph in graphs:
                graph.kill_process()
            for thread in threads:
                thread.join(3)
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                for graph in graphs:
                    graph.kill_process()
                for thread in threads:
                    thread.join(3)
                quit()

    pygame.draw.rect(surf, (0,0,0), (0, 0, 1000, 500))  # Draw background
    for graph in graphs:
        graph.display()
    pygame.display.flip()
    time.sleep(0.01)
