import copy
import math
import pickle
from random import randrange as rnd
from random import randrange as rnd, choice
import socket
import time

WINDOW_SIZE = (900, 650)
FIELD_SIZE = (860, 600)
DT = 30


class Ball:
    def __init__(self, compute):  # k - velocity rise coefficient
        # self.life == 0 if there are no balls on the field
        self.compute = compute
        self.x = rnd(70, 850)
        self.y = rnd(60, 500)
        self.r = 20
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)

        self.live = 1

    def hit(self):
        print('hit')
        print('start vx ', self.vx)
        self.vx = -self.vx
        self.vy = -self.vy + self.compute.red_footballers.vy
        if self.vx <= 0:
            self.vx -= abs(9*self.compute.cos)
            self.x -= 5
        else:
            self.vx += abs(3*self.compute.cos)
            self.x += 5
        print(self.vx)
        self.update()

    def update(self):
        if self.y >= 600 or self.y <= 0:
            if self.y >= 600:
                self.y = 595

            if self.y <= 0:
                self.y = 5

            self.vy = -self.vy

        if self.x >= 850 or self.x <= 50:
            if self.x >= 850:
                self.x = 835

            if self.x <= 50:
                self.x = 55

            self.vx = -self.vx

        self.vx = 0.99*self.vx
        self.vy = 0.99*self.vy
        self.x += self.vx
        self.y += self.vy

    def remove_ball(self):
        self.live = 0


class Footballer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 30


class RedFootballers:
    def __init__(self, compute):
        self.compute = compute
        self.score = 0

        self.mouse_coords = [None, None]

        # footballers' x coords
        self.y1 = 160
        self.y2 = 160
        self.y3 = 320

        self.dy = 160

        self.r = 30

        self.vy = 0
        self.pry = 0

        self.f1 = Footballer(275, self.y1)
        self.f2 = Footballer(275, self.dy + self.y1)
        self.f3 = Footballer(275, 2 * self.dy + self.y1)
        self.f4 = Footballer(525, self.y2)
        self.f5 = Footballer(525, self.dy + self.y1)
        self.f6 = Footballer(525, 2 * self.dy + self.y1)
        self.f7 = Footballer(755, self.y3)

        self.footballers = [self.f1, self.f2, self.f3, self.f4, self.f5,
                            self.f6, self.f7]

    def update_each_footballer(self):
        self.f1.y = self.y1
        self.f2.y = self.dy + self.y1
        self.f3.y = 2 * self.dy + self.y1
        self.f4.y = self.y2
        self.f5.y = self.dy + self.y1
        self.f6.y = 2 * self.dy + self.y1
        self.f7.y = self.y3

    def update(self):
        self.mouse_coords = self.compute.recv_data['mouse_coords_red']
        self.pry = copy.deepcopy(self.y1)
        self.y1 = self.mouse_coords[1] - self.dy
        self.y2 = self.mouse_coords[1] - self.dy
        self.y3 = self.mouse_coords[1]

        self.vy = self.y1 - self.pry
        self.update_each_footballer()


class BlueFootballers:
    def __init__(self, compute):
        self.compute = compute
        self.mouse_coords = [None, None]

        self.score = 0

        self.y3 = 160
        self.y2 = 160
        self.y1 = 320

        self.dy = 160

        self.r = 30

        self.vy = 0
        self.pry = 0

        self.f1 = Footballer(655, self.y2)
        self.f2 = Footballer(655, self.dy + self.y2)
        self.f3 = Footballer(655, 2 * self.dy + self.y2)
        self.f4 = Footballer(405, self.y3)
        self.f5 = Footballer(405, self.dy + self.y3)
        self.f6 = Footballer(405, 2 * self.dy + self.y3)
        self.f7 = Footballer(155, self.y1)

        self.footballers = [self.f1, self.f2, self.f3, self.f4, self.f5,
                            self.f6, self.f7]

    def update_each_footballer(self):
        self.f1.y = self.y1
        self.f2.y = self.dy + self.y1
        self.f3.y = 2 * self.dy + self.y1
        self.f4.y = self.y2
        self.f5.y = self.dy + self.y1
        self.f6.y = 2 * self.dy + self.y1
        self.f7.y = self.y3

    def update(self):
        self.mouse_coords = self.compute.recv_data['mouse_coords_blue']
        self.pry = copy.deepcopy(self.y1)
        self.y1 = self.mouse_coords[1] - self.dy
        self.y2 = self.mouse_coords[1] - self.dy
        self.y3 = self.mouse_coords[1]

        self.vy = self.y1 - self.pry
        self.update_each_footballer()


