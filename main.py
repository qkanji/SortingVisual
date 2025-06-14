import pygame

surf = pygame.display.set_mode((1000, 500))

x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()

    pygame.draw.rect(surf, "black", (0, 0, 1000, 500))
    pygame.draw.circle(surf, "orange2", (x, y), 25)
    pygame.display.flip()
