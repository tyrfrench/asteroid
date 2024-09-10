import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *


def game_start():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

def main():
	pygame.init()
	print(f"pygame live: {pygame.get_init()}")
	game_start()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	
	dt = 0

	while pygame.get_init() == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		for action in updatable:
			action.update(dt)

		for asteroid in asteroids:
			if asteroid.collision(player) == True:
				print("Game over!")
				raise SystemExit

		screen.fill(color=(0, 0, 0, 1))

		for action in drawable:
			action.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000  # Last action of frame


if __name__ == "__main__":
	main()
