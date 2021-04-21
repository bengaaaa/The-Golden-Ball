# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:38:22 2020

@author: benga
"""


"""
 This example shows having multiple balls bouncing around the screen at the
 same time. You can hit the space bar to spawn more balls.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
 
import pygame
import random
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (230, 230, 250)
# I decided to switch to using gold but I'm too lazy to change all of the names
RED = ( 240, 230, 140 )
BROWN = ( 205, 133, 63 )
PINK = ( 255, 182, 193 )
GREEN = (34, 139, 34)
DARKRED = ( 128, 0, 0 )
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25
LIFE_SIZE = 15
PROJ_SIZE = 5


class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        
class User:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        
class Life:
    def __init__(self):
        self.x = 0
        self.y = 0         
        self.change_x = 0
        self.change_y = 0

class Bomb:
    def __init__(self):
        self.x = 0
        self.y = 0         
        self.change_x = 0
        self.change_y = 0
        
class Projectile:
    def __init__(self):
        self.x = 0
        self.y = 0         
        self.change_x = 0
        self.change_y = 0
        
class TNT:
    def __init__(self):
        self.x = 0
        self.y = 0         
        self.change_x = 0
        self.change_y = 0

def make_life():
    
    life = Life()
    # Starting position of the life
    # take into account the size of life so we don't spawn on the edge
    life.x = random.randrange(LIFE_SIZE, SCREEN_WIDTH - LIFE_SIZE)
    life.y = random.randrange(LIFE_SIZE, SCREEN_HEIGHT - LIFE_SIZE)
    
    # Speed and direction of life
    life.change_x = random.randrange(-1, 1)
    life.change_y = random.randrange(-1, 1)
    
    return life

def make_TNT():
    
    tnt = TNT()
    # Starting position of the life
    # take into account the size of life so we don't spawn on the edge
    tnt.x = random.randrange(LIFE_SIZE, SCREEN_WIDTH - LIFE_SIZE)
    tnt.y = random.randrange(LIFE_SIZE, SCREEN_HEIGHT - LIFE_SIZE)
    
    # Speed and direction of life
    tnt.change_x = random.randrange(-5, 5)
    tnt.change_y = random.randrange(-5, 5)
    
    return tnt

def make_bomb():
    
    bomb = Bomb()
    # Starting position of the life
    # take into account the size of life so we don't spawn on the edge
    bomb.x = random.randrange(LIFE_SIZE, SCREEN_WIDTH - LIFE_SIZE)
    bomb.y = random.randrange(LIFE_SIZE, SCREEN_HEIGHT - LIFE_SIZE)
    
    # Speed and direction of life
    bomb.change_x = random.randrange(-2, 2)
    bomb.change_y = random.randrange(-2, 2)
    
    return bomb
 
def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    # Speed and direction of rectangle
    ball.change_x = random.randrange(-4, 3)
    ball.change_y = random.randrange(-4, 3)
    
    # Need to make sure the ball doesnt spawn on the user
    
    return ball
 
 
