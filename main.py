import pygame
from constants import *
from circleshape import *
from player import *



def game_start():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


def main():
	pygame.init()
	# print(f"pygame live: {pygame.get_init()}")
	
	Clock = pygame.time.Clock
	dt = 0
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_start()

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	player = Player(x, y)
	
	while pygame.get_init() == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(color=(0, 0, 0, 1))
		player.draw(screen)
		pygame.display.flip()

		

		dt = Clock().tick(60) / 1000  # Last action of frame




if __name__ == "__main__":
	main()
