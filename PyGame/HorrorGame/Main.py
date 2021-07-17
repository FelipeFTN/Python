import pygame

# Initialize PyGame
pygame.init()

# Create the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dark Legend")
icon = pygame.image.load("images/Logo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/PlayerResized.png')
playerX = 370
playerY = 480

def player():
	screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	player()
	pygame.display.update()