import pygame
from random import randrange as rnd

WIDTH, HEIGHT = 1400, 900
fps = 60

paddle_w = 250
paddle_h = 30
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)

ball_radius = 19
ball_speed = 1
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

block_list = [pygame.Rect(10 + 140 * i, 10 + 80 * j, 125, 68) for i in range(10) for j in range(4)]
color_list = [(rnd(90, 93), rnd(90, 92), rnd(90, 91)) for i in range(10) for j in range(4)]