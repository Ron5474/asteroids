from constants import *
from player import Player
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    p = Player(x, y)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    p.containers = (updatable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        p.update(dt)
        screen.fill("black")
        p.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen heigth: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
