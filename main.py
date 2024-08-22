# this allows us to use code from
# the open-source pygame library
# 
# throughout this file
import pygame
from constants import *
Black = (0, 0, 0)

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    font = pygame.font.SysFont("Arial" , 18 , bold = True)

    def update_fps():
        fps = str(int(clock.get_fps()))
        fps_text = font.render(fps, True, pygame.Color("red"))
        return fps_text


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(Black)
        screen.blit(update_fps(), (10,10))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__== "__main__":
    main()
