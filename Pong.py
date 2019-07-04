import pygame
import random
import sys


class MovingObject:
    """ This class includes all components, which are used by both Player and Ball """
    speed_of_moving = 7

    def __init__(self, x_axis, y_axis, board, color=(255, 255, 255)):
        self.default_x_axis = int(x_axis / 2)
        self.default_y_axis = int(y_axis / 2)
        self.position = [self.default_x_axis, self.default_y_axis]
        self.board_ref = board
        self.color = color

    def reset_position(self):
        self.position = [self.default_x_axis, self.default_y_axis]


class Player(MovingObject):
    height_of_rect = 100
    width_of_rect = 15
    score = 0
    bounce = False

    def __init__(self, x_axis, y_axis, board, color):
        MovingObject.__init__(self, x_axis, y_axis - self.height_of_rect, board, color)

    def update_position(self, up, down):
        if 0 <= self.position[1] + (up - down) * self.speed_of_moving <= pygame.Surface.get_height(self.board_ref) - self.height_of_rect:
            self.position[1] += (up - down) * self.speed_of_moving

    def display(self):
        pygame.draw.rect(self.board_ref, self.color, self.position + [self.width_of_rect, self.height_of_rect])


class Ball(MovingObject):
    radius = 5

    def __init__(self, width, height, board):
        MovingObject.__init__(self, width, height, board)
        self.x_way = random.choice([-1, 1])
        self.y_way = random.choice([-1, 1])
        self.speed_of_moving = 4

    def update_position(self):
        if self.position[1] - self.radius <= 0 or self.position[1] + self.radius >= pygame.Surface.get_height(self.board_ref):
            self.y_way *= -1

        self.position[0] += self.x_way * self.speed_of_moving
        self.position[1] += self.y_way * self.speed_of_moving

    def display(self):
        pygame.draw.circle(self.board_ref, self.color, self.position, self.radius)


