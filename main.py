import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    # player object
    player_one = Player(x, y)
    # astroid field object
    astroid_field = AsteroidField()


    
    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        # update the position of each player object in the group
        #player_one.update(dt)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player_one):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # draw each player object in the group
        #player_one.draw(screen)
        for player in drawable:
            player.draw(screen)

        
        

        pygame.display.flip()

        

        clock.tick(60)
        delta_time = clock.tick(60)
        dt = delta_time / 1000
        #print(dt)


if __name__ == "__main__":
    main()
