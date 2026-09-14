import pygame
# import Pygame library
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
# importuje dané věci z constants -> také lze from module import *
# pokud dám jen import constants, budu pak muset ke všemu přistupovat s předponou modulu (constants.SCREEN_HEIGHT)
from logger import log_state
# logger je testovací soubor boot.dev

def main():
    print(f"Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() #initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # získá se instance GUI okna

    clock_object = pygame.time.Clock()
    dt = 0.0 #delta time

    while True: #nekonečná loop (game loop)
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #kontroluje eventy, pokud uživatel zmáčkl X
            # hru to zavře

        screen.fill("black")
        pygame.display.flip() #refresne screen

        dt = clock_object.tick(60) / 1000
        # .tick() pozastaví program na potřebnou dobu
        # 60 je max FPS, které chci (můžu zvolit jaké chci)
        # zároveň to vrátí číslo, konkrétně ms, které uběhly
        # od minulého volání .tick()
        # dělím 1000 protože to chci v sekundách, ne ms

if __name__ == "__main__":
    main()