def main():
    """
    This is our main program.
    """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("The Golden Ball")
 
    # Loop until the user clicks the close button.
    done = False
    
    #Set starting user size
    USER_SIZE = 10

 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # Spawn the user
    user = User()
    user.x = random.randrange(USER_SIZE, SCREEN_WIDTH - USER_SIZE )
    user.y = random.randrange(USER_SIZE, SCREEN_HEIGHT - USER_SIZE )
 
    # an empty list for the life and the balls
    ball_list = []
    life_list = []
    bomb_list = []
    proj_list = []
    projr_list = []
    tnt_list = []
 
    #make a starting ball
    ball = make_ball()
    ball.change_x = 1
    ball.change_y = -1
    distance = math.sqrt((ball.x - user.x)**2 \
        + (ball.y - user.y )**2)
    if not distance < ( BALL_SIZE + USER_SIZE + 100 ):
        ball_list.append(ball)
    
    #make a starting life
    life = make_life()
    life_list.append( life )
    
    # This is the number of lives that the user has
    life_count = 1
    
    # This is the player's score
    score = 0
    
    clock.tick(60)
    pygame.time.delay( 1000 )
    
    #Lets add some lofi beats
    pygame.mixer.music.load( "summer.mp3" )
    pygame.mixer.music.play()
    
    ball_timer = 1
    
    # Here is a function for ending the game
    def end_game():
        screen.fill(RED)
        font = pygame.font.Font('Royalacid.ttf', 32)
        text = font.render('Game over. Your score: %d' % score, True, BROWN )
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit( text, textRect )
        pygame.display.flip()
        pygame.time.delay( 6000 )
        pygame.quit()
    
    # This function makes projectiles
    def make_projectiles():
    
        proj = Projectile()
        proj.x = 0
        proj.y = 0
        proj.change_x = 0
        proj.change_y = 0
    
        return proj
    
    def make_projectilesR():
    
        projr = Projectile()
        projr.x = 0
        projr.y = 0
        projr.change_x = 0
        projr.change_y = 0
    
        return projr
    
    #Lets make an intro to the game
    screen.fill(RED)
    pygame.display.flip()
    intro = True
    intro_counter = 0
    while intro:
        if intro_counter == 30 :
            font = pygame.font.Font('Royalacid.ttf', 32)
            text = font.render( "Welcome", True, BROWN )
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 100 )
            screen.blit( text, textRect )
            pygame.display.flip()
        if intro_counter == 70:
            text = font.render( "to", True, BROWN )
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 200 )
            screen.blit( text, textRect )
            pygame.display.flip()
        if intro_counter == 115 :
            text = font.render( '"The Golden Ball"' , True, BROWN )
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 300 )
            screen.blit( text, textRect )
            pygame.display.flip()
        if intro_counter == 190 :
            text = font.render( "Use WASD to move", True, BROWN )
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 400 )
            screen.blit( text, textRect )
            pygame.display.flip()
        if intro_counter == 500:
            intro = False
        clock.tick(60)    
        intro_counter += 1
        
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new ball.
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    distance = math.sqrt((ball.x - user.x)**2 \
                        + (ball.y - user.y )**2)
                    if not distance < ( BALL_SIZE + USER_SIZE + 600 ):
                        ball_list.append(ball)
                # if the user presses the WASD keys
                if event.key == pygame.K_w:
                    user.change_y = -4
                    user.change_x = 0
                if event.key == pygame.K_a:
                    user.change_x = -4
                    user.change_y = 0
                if event.key == pygame.K_s:
                    user.change_y = 4
                    user.change_x = 0
                if event.key == pygame.K_d:
                    user.change_x = 4
                    user.change_y = 0
 
        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
        
        # check if user hits a ball and lose a life if they do
        for ball in ball_list:
            distance = math.sqrt((ball.x - user.x)**2 + (ball.y - user.y )**2)
            if distance < (BALL_SIZE + USER_SIZE ):
                life_count -= 1
                ball_list.remove( ball )
                    
        # This spawns a ball every 150 milliseconds
        if ball_timer % 150 == 0:
            ball = make_ball()
            # This code below makes sure the ball doesnt spawn on top of the user
            distance = math.sqrt((ball.x - user.x)**2 \
                + (ball.y - user.y )**2)
            if not distance < ( BALL_SIZE + USER_SIZE + 150 ):
                ball_list.append(ball)
                score += 1
                
        # This spawns life every 5 seconds
        if ball_timer % 500 == 0:
            life = make_life()
            # This code below makes sure the life doesn't spawn on top of the user
            distance = math.sqrt((life.x - user.x)**2 \
                + (life.y - user.y )**2)
            if not distance < ( LIFE_SIZE + USER_SIZE + 150 ):
                life_list.append(life)
                
        # spawn a bomb every 7 seconds
        if ball_timer % 700 == 0:
            bomb = make_bomb()
            # This code below makes sure the life doesn't spawn on top of the user
            distance = math.sqrt((bomb.x - user.x)**2 \
                + (bomb.y - user.y )**2)
            if not distance < ( LIFE_SIZE + USER_SIZE + 150 ):
                bomb_list.append(bomb)
                
        # Move the life around
        for life in life_list:
            # Move the ball's center
            life.x += life.change_x
            life.y += life.change_y
            # Bounce if necessary
            if life.y > SCREEN_HEIGHT - LIFE_SIZE or life.y < LIFE_SIZE:
                life.change_y *= -1
            if life.x > SCREEN_WIDTH - LIFE_SIZE or life.x < LIFE_SIZE:
                life.change_x *= -1
                
        # Move the projectiles around
        for proj in proj_list:
            # Move the ball's center
            proj.x += proj.change_x
            proj.y += proj.change_y
            # Bounce if necessary
            if proj.y > SCREEN_HEIGHT - PROJ_SIZE or proj.y < PROJ_SIZE:
                if proj in proj_list:
                    proj_list.remove( proj )
            if proj.x > SCREEN_WIDTH - PROJ_SIZE or proj.x < PROJ_SIZE:
                if proj in proj_list:
                    proj_list.remove( proj )
        
        # Move the projectiles around
        for projr in projr_list:
            # Move the ball's center
            projr.x += projr.change_x
            projr.y += projr.change_y
            # Bounce if necessary
            if projr.y > SCREEN_HEIGHT - PROJ_SIZE or projr.y < PROJ_SIZE:
                if projr in projr_list:
                    projr_list.remove( projr )
            if projr.x > SCREEN_WIDTH - PROJ_SIZE or projr.x < PROJ_SIZE:
                if projr in projr_list:
                    projr_list.remove( projr )
                
        # Move the bombs around
        for bomb in bomb_list:
            # Move the ball's center
            bomb.x += bomb.change_x
            bomb.y += bomb.change_y
            # Bounce if necessary
            if bomb.y > SCREEN_HEIGHT - LIFE_SIZE or bomb.y < LIFE_SIZE:
                bomb.change_y *= -1
            if bomb.x > SCREEN_WIDTH - LIFE_SIZE or bomb.x < LIFE_SIZE:
                bomb.change_x *= -1
                
        # Move the tnt around
        for tnt in tnt_list:
            # Move the ball's center
            tnt.x += tnt.change_x
            tnt.y += tnt.change_y
            # Bounce if necessary
            if tnt.y > SCREEN_HEIGHT - LIFE_SIZE or tnt.y < LIFE_SIZE:
                tnt.change_y *= -1
            if tnt.x > SCREEN_WIDTH - LIFE_SIZE or tnt.x < LIFE_SIZE:
                tnt.change_x *= -1
                
        # check if user hits a life and give them another if they do
        for life in life_list:
            distance = math.sqrt((life.x - user.x)**2 + (life.y - user.y )**2)
            if distance < (LIFE_SIZE + USER_SIZE ):
                life_count += 1
                life_list.remove( life )
                score += 1
            
        # check if user hits a bomb and make projectiles if they do
        for bomb in bomb_list:
            distance = math.sqrt((bomb.x - user.x)**2 + (bomb.y - user.y )**2)
            if distance < (LIFE_SIZE + USER_SIZE ):
                proj = make_projectiles()
                proj.change_x = 5
                proj.x = bomb.x
                proj.y = bomb.y
                proj_list.append( proj )
                proj = make_projectiles()
                proj.change_x = -5
                proj.x = bomb.x
                proj.y = bomb.y
                proj_list.append( proj )
                proj = make_projectiles()
                proj.change_y = 5
                proj.x = bomb.x
                proj.y = bomb.y
                proj_list.append( proj )
                proj = make_projectiles()
                proj.change_y = -5
                proj.x = bomb.x
                proj.y = bomb.y
                proj_list.append( proj )
                proj = make_projectiles()
                proj.change_x = 3
                proj.change_y = 4
                proj.x = bomb.x
                proj.y = bomb.y
                proj_list.append( proj )
                proj = make_projectiles()
                proj.change_x = -3
                proj.change_y = -4
                proj.x = bomb.x
                proj.y = bomb.y
                proj_list.append( proj )
                proj = make_projectiles()
                proj.change_x = -3
                proj.change_y = 4
                proj.x = bomb.x
                proj.y = bomb.y
                proj_list.append( proj )
                proj = make_projectiles()
                proj.change_x = 3
                proj.change_y = -4
                proj.x = bomb.x
                proj.y = bomb.y
                proj_list.append( proj )
                bomb_list.remove( bomb )
                
        # check if user hits tnt and make projectiles if they do
        for tnt in tnt_list:
            distance = math.sqrt((tnt.x - user.x)**2 + (tnt.y - user.y )**2)
            if distance < (LIFE_SIZE + USER_SIZE ):
                projr = make_projectilesR()
                projr.change_x = 5
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -5
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_y = 5
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_y = -5
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = 3
                projr.change_y = 4
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -3
                projr.change_y = -4
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -3
                projr.change_y = 4
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = 3
                projr.change_y = -4
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = 4
                projr.change_y = 3
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -4
                projr.change_y = -3
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -4
                projr.change_y = 3
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = 4
                projr.change_y = -3
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = 1
                projr.change_y = 5
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = 1
                projr.change_y = -5
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -1
                projr.change_y = 5
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -1
                projr.change_y = -5
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = 5
                projr.change_y = 1
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -5
                projr.change_y = -1
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = -5
                projr.change_y = 1
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                projr = make_projectilesR()
                projr.change_x = 5
                projr.change_y = -1
                projr.x = tnt.x
                projr.y = tnt.y
                projr_list.append( projr )
                tnt_list.remove( tnt )
                
        # Check if a projectile hits a ball
        for proj in proj_list:
            for ball in ball_list:
                distance = math.sqrt((proj.x - ball.x)**2 + (proj.y - ball.y )**2)
                if distance < (BALL_SIZE + PROJ_SIZE ):
                    ball_list.remove( ball )
                    score += 1
                    
        # Check if a projectiler hits a ball
        for projr in projr_list:
            for ball in ball_list:
                distance = math.sqrt((projr.x - ball.x)**2 + (projr.y - ball.y )**2)
                if distance < (BALL_SIZE + PROJ_SIZE ):
                    ball_list.remove( ball )
                    score += 1
                
            
        if life_count == 0:
            end_game()
            return
        
        # More music?
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load( "beach.mp3" )
            pygame.mixer.music.play()
        
        # Lets make the game harder as time goes on
        if ball_timer > 2000:
            if ball_timer % 400 == 0:
                bomb = make_bomb()
            # This code below makes sure the bomb doesn't spawn on top of the user
                distance = math.sqrt((bomb.x - user.x)**2 \
                + (bomb.y - user.y )**2)
                if not distance < ( LIFE_SIZE + USER_SIZE + 150 ):
                    bomb_list.append(bomb)
            if ball_timer % 110 == 0:
                ball = make_ball()
                # This code below makes sure the ball doesnt spawn on top of the user
                distance = math.sqrt((ball.x - user.x)**2 \
                    + (ball.y - user.y )**2)
                if not distance < ( BALL_SIZE + USER_SIZE + 150 ):
                    ball_list.append(ball)
                    score += 1
            if ball_timer % 1001 == 0:
                tnt = make_TNT()
            # This code below makes sure the tnt doesn't spawn on top of the user
                distance = math.sqrt((tnt.x - user.x)**2 \
                + (tnt.y - user.y )**2)
                if not distance < ( LIFE_SIZE + USER_SIZE + 150 ):
                    tnt_list.append(tnt)
        if ball_timer > 6000:
            if ball_timer % 300 == 0:
                bomb = make_bomb()
            # This code below makes sure the life doesn't spawn on top of the user
                distance = math.sqrt((bomb.x - user.x)**2 \
                + (bomb.y - user.y )**2)
                if not distance < ( LIFE_SIZE + USER_SIZE + 150 ):
                    bomb_list.append(bomb)
            if ball_timer % 45 == 0:
                ball = make_ball()
                # This code below makes sure the ball doesnt spawn on top of the user
                distance = math.sqrt((ball.x - user.x)**2 \
                    + (ball.y - user.y )**2)
                if not distance < ( BALL_SIZE + USER_SIZE + 150 ):
                    ball_list.append(ball)
                    score += 1
        if ball_timer > 12000:
            if ball_timer % 40 == 0:
                ball = make_ball()
                # This code below makes sure the ball doesnt spawn on top of the user
                distance = math.sqrt((ball.x - user.x)**2 \
                    + (ball.y - user.y )**2)
                if not distance < ( BALL_SIZE + USER_SIZE + 150 ):
                    ball_list.append(ball)
                    score += 1
            
                
            
            
                
        # Bounce the user if needed
        if user.y > SCREEN_HEIGHT - USER_SIZE or user.y < USER_SIZE:
                user.change_y *= -1
        if user.x > SCREEN_WIDTH - USER_SIZE or user.x < USER_SIZE:
                user.change_x *= -1
        
        #Change the user's position
        user.x += user.change_x
        user.y += user.change_y
        
        # add to the ball timer
        ball_timer += 1
 
        # --- Drawing
        # Set the screen background
        screen.fill(BROWN)
        
        # Draw the user
        pygame.draw.circle( screen, RED, [user.x, user.y], USER_SIZE)
 
        # Draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)
            
        # Draw the life
        if len( life_list ) > 0:   
            for life in life_list:
                pygame.draw.circle(screen, PINK, [life.x, life.y], LIFE_SIZE)
                
        # Draw the bombs
        if len( bomb_list ) > 0:
            for bomb in bomb_list:
                pygame.draw.circle(screen, GREEN, [bomb.x, bomb.y], LIFE_SIZE)
                
        # Draw the projectiles
        if len( proj_list ) > 0:
            for proj in proj_list:
                pygame.draw.circle(screen, GREEN, [proj.x, proj.y], PROJ_SIZE)
                
        # Draw the projectilesr
        if len( projr_list ) > 0:
            for projr in projr_list:
                pygame.draw.circle(screen, DARKRED, [projr.x, projr.y], PROJ_SIZE)        
                
                
        # Draw the tnt
        if len( tnt_list ) > 0:
            for tnt in tnt_list:
                pygame.draw.circle(screen, DARKRED, [tnt.x, tnt.y], LIFE_SIZE)
                
        # Display lives in the top left corner
        text = font.render( "Lives: %d" % life_count, True, PINK )
        textRect = text.get_rect()
        textRect.center = ( 60, 20 )
        screen.blit( text, textRect )
        
        # Display score in the top right
        text = font.render( "Score: %d" % score, True, GREEN )
        textRect = text.get_rect()
        textRect.center = ( 620, 20 )
        screen.blit( text, textRect )
 
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
    
