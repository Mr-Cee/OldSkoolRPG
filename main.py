import pygame

pygame.init()

width = 800
height = 800
game_window_bg = (255, 255, 255)

game_window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()


def run_game_loop():
    while True:
        # Handle Events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # Execute Logic
        # Update Display
        game_window.fill(game_window_bg)
        pygame.display.update()

        clock.tick(60)


run_game_loop()

pygame.quit()
quit()