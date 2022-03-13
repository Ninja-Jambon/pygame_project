import pygame
import os

pygame.font.init()

HOME_FONT = pygame.font.SysFont('comicsans', 40)

WIDTH = 900
HEIGHT = 500
BOY_WIDTH = 50
BOY_HEIGHT = 50

FPS = 60

VEL = 5

BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
WHITE = (255,255,255)

RED_BOY_IMAGE = pygame.image.load(os.path.join("Assets","red_sprite.png"))
BLUE_BOY_IMAGE = pygame.image.load(os.path.join("Assets","blue_sprite.png"))

RED_BOY = pygame.transform.scale(RED_BOY_IMAGE,(BOY_WIDTH, BOY_HEIGHT))
BLUE_BOY = pygame.transform.scale(BLUE_BOY_IMAGE,(BOY_WIDTH, BOY_HEIGHT))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

def home_window():
    WIN.fill(BLACK)
    home_text = HOME_FONT.render("Press SPACE to Start", 1, WHITE)
    WIN.blit(home_text, (WIDTH//2 - (home_text.get_width()//2), HEIGHT//2 - (home_text.get_height()//2)))
    pygame.display.update()

def draw_window(red,blue):
    WIN.fill(CYAN)
    WIN.blit(RED_BOY, (red.x,red.y))
    WIN.blit(BLUE_BOY, (blue.x,blue.y))
    pygame.display.update()

def blue_handle_movement(keys_pressed, blue):
    if keys_pressed[pygame.K_q] and blue.x - VEL >= 0: #LEFT
            blue.x -= VEL
    if keys_pressed[pygame.K_d] and blue.x + VEL + blue.width <= WIDTH: #RIGHT
            blue.x += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL >= 0: #LEFT
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width <= WIDTH: #RIGHT
            red.x += VEL

def main():
    red = pygame.Rect(700, 300, BOY_WIDTH, BOY_HEIGHT)
    blue = pygame.Rect(200, 300, BOY_WIDTH, BOY_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    home = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            home = False

        if home == True:
            home_window()
        elif home == False:
            draw_window(red, blue)
        blue_handle_movement(keys_pressed, blue)
        red_handle_movement(keys_pressed, red)
    pygame.quit()


if __name__ == "__main__":
    main()