import pygame

pygame.font.init()

HOME_FONT = pygame.font.SysFont('comicsans', 40)

WIDTH = 900
HEIGHT = 500

FPS = 60

BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
WHITE = (255,255,255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

def home_window():
    WIN.fill(BLACK)
    home_text = HOME_FONT.render("Press SPACE to Start", 1, WHITE)
    WIN.blit(home_text, (WIDTH//2 - (home_text.get_width()//2), HEIGHT//2 - (home_text.get_height()//2)))
    pygame.display.update()

def draw_window():
    WIN.fill(CYAN)
    pygame.display.update()

def main():
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
            draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()

