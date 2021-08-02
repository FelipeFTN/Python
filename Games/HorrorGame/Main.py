# Imports
import pygame

# Initialize pygame
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("Horror Game")
#icon = pygame.image.load('Horror.png')
#pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False