################################################################################
# INSTRUCTIONS:
# Complete the TODOS below to add another "enemy" character. When the player 
# collides with the enemy, it should reset points to 0.
# 
# STRETCH CHALLENGES (complete if you've already finished the main challenge):
# 1. Add a "You Lose" screen that shows for 2 seconds if the player collides
#    with an enemy.
# 2. Create multiple enemies that can all fall at once.
################################################################################

import pygame
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Make School Starter Game!')

################################################################################
# VARIABLES
################################################################################

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

CHARACTER_WIDTH = 40
CHARACTER_HEIGHT = 40

# Color constants
BLACK = (0, 50, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
PINK = (255, 182, 193)

# Player Variables
player_x = 50
player_y = 450

# Target Variables
target_x = 250
target_y = 0

# TODO: Add variables for the "enemy" character
enemy_x = 200
enemy_y = 50

# Other variables
enemy_velocity = 7  # Adjust the value as needed
velocity = 4
points = 0

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


game_over = False


################################################################################
# HELPER FUNCTIONS
################################################################################

def is_colliding(x1, y1, x2, y2, width, height):
    """Returns True if two rectangles are colliding, or False otherwise"""
    # If one rectangle is on left side of the other 
    if (x1 >= x2 + width) or (x2 >= x1 + width):
        return False
  
    # If one rectangle is above the other
    if (y1 >= y2 + height) or (y2 >= y1 + height):
        return False
  
    return True

def draw_text(text, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

################################################################################
# GAME LOOP
################################################################################

# Run until the user asks to quit
running = True
while running:
    # Advance the clock
    pygame.time.delay(20)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()



    # Update the player
    if keys[pygame.K_LEFT]:
        player_x -= velocity
    if keys[pygame.K_RIGHT]:
        player_x += velocity
    if keys[pygame.K_UP]:
        player_y -= velocity
    if keys[pygame.K_DOWN]:
        player_y += velocity

    # Update the target
    target_y += velocity
    enemy_y += enemy_velocity

    # TODO: Update the enemy's y position based on its velocity

    # If target went off the screen, reset it
    if target_y > SCREEN_HEIGHT: 
        target_y = 0
        target_x = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)

    # TODO: If enemy went off the screen, reset it
    if enemy_y > SCREEN_HEIGHT: 
        enemy_y = 0
        enemy_x = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)

    # If player collides with target, reset it & increment points
    if is_colliding(player_x, player_y, target_x, target_y, CHARACTER_WIDTH, CHARACTER_HEIGHT):
        points += 1
        target_y = 0
        target_x = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)

    # TODO: If player collides with enemy, reset it & set points to 0
    if is_colliding(player_x, player_y, enemy_x, enemy_y, CHARACTER_WIDTH, CHARACTER_HEIGHT):
       game_over = True
    # Fill screen with white
    screen.fill(WHITE)

    if game_over:
        screen.fill(BLACK)  # Fill the screen with a black background

        # Display "You Lose" text
        draw_text("Sorry Professor, You Lose!", WHITE, 40, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50)
        draw_text(f'Your Score was: {points}', WHITE, 30, SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 + 20)
        
        pygame.display.update()

        # Wait for a moment before quitting
        pygame.time.delay(3000)  
        running = False
    # Draw the player as a blue square
    pygame.draw.rect(screen, BLUE, (player_x, player_y, CHARACTER_WIDTH, CHARACTER_HEIGHT))

    # Draw the target as a green square
    pygame.draw.rect(screen, GREEN, (target_x, target_y, CHARACTER_WIDTH, CHARACTER_HEIGHT))

    # TODO: Draw the enemy as a red square
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, CHARACTER_WIDTH, CHARACTER_HEIGHT))
    
    # Draw the points
    draw_text(text=f'Points: {points}', color=BLACK, font_size=24, x=20, y=20)

    draw_text("Welcome to Krystal's Game!", color=PINK, font_size=28, x=100, y=50)

    draw_text("Enemies = Red", color=BLACK, font_size=18, x=15, y=80)
    draw_text("Points = Green" , color=BLACK, font_size=18, x=15, y=100)


    
    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()