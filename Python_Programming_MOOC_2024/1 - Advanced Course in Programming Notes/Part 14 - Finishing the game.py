# Finishing the game

# Our game is already quite functional, so it is time to add some finishing touches to it. 
# We will add a counter for displaying the moves taken, an option to start a new game and close the game with keyboard input, and a notification for when the player succeeds in solving the game.

# Move counter

# The move counter near the bottom edge of the game window displaye the number of moves taken by the player so far. 
# This can be used to find the solution with the least number of moves.

# The counter requires some shanges to the code. 
# First, let's change the constructor so that there is adequate space for the counter, and that we have an appropriate font at our disposal in order to draw the text:

    def __init__(self):
        ...
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))

        self.game_font = pygame.font.SysFont("Arial", 24)
        ...

# The move counter is initialized to zero at the beginning of the game. 
# Each move increases it by one:

    def new_game(self):
        ...
        self.moves = 0

    def move(self, move_y, move_x):
        ...
        self.moves += 1

# Each time the window contents are updated, the number of moves taken shown on the screen should also be updated:
    def draw_window(self):
        ...
        game_text = self.game_font.render("Moves: " + str(self.moves), True, (255, 0, 0))
        self.window.blit(game_text, (25, self.height * self.scale + 10))
        ...

# New game and exiting the game

# Next, let's add keyboard commands for starting a new game with F2 and exiting the game with Esc. 
# Both are rather easy to implement:

    def check_events(self):
        ...
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()
        ...

# We should also add information about this functionality for the player to see:
    def draw_window(self):
        ...
        game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (200, self.height * self.scale + 10))

        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + 10))
        ...

# Solving the game

