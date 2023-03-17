import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (245, 245, 245)
GREEN = (50, 205, 50)
RED = (255, 0, 0)

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up clock
clock = pygame.time.Clock()

# Define snake properties
snake_size = 20
snake_speed = 10
snake_pos = [[100, 60], [90, 60], [80, 60]]

# Define food properties
food_size = 20
food_pos = [random.randrange(0, WIDTH // food_size) * food_size, random.randrange(0, HEIGHT // food_size) * food_size]

def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

def check_collision(snake_head, food_pos):
    return pygame.Rect(snake_head[0], snake_head[1], snake_size, snake_size).colliderect(pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

def move_snake(snake_pos, direction):
    global food_pos
    x, y = direction
    new_head = [snake_pos[0][0] + x * snake_size, snake_pos[0][1] + y * snake_size]

    if new_head in snake_pos[1:] or new_head[0] < food_size or new_head[0] >= WIDTH - food_size or new_head[1] < food_size or new_head[1] >= HEIGHT - food_size:
        return None  # Game over condition

    if check_collision(new_head, food_pos):
        food_pos = [random.randrange(1, (WIDTH // food_size) - 1) * food_size, random.randrange(1, (HEIGHT // food_size) - 1) * food_size]
    else:
        snake_pos.pop()

    snake_pos.insert(0, new_head)
    return snake_pos

def draw_grid():
    for x in range(food_size, WIDTH - food_size, food_size):
        pygame.draw.line(screen, (230, 230, 230), (x, food_size), (x, HEIGHT - food_size))
    for y in range(food_size, HEIGHT - food_size, food_size):
        pygame.draw.line(screen, (230, 230, 230), (food_size, y), (WIDTH - food_size, y))

def draw_border():
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(0, 0, WIDTH, food_size))
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(0, HEIGHT - food_size, WIDTH, food_size))
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(0, 0, food_size, HEIGHT))
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(WIDTH - food_size, 0, food_size, HEIGHT))

def main(snake_pos):
    direction = [1, 0]  # Initial direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != [0, 1]:
                    direction = [0, -1]
                elif event.key == pygame.K_DOWN and direction != [0, -1]:
                    direction = [0, 1]
                elif event.key == pygame.K_LEFT and direction != [1, 0]:
                    direction = [-1, 0]
                elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
                    direction = [1, 0]

        snake_pos = move_snake(snake_pos, direction)
        if snake_pos is None:  # Game over
            break

        screen.fill(WHITE)
        draw_border()
        draw_grid()
        draw_snake(snake_pos)
        draw_food(food_pos)
        pygame.display.flip()
        clock.tick(snake_speed)

    pygame.quit()

if __name__ == "__main__":
    main(snake_pos)