class Game:
    delay = 10
    play = True
    last_mouse_pos = 0
    computer_mode = False
    difficulty_level = 7

    def __init__(self):
        """ Configuration by text file: """
        try:
            file = open('config.txt', 'r')
            content = file.read().split(' ')
            if int(content[0]) < 800 or int(content[1]) < 600:
            	raise FileNotFoundError
        except FileNotFoundError:
            content = [800, 600]
        self.width = int(content[0])
        self.height = int(content[1])

        """ Generate a game board with sizes set in configuration: """
        pygame.init()
        self.board = pygame.display.set_mode((self.width, self.height))

        """ Define main components: """
        self.players = [Player(30, self.height, self.board, (255, 0, 0)),
                        Player(2 * self.width - 60, self.height, self.board, (0, 0, 255))]
        self.ball = Ball(self.width, self.height, self.board)

        """ Run main loop: """
        self.engine()

    def screen_refresh(self):
        pygame.Surface.fill(self.board, (0, 0, 0))
        self.players[0].display()
        self.players[1].display()
        self.board.blit(pygame.font.Font.render(pygame.font.Font(pygame.font.match_font("consolas"), 50),
                                                (str(self.players[0].score) + " : " + str(self.players[1].score)),
                                                True, (50, 50, 50)), (self.width / 2 - 50, self.height / 2 - 25))
        self.ball.display()

        # If the first player bounce the ball by the front side:
        if self.ball.position[0] - self.ball.radius <= self.players[0].position[0] + self.players[0].width_of_rect and \
           self.players[0].position[1] <= self.ball.position[1] <= self.players[0].position[1] + self.players[0].height_of_rect and self.players[0].bounce == False:
            self.ball.x_way = 1
            self.players[0].bounce = True
            self.players[1].bounce = False
        # If the first player bounce the ball by the corner: 
        elif self.ball.position[0] - self.ball.radius <= self.players[0].position[0] + self.players[0].width_of_rect and \
        self.players[0].position[1] - self.ball.radius <= self.ball.position[1] <= self.players[0].position[1] + self.players[0].height_of_rect + self.ball.radius and self.players[0].bounce == False:
            self.ball.x_way = 1
            # top corner: 
            if self.ball.position[1] > self.players[0].position[1] + self.players[0].height_of_rect/2:
            	self.ball.y_way = 1
            # bottom corner
            else:
            	self.ball.y_way = -1
            self.players[0].bounce = True
            self.players[1].bounce = False
        # Otherwise, if they misses:
        elif self.ball.position[0] - self.ball.radius <= 0:
            self.players[1].score += 1
            self.reset_all()

        # If the second player bounce the ball by the front side:
        if self.ball.position[0] + self.ball.radius >= self.players[1].position[0] and \
        self.players[1].position[1] <= self.ball.position[1] <= self.players[1].position[1] + self.players[1].height_of_rect and self.players[1].bounce == False:
            self.ball.x_way = -1
            self.players[1].bounce = True
            self.players[0].bounce = False
        # If the second player bounce the ball by the corner: 
        elif self.ball.position[0] + self.ball.radius >= self.players[1].position[0] and \
            self.players[1].position[1] - self.ball.radius <= self.ball.position[1] <= self.players[1].position[1] + self.players[1].height_of_rect + self.ball.radius and self.players[1].bounce == False:
            self.ball.x_way = -1
            # top corner: 
            if self.ball.position[1] > self.players[1].position[1] + self.players[1].height_of_rect/2:
            	self.ball.y_way = 1
            # bottom corner
            else:
            	self.ball.y_way = -1
            self.players[1].bounce = True
            self.players[0].bounce = False
        # Otherwise, if they misses:
        elif self.ball.position[0] + self.ball.radius >= self.width:
            self.players[0].score += 1
            self.reset_all()

        pygame.display.update()

    def listen_input(self):
        pygame.event.get()
        keys = pygame.key.get_pressed()

        """ 'ESCAPE' => Quit the game """
        if keys[pygame.K_ESCAPE]:
            self.play = False
            sys.exit()

        """ '1'-'9' => Set speed of ball """
        for i in range(9):
            if keys[pygame.K_1 + i]:
                self.ball.speed_of_moving = i + 1;

        """ 'r' => Reset the score board """
        if keys[pygame.K_r]:
            self.players[0].score = 0
            self.players[1].score = 0

        """ 'p' => pause the game """
        if keys[pygame.K_p]:
            """ 'SPACE' => resume the game '"""
            while not keys[pygame.K_SPACE]:
                pygame.event.get()
                keys = pygame.key.get_pressed()
                pygame.time.delay(self.delay)

        """ 'TAB' => computer mode ON """
        if keys[pygame.K_TAB] and not self.computer_mode:
            self.computer_mode = True

        """ 'q' => computer mode OFF """
        if keys[pygame.K_q] and self.computer_mode:
            self.computer_mode = False

        """ 'x' => difficulty level = EASY """
        if keys[pygame.K_x]:
            self.difficulty_level = 4

        """ 'y' => difficulty level = MEDIUM """
        if keys[pygame.K_y]:
            self.difficulty_level = 7

        """ 'z' => difficulty level = HARD """
        if keys[pygame.K_z]:
            self.difficulty_level = 0

        if not self.computer_mode:
            """ Control first player using arrows """
            self.players[0].update_position(keys[pygame.K_DOWN], keys[pygame.K_UP])
            self.players[0].update_position(keys[pygame.K_s], keys[pygame.K_w])
        else:
            self.emulate_input()

        """ Control second player using mouse """
        mouse = pygame.mouse.get_pos()
        if 0 <= mouse[1] <= self.height - self.players[1].height_of_rect:
            self.players[1].position[1] = mouse[1]

    def emulate_input(self):
        if self.difficulty_level == 0:
            """ Level HARD: """
            if self.ball.x_way == 1:
                """ If the ball is moving away, set in the middle """
                if self.players[0].position[1] + self.players[0].height_of_rect/2 > self.height/2:
                    self.players[0].update_position(0, 1)
                elif self.players[0].position[1] + self.players[0].height_of_rect/2 < self.height/2 - self.height/100:
                    self.players[0].update_position(1, 0)
            elif self.ball.position[0] < self.width/2:
                """ Else carefully follow the ball"""
                if self.players[0].position[1] + self.players[0].height_of_rect/2 < self.ball.position[1] and self.ball.y_way == 1:
                    self.players[0].update_position(1, 0)
                elif self.players[0].position[1] + self.players[0].height_of_rect/2 > self.ball.position[1] and self.ball.y_way == -1:
                    self.players[0].update_position(0, 1)
        else:
            """ Level MEDIUM/EASY"""
            if self.ball.x_way == -1 and self.ball.position[0] < self.width/2:
                """" If the ball approaches, follow it with specified accuracy """
                if self.players[0].position[1] + self.players[0].height_of_rect/2 < self.ball.position[1]:
                    if random.randint(1, 10) < self.difficulty_level:
                        self.players[0].update_position(1, 0)
                elif self.players[0].position[1] + self.players[0].height_of_rect/2 > self.ball.position[1]:
                    if random.randint(1, 10) < 7:
                        self.players[0].update_position(0, 1)

    def reset_all(self):
        """ Reset the whole round: """
        self.players[0].reset_position()
        self.players[1].reset_position()
        self.players[0].bounce = False
        self.players[1].bounce = False
        self.ball.x_way = random.choice([-1, 1])
        self.ball.y_way = random.choice([-1, 1])
        self.ball.reset_position()
        self.screen_refresh()

    def engine(self):
        """ The main loop: """
        while self.play:
            self.screen_refresh()
            self.listen_input()
            self.ball.update_position()
            pygame.time.delay(self.delay)


if __name__ == "__main__":
    Game()