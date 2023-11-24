import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Red Ball Movement Game")

RED = (255, 0, 0)
WHITE = (255, 255, 255)

ball_radius = 25
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_speed > ball_radius:
                ball_y -= ball_speed
            if event.key == pygame.K_DOWN and ball_y + ball_speed < SCREEN_HEIGHT - ball_radius:
                ball_y += ball_speed
            if event.key == pygame.K_LEFT and ball_x - ball_speed > ball_radius:
                ball_x -= ball_speed
            if event.key == pygame.K_RIGHT and ball_x + ball_speed < SCREEN_WIDTH - ball_radius:
                ball_x += ball_speed

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

pygame.quit()