class GameComputation:
    def __init__(self):
        self.ball = None
        self.red_footballers = None
        self.blue_footballers = None

        self.recv_data = None

        self.restart = 0

        self.mouse_coords = [None, None]
        self.an = None
        self.sin = None
        self.cos = None

        self.score_red = 0
        self.score_blue = 0
        self.ball.live = 1

        self.data = {'ball_x': self.ball.x, 'ball_y': self.ball.y, 'ball_live':
            self.ball.live, 'red_footb_y': self.red_footballers.y +
                                           self.red_footballers.dy,
                     'blue_footb_y': self.blue_footballers.y + self.blue_footballers.dy,
                     'score_red': self.red_footballers.score,
                     'score_blue': self.blue_footballers.score,
                     'restart': self.restart}

    def start(self):
        print('start')
        self.restart = 0
        self.ball = Ball(self)
        self.red_footballers = RedFootballers(self)
        self.blue_footballers = BlueFootballers(self)
        self.update()

    def remove_ball(self):
        self.ball.remove_ball()
        self.red_footballers.remove_footballers()
        self.blue_footballers.remove_footballers()

    def restart_game(self):
        self.restart = 1
        self.remove_ball()
        time.sleep(1.5)
        self.start()

    def check_goal(self):
        if (self.ball.y >= 210) and (self.ball.y <= 390):
            if self.ball.x >= 815:
                self.score_red += 1
                self.restart_game()
            if self.ball.x <= 75:
                self.score_blue += 1
                self.restart_game()

    def check_hit(self):
        for i in range(len(self.red_footballers.footballers)):
            if (self.ball.x - self.red_footballers.footballers[i].x) ** 2 + \
                    (self.ball.y - self.red_footballers.footballers[i].y) ** 2 \
                    <= (
                    self.ball.r + self.red_footballers.footballers[i].r) ** 2:
                self.mouse_coords = self.recv_data['mouse_coords_red']
                dx = self.mouse_coords[0] - self.red_footballers.footballers[i].x
                dy = self.mouse_coords[1] - self.red_footballers.footballers[i].y
                if dx != 0:
                    self.an = math.atan2(dy, dx)
                    self.sin = dy / math.sqrt(dx**2 + dy**2)
                    self.cos = dx / math.sqrt(dx**2 + dy**2)
                else:
                    self.an = 1
                    self.sin = 0
                    self.cos = 0

                self.ball.hit()

        for i in range(len(self.blue_footballers.footballers)):
            if (self.ball.x - self.blue_footballers.footballers[i].x) ** 2 + \
                    (self.ball.y - self.blue_footballers.footballers[i].y) ** 2 \
                    <= (
                    self.ball.r + self.blue_footballers.footballers[i].r) ** 2:
                self.mouse_coords = self.recv_data['mouse_coords_blue']
                dx = self.mouse_coords[0] - self.blue_footballers.footballers[i].x
                dy = self.mouse_coords[1] - self.blue_footballers.footballers[i].y
                if dx != 0:
                    self.an = math.atan2(dy, dx)
                    self.sin = dy / math.sqrt(dx**2 + dy**2)
                    self.cos = dx / math.sqrt(dx**2 + dy**2)
                else:
                    self.an = 1
                    self.sin = 0
                    self.cos = 0

                self.ball.hit()

    def update(self):  # put root.after here
        self.ball.update()
        self.red_footballers.update()
        self.blue_footballers.update()
        self.check_hit()
        self.check_goal()
        time.sleep(0.02)
        self.update()


HOST = '' # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
i = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)
    while i < 2:
        i += 1
        conn, addr = s.accept()

game = GameComputation()
game.start()
