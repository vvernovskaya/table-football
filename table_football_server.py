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
        self.x = -60
        self.y = -60


class Footballer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 30

    def remove(self):
        self.x = -50
        self.y = -50

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
        self.mouse_coords = self.compute.recv_data_red
        self.pry = copy.deepcopy(self.y1)
        self.y1 = self.mouse_coords[1] - self.dy
        self.y2 = self.mouse_coords[1] - self.dy
        self.y3 = self.mouse_coords[1]

        self.vy = self.y1 - self.pry
        self.update_each_footballer()

    def remove_footballers(self):
        print('remove footb')
        for i in range(len(self.footballers)):
            self.footballers[i].remove()


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
        self.mouse_coords = self.compute.recv_data_blue
        self.pry = copy.deepcopy(self.y1)
        self.y1 = self.mouse_coords[1] - self.dy
        self.y2 = self.mouse_coords[1] - self.dy
        self.y3 = self.mouse_coords[1]

        self.vy = self.y1 - self.pry
        self.update_each_footballer()

    def remove_footballers(self):
        print('remove footb')
        for i in range(len(self.footballers)):
            self.footballers[i].remove()


class GameComputation:
    def __init__(self):
        self.ball = None
        self.red_footballers = None
        self.blue_footballers = None

        self.recv_data_red = None
        self.recv_data_blue = None

        self.restart = 0

        self.mouse_coords = [None, None]
        self.an = None
        self.sin = None
        self.cos = None

        self.score_red = 0
        self.score_blue = 0
        self.live = 1

        self.data = None

    def start(self):
        print('start')
        self.restart = 0
        self.ball = Ball(self)
        self.red_footballers = RedFootballers(self)
        self.blue_footballers = BlueFootballers(self)
        self.update_data()

    def update_data(self):
        self.data = {'ball_x': self.ball.x, 'ball_y': self.ball.y, 'ball_live':
            self.live, 'red_footb_y': self.red_footballers.y1 +
                                           self.red_footballers.dy,
                     'blue_footb_y': self.blue_footballers.y1 + self.blue_footballers.dy,
                     'score_red': self.score_red,
                     'score_blue': self.score_blue,
                     'restart': self.restart}

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
                self.score_blue += 1
                self.restart_game()
            if self.ball.x <= 75:
                self.score_red += 1
                self.restart_game()

    def check_hit(self):
        for i in range(len(self.red_footballers.footballers)):
            if (self.ball.x - self.red_footballers.footballers[i].x) ** 2 + \
                    (self.ball.y - self.red_footballers.footballers[i].y) ** 2 \
                    <= (
                    self.ball.r + self.red_footballers.footballers[i].r) ** 2:
                self.mouse_coords = self.recv_data_red
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
                self.mouse_coords = self.recv_data_blue
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

    def update(self, data_red, data_blue):  # put root.after here
        self.recv_data_red = data_red
        self.recv_data_blue = data_blue
        self.ball.update()
        self.red_footballers.update()
        self.blue_footballers.update()
        self.check_hit()
        self.check_goal()
        self.update_data()
        time.sleep(0.02)

HOST = '' # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
i = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)
    conn1, addr1 = s.accept()
    conn2, addr2 = s.accept()
    color1 = conn1.recv(1024)
    color2 = conn2.recv(1024)
    color1 = pickle.loads(color1)
    color2 = pickle.loads(color2)

    conn_red = None
    conn_blue = None
    addr_red = None
    addr_blue = None

    recv_data_red = None
    recv_data_blue = None

    data_to_send = None

    if color1 == 'red':
        conn_red, addr_red = conn1, addr1
    else:
        conn_blue, addr_blue = conn1, addr1

    if color2 == 'red':
        conn_red, addr_red = conn2, addr2
    else:
        conn_blue, addr_blue = conn2, addr2

    game = GameComputation()
    game.start()
    while True:
        data_to_send = pickle.dumps(game.data)
        conn_red.sendall(data_to_send)
        conn_blue.sendall(data_to_send)
        print('i sent the data')
        recv_data_red = conn_red.recv(1024)
        recv_data_blue = conn_blue.recv(1024)
        print('i got the data')
        recv_data_red = pickle.loads(recv_data_red)
        recv_data_blue = pickle.loads(recv_data_blue)
        game.update(recv_data_red, recv_data_blue)

