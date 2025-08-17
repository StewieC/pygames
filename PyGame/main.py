import pygame
import time
import random

#creating a window
WIDTH, HEIGHT = 1000, 500



WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space dodge")

# setting background
BG =pygame.transform.scale(pygame.image.load("PyGame/image.png"), (WIDTH, HEIGHT))


def draw():
    WIN.blit(BG, (0,0))
    pygame.display.update()

# main game logic

def main():
    run = True
    # check if user clicks quit button
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        # fill the window with background
            draw()
    pygame.quit()
    
    
if __name__ == "__main__":
    main()