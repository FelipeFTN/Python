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
playerDirectionX = 0
playerDirectionY = 0

def player(x, y):
	screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerDirectionX = -0.05
			if event.key == pygame.K_RIGHT:
				playerDirectionX = 0.05
			if event.key == pygame.K_UP:
				playerDirectionY = -0.05
			if event.key == pygame.K_DOWN:
				playerDirectionY = 0.05

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
				playerDirectionX = 0
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				playerDirectionY = 0

	screen.fill((0, 0, 0))

	playerX += playerDirectionX
	playerY += playerDirectionY
	player(playerX, playerY)
	pygame.display.update()