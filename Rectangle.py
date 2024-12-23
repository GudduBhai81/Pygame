import pygame
pygame.init()
screen = pygame.display.set_mode((500,400))
compelete = False

while not compelete:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            compelete = True
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(40, 40, 70, 70))
    
    pygame.display.flip()