import pygame
import sys
import os
from circleshape import CircleShape
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        font = pygame.font.Font(None, 48)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        for obj in asteroids:
            if player.collision(obj):
                print(f"Game over! Your score was {score}")
                return
        for bullet in shots:
            for obj in asteroids:
                if bullet.collision(obj):
                    bullet.kill()
                    obj.split()
                    score += SCORE_INCREMENT
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()
