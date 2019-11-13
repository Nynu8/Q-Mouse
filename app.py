import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))

for i in range(0, 8):
    for j in range(0, 8):
        pygame.draw.rect(screen, (i*25, j*25, 255), pygame.Rect(i*100, j*100, 100, 100))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()