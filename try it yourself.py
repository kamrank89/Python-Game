import pygame
import sys
class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My test")
        self.bg_color = (255, 255, 255)


    def run_background(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
            self.screen.fill(self.bg_color)


            pygame.display.flip()


if __name__ == '__main__':
    ai = Window(1400, 800)
    ai.run_background()