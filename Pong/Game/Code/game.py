import pygame
from racket import Racket
import square

#Global Colors
GREEN  = (31, 161, 61)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (3, 73, 252)

pygame.init()

#Game objects
racketA = Racket(RED, 10, 100)
racketA.rect.x = 20
racketA.rect.y = 200

scoreA = 0
scoreB = 0

racketB = Racket(BLUE, 10, 100)
racketB.rect.x = 670
racketB.rect.y = 200

ball = square.Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#Window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")

#List of Sprites
all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(racketA)
all_sprites_list.add(racketB)
all_sprites_list.add(ball)

#FPS
clock = pygame.time.Clock()

#Main game loop
GameLoop = True
while GameLoop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GameLoop = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				GameLoop = False
	
	# Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		racketA.moveUp(5)
	if keys[pygame.K_s]:
		racketA.moveDown(5)
	if keys[pygame.K_UP]:
		racketB.moveUp(5)
	if keys[pygame.K_DOWN]:
		racketB.moveDown(5)
	
	# --- Game logic should go here
	all_sprites_list.update()
	
	# Check if the ball is bouncing against any of the 4 walls:
	if ball.rect.x >= 690:
		scoreA += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.x <= 0:
		scoreB += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.y > 490:
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.y < 0:
		ball.velocity[1] = -ball.velocity[1]
	
	# Detect collisions between the ball and the paddles
	if pygame.sprite.collide_mask(ball, racketA) or pygame.sprite.collide_mask(ball, racketB):
		ball.bounce()
	
	# --- Drawing code should go here
	# First, clear the screen to black.
	screen.fill(GREEN)
	# Draw the net
	pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
	
	# Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
	all_sprites_list.draw(screen)
	
	# Display scores:
	font = pygame.font.Font(None, 74)
	text = font.render(str(scoreA), 1, WHITE)
	screen.blit(text, (250, 10))
	text = font.render(str(scoreB), 1, WHITE)
	screen.blit(text, (420, 10))
	
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	
	# --- Limit to 60 frames per second
	clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()