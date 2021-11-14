import pygame

def main():

    screen = pygame.display.set_mode((500, 500))

    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((255, 255, 255))

        pygame.display.flip()

if __name__ == "__main__":
    main()