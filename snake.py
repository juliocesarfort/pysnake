#!/usr/bin/python
import pygame
import random
import sys

RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

HEIGHT = 800
WIDTH = 600
FPS = 30
FONT_SIZE = 30
BLOCK_SIZE = 10

DRAW_SCREEN = False

pygame.init()

display_screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Snake")

def message_on_screen(msg, color):
    font = pygame.font.SysFont(None, FONT_SIZE)
    render_surface = font.render(msg, True, color)
    display_screen.blit(render_surface, HEIGHT/2, WIDTH/2)

def random_position():
    rand_x = random.randint(0 + BLOCK_SIZE, HEIGHT - BLOCK_SIZE)
    rand_y = random.randint(0 + BLOCK_SIZE, WIDTH - BLOCK_SIZE)
    return (rand_x, rand_y)

def draw_snake(x, y):
    pygame.draw.rect(display_screen, GREEN, (x, y, BLOCK_SIZE, BLOCK_SIZE), 0)

def draw_apple(x, y):
    ''' Round it to the nearest round of 10 '''
    x = round(x/10.0) * 10.0
    y = round(x/10.0) * 10.0
    pygame.draw.rect(display_screen, RED, (x, y, BLOCK_SIZE, BLOCK_SIZE), 0)

def eat_apple():
    return True

def collision_wall(x, y):
    if (x + BLOCK_SIZE >= HEIGHT) or (x + BLOCK_SIZE <= 0):
        return True
    elif (y - BLOCK_SIZE >= WIDTH) or (y - BLOCK_SIZE <= 0):
        return True
    else:
        return False

def main():
    gameloop = True
    gameover = False
    
    clock = pygame.time.Clock()
    snakehead_x, snakehead_y = random_position()
    apple_x, apple_y = random_position()
    change_x = change_y = 0

    while gameloop:
        while not gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameloop = False
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        change_x = BLOCK_SIZE
                        change_y = 0
                        print "RIGHT"
                    if event.key == pygame.K_LEFT:
                        change_x = -BLOCK_SIZE
                        change_y = 0
                        print "LEFT"
                    if event.key == pygame.K_UP:
                        change_x = 0
                        change_y = -BLOCK_SIZE
                        print "UP"
                    if event.key == pygame.K_DOWN:
                        change_x = 0
                        change_y = BLOCK_SIZE
                        print "DOWN"
                
                    if event.key == pygame.K_q:
                        gameloop = False
                        gameover = True
                        pygame.quit()
                        sys.exit()
     
            snakehead_x += change_x
            snakehead_y += change_y

            display_screen.fill(WHITE)
            draw_snake(snakehead_x, snakehead_y)
            draw_apple(apple_x, apple_y)

            if collision_wall(snakehead_x, snakehead_y):
                print "COLIDIU"
                gameover = True

            if apple_x == snakehead_x or apple_y+1 == snakehead_y:
                print "COMEU!"
                apple_x, apple_y = random_position()
                draw_apple(apple_x, apple_y)

            pygame.display.update()
            clock.tick(FPS)

        print "GAME OVER"
        gameloop = False


if __name__ == '__main__':
    main()
