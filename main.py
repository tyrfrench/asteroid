import pygame
from constants import *



def game_start():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


def main():
	pygame.init()
	print(f"pygame live: {pygame.get_init()}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_start()
	while pygame.get_init() == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(color=(0, 0, 0, 1))
		pygame.display.flip()




if __name__ == "__main__":
	main()
