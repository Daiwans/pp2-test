import pygame
import sys
from datetime import datetime
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

window_size = (768, 768)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Mickey Mouse Clock')

background_image = pygame.image.load('mickeyclock.jpeg')
minute_hand_image = pygame.image.load('right-hand.png')
second_hand_image = pygame.image.load('left-hand.png')

FPS = 60

center_of_rotation = (384, 384)

def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    current_minutes = now.minute
    current_seconds = now.second

    minute_angle = (current_minutes * 6) % 360
    second_angle = (current_seconds * 6) % 360

    minute_hand_rotated = pygame.transform.rotate(minute_hand_image, -minute_angle)
    second_hand_rotated = pygame.transform.rotate(second_hand_image, -second_angle)

    minute_hand_rect = minute_hand_rotated.get_rect(center=center_of_rotation)
    second_hand_rect = second_hand_rotated.get_rect(center=center_of_rotation)

    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))
    blit_rotate_center(screen, minute_hand_rotated, minute_hand_rect.topleft, minute_angle)
    blit_rotate_center(screen, second_hand_rotated, second_hand_rect.topleft, second_angle)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
