# Import PyGame
import pygame

# Initialize PyGame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Dark Legend")
icon = pygame.image.load('images/logo.png')
pygame.display.set_icon(icon)

# Player
playerIcon = pygame.image.load('images/Player.png')
playerX = 370
playerY = 480
playerDX = 0
playerDY = 0

def player(x, y):
	screen.blit(playerIcon, (x, y))

# Game Loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# Screen Color
	screen.fill((255, 255, 255))
	
	player(playerX, playerY)
	pygame.display.update()