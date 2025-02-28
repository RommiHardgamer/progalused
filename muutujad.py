import pygame
import random
import time

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Õunade püüdmine!")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)
button_font = pygame.font.SysFont(None, 48)

class Basket:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height - self.height - 10
        self.speed = 10

    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

class Apple:
    def __init__(self):
        self.size = 20
        self.x = random.randint(0, screen_width - self.size)
        self.y = -self.size
        self.speed = random.randint(3, 6)

    def fall(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.size)

def main_menu():
    running = True
    while running:
        screen.fill(WHITE)
        title_text = font.render("Õunade püüdmine!", True, BLACK)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))

        start_button = pygame.Rect(screen_width // 2 - 100, 150, 200, 50)
        pygame.draw.rect(screen, GREEN, start_button)
        start_text = button_font.render("Alusta", True, WHITE)
        screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, 160))

        exit_button = pygame.Rect(screen_width // 2 - 100, 230, 200, 50)
        pygame.draw.rect(screen, RED, exit_button)
        exit_text = button_font.render("Välju", True, WHITE)
        screen.blit(exit_text, (screen_width // 2 - exit_text.get_width() // 2, 240))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_duration_menu()
                if exit_button.collidepoint(event.pos):
                    running = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)

def game_duration_menu():
    running = True
    while running:
        screen.fill(WHITE)
        title_text = font.render("Vali mängu aeg", True, BLACK)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))

        five_minutes_button = pygame.Rect(screen_width // 2 - 100, 150, 200, 50)
        pygame.draw.rect(screen, GREEN, five_minutes_button)
        five_minutes_text = button_font.render("5 minutit", True, WHITE)
        screen.blit(five_minutes_text, (screen_width // 2 - five_minutes_text.get_width() // 2, 160))

        one_minutes_button = pygame.Rect(screen_width // 2 - 100, 230, 200, 50)
        pygame.draw.rect(screen, GREEN, one_minutes_button)
        one_minutes_text = button_font.render("1 minut", True, WHITE)
        screen.blit(one_minutes_text, (screen_width // 2 - one_minutes_text.get_width() // 2, 240))

        back_button = pygame.Rect(screen_width // 2 - 100, 310, 200, 50)
        pygame.draw.rect(screen, RED, back_button)
        back_text = button_font.render("Tagasi", True, WHITE)
        screen.blit(back_text, (screen_width // 2 - back_text.get_width() // 2, 320))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if five_minutes_button.collidepoint(event.pos):
                    start_game(5 * 60)
                if one_minutes_button.collidepoint(event.pos):
                    start_game(1 * 60)
                if back_button.collidepoint(event.pos):
                    running = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)

def start_game(time_limit):
    basket = Basket()
    apples = []
    score = 0
    game_over = False
    start_time = time.time()
    
    max_apples = 10

    while not game_over:
        screen.fill(WHITE)

        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            game_over = True

        if len(apples) < max_apples and random.random() < 0.02:
            apples.append(Apple())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket.move(-basket.speed)
        if keys[pygame.K_RIGHT]:
            basket.move(basket.speed)

        for apple in apples[:]:
            apple.fall()
            if apple.y > screen_height:
                apples.remove(apple)
                score -= 1
            if apple.y + apple.size >= basket.y and basket.x < apple.x < basket.x + basket.width:
                apples.remove(apple)
                score += 1

        basket.draw()
        for apple in apples:
            apple.draw()

        score_text = font.render(f"Skoor: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        remaining_time = int(time_limit - elapsed_time)
        time_text = font.render(f"Aeg: {remaining_time}s", True, BLACK)
        screen.blit(time_text, (screen_width - 150, 10))

        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    game_over_menu(score)

def game_over_menu(final_score):
    running = True
    while running:
        screen.fill(WHITE)
        game_over_text = font.render("Mäng läbi!", True, BLACK)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, 50))

        score_text = font.render(f"Lõpp skoor: {final_score}", True, BLACK)
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 150))

        restart_button = pygame.Rect(screen_width // 2 - 100, 230, 200, 50)
        pygame.draw.rect(screen, GREEN, restart_button)
        restart_text = button_font.render("Alusta uuesti", True, WHITE)
        screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, 240))

        exit_button = pygame.Rect(screen_width // 2 - 100, 310, 200, 50)
        pygame.draw.rect(screen, RED, exit_button)
        exit_text = button_font.render("Välju", True, WHITE)
        screen.blit(exit_text, (screen_width // 2 - exit_text.get_width() // 2, 320))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    main_menu()
                if exit_button.collidepoint(event.pos):
                    running = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main_menu()
