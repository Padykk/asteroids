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

    while True: #nekonečná loop (game loop)
        log_state()

        for event in pygame.event.get():
            pass

        screen.fill("black")
        pygame.display.flip() #refresne screen

if __name__ == "__main__":
    main()