# The player has solved the game when each box is in one of the target squares. 
# The following method takes care of checking this:

    def game_solved(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [2, 6]:
                    return False
        return True

# The method goes through all the squares in the game grid. 
# If any of the squares is a 2 (an empty target square) or a 6 (a robot in a target square) the game is not yet solved, so the method returns `False`. 
# If no such square is present in the grid, all target squares must be occupied by boxes, the game is solved, and the method returns `True`.

# If the player solves the game, we should display an appropriate message with the `draw_window` method:

    def draw_window(self):
        ...
        if self.game_solved():
            game_text = self.game_font.render("Congratulations, you solved the game!", True, (255, 0, 0))
            game_text_x = self.scale * self.width / 2 - game_text.get_width() / 2
            game_text_y = self.scale * self.height / 2 - game_text.get_height() / 2
            pygame.draw.rect(self.window, (0, 0, 0), (game_text_x, game_text_y, game_text.get_width(), game_text.get_height()))
            self.window.blit(game_text, (game_text_x, game_text_y))
        ...
        
# For completeness' sake, let's also change the `move` method so that the player can no longer move when they have solved the game:
    def move(self, move_y, move_x):
        if self.game_solved():
            return
        ...

# The player can still see the game grid and the final state of the game, however.

# A hint for testing

# When developing games it often happens that you'd want to check what happens in some later situation in the game. 
# For example, in this game the moment where the game is solved is one such situation.

# It can be difficult to test the correct functioning of a situation like that, as you'd normally have to solve the game to reach that point in the game. 
# As programmers we can make some temporary alleviations in our games, to make it easier to test them. 
# For example, we could add the following to make it temporarily easier to solve the game:
    def game_solved(self):
        return True

# Now the method always returns `True`, which means that the game is "solved" to begin with. 
# This makes it easy to check that the notification at the end looks good and the player can no longer move on the grid after solving. 
# When this functionality is thoroughly tested, we can revoke the changes.

# Your game on GitHub?

# The game is now finished. If you want an easy way to play around with the code and images, you can retrieve the source code from GitHub:

# [https://github.com/moocfi/sokoban](https://github.com/moocfi/sokoban)

# GitHub is a popular place for many kinds of programming projects. 
# It can be used to store the source code and other materials of all your own programming projects as well, and your program will then be maintained through git version control, and it can be easily shared with others. 
# You will become very familiar with git and GitHub if you continue on to other mooc.fi programming courses.

# How many moves are required?

# The grid in this game is quite small, but the game is not all that easy. 
# The first challenge is simply passing the game, but the next stage is trying to do so with as few moves as possible. 
# How short is the shortest path to a solution?

# Looking for the shortest possible solution is not an easy task at all, but there are computational solutions to this as well. 
# They are one of the subjects of the _Data Structures and Algorithms_ course.

# Final Code - English
import pygame

class Sokoban:
    def __init__(self):
        pygame.init()
        
        self.load_images()
        self.new_game()
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()

        window_height = self.scale * self.height
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))
        
        self.game_font = pygame.font.SysFont("Arial", 24)

        pygame.display.set_caption("Sokoban")

        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["floor", "wall", "target", "box", "robot copy", "done", "target_robot"]:
            self.images.append(pygame.image.load("Images\\Pygame\\" + name + ".png"))

    def new_game(self):
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
                    [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
        self.moves = 0
    
    def find_robot(self ):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [4, 6]:
                    return (y, x)
    
    def move(self, move_y, move_x):
        if self.game_solved():
            return
                
        robot_old_y, robot_old_x = self.find_robot() 
        robot_new_y = robot_old_y + move_y
        robot_new_x = robot_old_x + move_x
        
        # If the movement attempts to move the robot into a wall, movement is unsuccessful - Game state remains unchanged
        if self.map[robot_new_y][robot_new_x] == 1:
            return

        # If the movement attempts to move the robot to change the location of the box or moves into "done", new box coordinates are computed (continue)
        if self.map[robot_new_y][robot_new_x] in [3, 5]:
            box_new_y = robot_new_y + move_y
            box_new_x = robot_new_x + move_x

            # If the box moves into a wall, or into another box or into the "done" location, movement is unsuccessful
            if self.map[box_new_y][box_new_x] in [1, 3, 5]:
                return

            # If the path is clear and the movement is legal, the state of the map is changed with box in the new location and box removed from the old location where the robot is now positioned
            # NB: when the box moves onto a target block (index = 2), the + 3 updates the map location to 5 on the map and the clever ordering of the image index displays the 'done' image (index = 5).
            self.map[robot_new_y][robot_new_x] -= 3
            self.map[box_new_y][box_new_x] += 3

        # The robot occupies the space of the new coordinate and is removed from the previous coordinate. 
        # The successfully moved locations are now "floors" indexed as "0" in the map attribute/variable.
        # This applies to all legal moves with or without box movements.
        # NB: when the robot moves onto a target block (index = 2), the + 4 updates the map location to 6 on the map and the clever ordering of the image index displays the 'target_robot' image (index = 6).
        self.map[robot_old_y][robot_old_x] -= 4
        self.map[robot_new_y][robot_new_x] += 4
        
        self.moves += 1
    
    def game_solved(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [2, 6]:
                    return False
        return True            

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move(1, 0)
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()                

            if event.type == pygame.QUIT:
                exit()

    def draw_window(self):
        self.window.fill((0, 0, 0))

        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                self.window.blit(self.images[square], (x * self.scale, y * self.scale))
        
        game_text = self.game_font.render("Moves: " + str(self.moves), True, (255, 0, 0))
        self.window.blit(game_text, (25, self.height * self.scale + 10))

        game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (200, self.height * self.scale + 10))

        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + 10))
        
        if self.game_solved():
            game_text = self.game_font.render("Congratulations, you solved the game!", True, (255, 0, 0))
            game_text_x = self.scale * self.width / 2 - game_text.get_width() / 2
            game_text_y = self.scale * self.height / 2 - game_text.get_height() / 2
            pygame.draw.rect(self.window, (0, 0, 0), (game_text_x, game_text_y, game_text.get_width(), game_text.get_height()))
            self.window.blit(game_text, (game_text_x, game_text_y))        

        pygame.display.flip()

if __name__ == "__main__":
    Sokoban()