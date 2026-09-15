import pygame
# import Pygame library
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
# importuje dané věci z constants -> také lze from module import *
# pokud dám jen import constants, budu pak muset ke všemu přistupovat s předponou modulu (constants.SCREEN_HEIGHT)
from logger import log_state, log_event
# logger je testovací soubor boot.dev
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys


def main():
    print(f"Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() #initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # získá se instance GUI okna

    clock_object = pygame.time.Clock()
    dt = 0.0 #delta time

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    #group na všechno s metodou update
    drawable = pygame.sprite.Group()
    #grup na všechno s metodou draw
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    #přidání classy do group, takže nově vytvořené instance budou vždy součástí
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x, y)
    #vytvoří objekt player se souřadnicemi středu obrazovky

    asteroidfield = AsteroidField()


    while True: #nekonečná loop (game loop)
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #kontroluje eventy, pokud uživatel zmáčkl X
            # hru to zavře

        dt = clock_object.tick(60) / 1000
        # .tick() pozastaví program na potřebnou dobu
        # 60 je max FPS, které chci (můžu zvolit jaké chci)
        # zároveň to vrátí číslo, konkrétně ms, které uběhly
        # od minulého volání .tick()
        # dělím 1000 protože to chci v sekundách, ne ms

        #------------------------------------
        #------definice co je na screen------
        screen.fill("black")
        # vyčistí plátno (vyplní ho černě)

        updatable.update(dt)

        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for object in drawable:
            object.draw(screen)

        #------------------------------------
        #------------------------------------
        pygame.display.flip()
        #refresne screen (vykreslí vše výše)

if __name__ == "__main__":
    main()
     #if projde pouze pokud je volán přímo main.py (jako main soubor)
