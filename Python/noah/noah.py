import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bible Story: Noah\'s Ark')

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Load images (make sure you have these images in the same folder or change the path)
background_img = pygame.image.load('background.png')  # Replace with your background image path
noah_img = pygame.image.load('noah.png')  # Replace with your Noah image path
ark_img = pygame.image.load('ark.png')  # Replace with your ark image path
animal_img = pygame.image.load('animal.png')  # Replace with your animal image path

# Scale images if needed
noah_img = pygame.transform.scale(noah_img, (100, 200))
ark_img = pygame.transform.scale(ark_img, (300, 150))
animal_img = pygame.transform.scale(animal_img, (50, 50))

# Set positions for objects
ark_x = 250
ark_y = 400
noah_x = 350
noah_y = 350
animal_x = 500
animal_y = 500

# Animation function
def animate_scene():
    running = True
    clock = pygame.time.Clock()

    while running:
        # Handle events (close window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with white (or set a background image)
        screen.fill(WHITE)

        # Draw background
        screen.blit(background_img, (0, 0))

        # Move the ark and animal across the screen (animation)
        ark_x += 1
        if ark_x > screen_width:  # Reset position when it moves off-screen
            ark_x = -300  # Start from the left again

        animal_y -= 1  # Animal moves up, as if it's going on the Ark
        if animal_y < 100:  # Reset animal position
            animal_y = 500

        # Draw Noah, Ark, and Animals
        screen.blit(noah_img, (noah_x, noah_y))
        screen.blit(ark_img, (ark_x, ark_y))
        screen.blit(animal_img, (animal_x, animal_y))

        # Update the screen
        pygame.display.update()

        # Control the speed of the animation
        clock.tick(60)  # 60 frames per second

        # Pause for a moment before moving to the next scene
        if ark_x == -300:
            time.sleep(2)  # Wait 2 seconds before restarting

    # Quit the game
    pygame.quit()

