#display text on screen object, figure out how to make text a button, implement mouse input, display pictures on screen. 
#When the mouse clicks a button on screen(or a coord), a new image and text surface will be blited on the screen, The endings could have a replay button also 
#surf = pygame.image.load("beastresized.jpg")
#surf.convert() This may make it more optimized? Idk 
#screen.blit(surf, (0, 0)) #transfers surf onto screen
# if pygame.mouse.get_pressed()[0] == True: - This is for the left mouse button 
#pygame.Rect.collidepoint - so if the mouse x,y is in the rectangle then clicks, a new image and text will blit onto the screen. 
# So first the mouse has to be in the rectangle, then it has to click, for the screen to change.

import pygame
def main():
    pygame.init()
    pygame.display.set_caption("Choose Your Own Adventure")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution) #set mode creates surface, it's stored inside the variable screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        button = pygame.draw.rect(screen, (150, 0, 0), (200, 200, 200, 200)) #first 2 are xy 
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(button, mouse_pos) == True:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) #changes cursor into hand with hovering over button
        else:
            pygame.mouse.set_cursor()
        if pygame.Rect.collidepoint(button, mouse_pos) and pygame.mouse.get_pressed()[0]: #I need it to stay after clicking, if the mouse clicks up, the image stays
            surf = pygame.image.load("beastresized.jpg")
            screen.blit(surf, (0, 0)) #when mouse clicks button, something happens 
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

