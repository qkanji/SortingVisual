import pygame

# Initialize Pygame
pygame.init()

# Create a 64x64 surface for the icon
icon_surface = pygame.Surface((64, 64), pygame.SRCALPHA)  # Add alpha channel for transparency
icon_surface.fill((0, 0, 0, 0))  # Transparent background

# Draw black rounded rectangle background
pygame.draw.rect(icon_surface, (0, 0, 0), (4, 4, 56, 56), border_radius=12)

# Draw some bars to represent sorting
colors = [(255, 0, 0), (0, 255, 0), (0, 191, 255)]  # Red, Green, Bright Blue (DodgerBlue)
bar_width = 8
spacing = 4
total_width = (bar_width * len(colors)) + (spacing * (len(colors) - 1))
start_x = (64 - total_width) // 2  # Center the bars horizontally

for i, color in enumerate(colors):
    height = 10 + (i * 15)  # Start lower and increase height difference
    pygame.draw.rect(icon_surface, color, 
                    (start_x + (i * (bar_width + spacing)), 
                     56 - height,  # Align to bottom
                     bar_width, 
                     height))

# Save the icon
pygame.image.save(icon_surface, "icon.png")
pygame.quit() 