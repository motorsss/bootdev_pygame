import pygame
from constants import *
from player import *

Black = (0, 0, 0)

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    font = pygame.font.SysFont("Arial" , 28 , bold = True)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(Black)
        player.draw(screen)
        fps = str(int(clock.get_fps()))
        fps_text = font.render(fps, True, pygame.Color("red"))
        screen.blit(fps_text, (10,10))
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__== "__main__":
    main()
