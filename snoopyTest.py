import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snoopy Escapes the Classroom")

# Clock for FPS
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Game variables
running = True
gameOver = False
win = False

# Functions
def reset_game():
    """Resets the game state."""
    global snoopy, teacher, gameOver, win
    snoopy = pygame.Rect(50, HEIGHT // 2, 50, 50)
    teacher = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
    gameOver = False
    win = False

def move_teacher():
    """Randomly moves the teacher."""
    global teacherDirection

    # Change direction randomly
    if random.randint(0, 100) < 5:
        teacherDirection = random.choice(["up", "down", "left", "right"])

    # Move the teacher
    if teacherDirection == "up" and teacher.top > 0:
        teacher.y -= teacherSpeed
    elif teacherDirection == "down" and teacher.bottom < HEIGHT:
        teacher.y += teacherSpeed
    elif teacherDirection == "left" and teacher.left > 0:
        teacher.x -= teacherSpeed
    elif teacherDirection == "right" and teacher.right < WIDTH:
        teacher.x += teacherSpeed

def display_message(message, color):
    """Displays a message on the screen."""
    text = font.render(message, True, color)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

# Reset game for the first playthrough
reset_game()

# Teacher movement attributes
teacherSpeed = 3
teacherDirection = random.choice(["up", "down", "left", "right"])

# Exit zone
exitZone = pygame.Rect(WIDTH - 50, HEIGHT // 2 - 50, 50, 100)

# Main game loop
while running:
    screen.fill(WHITE)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if gameOver and event.key == pygame.K_SPACE:
                reset_game()

    # Get keys
    keys = pygame.key.get_pressed()
    if not gameOver:
        if keys[pygame.K_UP] and snoopy.top > 0:
            snoopy.y -= 5
        if keys[pygame.K_DOWN] and snoopy.bottom < HEIGHT:
            snoopy.y += 5
        if keys[pygame.K_LEFT] and snoopy.left > 0:
            snoopy.x -= 5
        if keys[pygame.K_RIGHT] and snoopy.right < WIDTH:
            snoopy.x += 5

    # Move the teacher
    if not gameOver:
        move_teacher()

    # Check collision
    if snoopy.colliderect(teacher):
        gameOver = True

    # Check if Snoopy reached the exit
    if snoopy.colliderect(exitZone):
        win = True
        gameOver = True

    # Draw everything
    pygame.draw.rect(screen, BLUE, snoopy)  # Snoopy
    pygame.draw.rect(screen, RED, teacher)  # Teacher
    pygame.draw.rect(screen, BLACK, exitZone)  # Exit zone

    # Messages
    if gameOver:
        if win:
            display_message("You Escaped! Snoopy Wins! Press SPACE to play again.", BLUE)
        else:
            display_message("Caught by the Teacher! Game Over! Press SPACE to try again.", RED)

    # Update display
    pygame.display.flip()

    # Tick the clock
    clock.tick(30)

pygame.quit()

