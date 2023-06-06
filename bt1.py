import pgzrun
import random
from random import randint

WIDTH = 800
HEIGHT = 600
score = 0
game_over = False

ship = Actor('images')
ship.x = 370
ship.y = 550

gem = Actor('gemblue')
gem.x = 200
gem.y = 0

meto = Actor('meteogrey')
meto.x = 400
meto.y = 0

button_width = 200
button_height = 100
button_pos = (WIDTH // 2 - button_width // 2, HEIGHT // 2 + 50)
restart_button_visible = False

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]
    ship.y = pos[1]

def on_mouse_down(pos, button):
    global score, game_over, restart_button_visible
    if game_over and restart_button_visible:
        if (
            pos[0] >= button_pos[0]
            and pos[0] < button_pos[0] + button_width
            and pos[1] >= button_pos[1]
            and pos[1] < button_pos[1] + button_height
        ):
            # Restart the game
            score = 0
            game_over = False
            restart_button_visible = False

def update():
    global score, game_over, restart_button_visible
    if not game_over:
        gem.y += 4 + score / 4
        meto.y += 4 + score + 4

        if gem.y > 600:
            gem.x = random.randint(20, 780)
            gem.y = 0
        if meto.y > 600:
            meto.x = random.randint(20, 780)
            meto.y = 0
        if gem.colliderect(ship):
            gem.x = random.randint(20, 780)
            gem.y = 0
            score += 1
        if meto.colliderect(ship):
            game_over = True
            restart_button_visible = True

def draw():
    screen.fill((0, 0, 0))
    if game_over:
        screen.draw.text('Game over', (200, 200), color=(255, 255, 255), fontsize=60)
        screen.draw.text('Final Score: ' + str(score), (200, 250), color=(255, 0, 255), fontsize=80)
        screen.draw.filled_rect(Rect(button_pos, (button_width, button_height)), (255, 0, 0))
        screen.draw.text('Restart', center=(WIDTH // 2, HEIGHT // 2 + 100), color=(255, 255, 255), fontsize=40)
    else:
        screen.draw.text('Score: ' + str(score), (10, 15), color=(255, 255, 255), fontsize=60)
        ship.draw()
        gem.draw()
        meto.draw()

pgzrun.go()
