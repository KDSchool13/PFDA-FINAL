#TODO: display text on screen object, figure out how to make text a button, implement mouse input, display pictures on screen. 
#When the mouse clicks a button on screen(or a coord), a new image and text surface will be blited on the screen, The endings could have a replay button also 
#surf = pygame.image.load("beastresized.jpg"), You will have to resize ur images. 
#surf.convert() This may make it more optimized? Idk 
#screen.blit(surf, (0, 0)) #transfers surf onto screen

import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Choose Your Own Adventure")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution) #set mode creates surface, it's stored inside the variable screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        screen.fill(black)
        surf = pygame.Surface((30,30))
        surf.fill(white)
        screen.blit(surf, (resolution[0]//2, resolution[1]//2)) #transfers surf onto screen
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

