import pygame


def main():
    # In Processing, this is where void setup() would be #

    size = (640, 320)  # Set the screen size
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode(size)  # Initialize the pygame screen
    clock = pygame.time.Clock()  # Initialize a pygame timer

    black = (0, 0, 0)  # Define the color black

    while True:
        # In Processing, this is where void draw() would be #

        # Check for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                pygame.quit()

        screen.fill(black)  # Fill the whole screen with the color black

        # Add some drawing code here

        pygame.display.flip()  # Update the screen

        clock.tick(60)  # Limits frame rate to 60 FPS


# Run the main function only if this module is executed as the main script
if __name__ == "__main__":
    # call the main function
    main()
