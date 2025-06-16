import random
import time
from threading import Thread
import pygame
from SortingVisualizer import SortingVisualizer

surf = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Sorting Algorithm Visualizer")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

x = 0
y = 0

number_of_items = 50

left_graph = SortingVisualizer(surf, 20, 20, 460, 460, list(range(1, number_of_items + 1)), number_of_items, number_of_items)
right_graph = SortingVisualizer(surf, 520, 20, 460, 460, list(range(1, number_of_items + 1)), number_of_items, number_of_items)
random.shuffle(left_graph.arr)
for i in range(number_of_items):
    right_graph.arr[i] = left_graph.arr[i]

left_thread = Thread(target=left_graph.insertion_sort)
right_thread = Thread(target=right_graph.merge_sort)

conti = True
while conti:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                conti = False
                break

left_thread.start()
right_thread.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            left_graph.kill_process()
            left_thread.join(3)
            right_graph.kill_process()
            right_thread.join(3)
            quit()

    pygame.draw.rect(surf, (0,0,0), (0, 0, 1000, 500))  # Draw background
    left_graph.display()
    right_graph.display()
    pygame.display.flip()
    time.sleep(0.01)
