import pygame
from sys import exit

pygame.init()  # runs pygame
screen = pygame.display.set_mode((800, 400))     # game window.
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = font.render('My game', False, 'Black').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright =(600,300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom =(80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()       # exits game
            exit()              # stops loop
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')

    screen.blit(sky_surface,(0, 0 ))  # blit puts surface on surface
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_rect.x -= 4
    if snail_rect.x == -100: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print('collision')

    pygame.display.update()
    clock.tick(60) # limits game fps on 60