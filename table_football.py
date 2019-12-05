import math
import tkinter as tk
from random import randrange as rnd
from random import randrange as rnd, choice

WINDOW_SIZE = (900, 700)
FIELD_SIZE = (860, 600)
DT = 30


class Ball:
    def __init__(self, canvas):  # k - velocity rise coefficient
        # self.life == 0 if there are no balls on the field
        self.canvas = canvas
        self.x = rnd(70, 850)
        self.y = rnd(60, 500)
        self.r = 20
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)

        self.id = self.canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill='white', outline='black')

    def update_coords(self):
        self.canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )
        print("coords updated")
        self.canvas.master.master.update()

    def remove_ball(self):
        self.canvas.delete(self.id)

    def hit(self):
        self.vx = -self.vx
        self.vy = -self.vy
        self.update_coords()

    def update(self):
        if self.y >= 600 or self.y <= 0:
            self.vy = -self.vy
            if self.y >= 600:
                self.y = 595

            if self.y <= 0:
                self.y = 5

        if self.x >= 800 or self.x <= 0:
            self.vx = -self.vx
            if self.x >= 860:
                self.x = 855

            if self.x <= 0:
                self.x = 5

        self.x += self.vx
        self.y += self.vy

        self.update_coords()


class Footballer:
    def __init__(self, canvas, x, y):
        self.canvas = canvas

        self.x = x
        self.y = y
        self.r = 30

        self.id = self.canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill='red')

    def update_coords(self):
        self.canvas.coords(self.id,
                           self.x - self.r,
                           self.y - self.r,
                           self.x + self.r,
                           self.y + self.r)


class RedFootballers:
    def __init__(self, canvas):
        self.canvas = canvas

        self.score = 0

        self.mouse_coords = [None, None]

        # sticks
        self.id = self.canvas.create_rectangle(270, 0, 280, 600, fill='grey')
        self.id = self.canvas.create_rectangle(520, 0, 530, 600, fill='grey')
        self.id = self.canvas.create_rectangle(750, 0, 760, 600, fill='grey')

        # footballers' x coords
        self.y1 = 160
        self.y2 = 160
        self.y3 = 320

        self.dy = 160

        self.r = 30

        self.f1 = Footballer(canvas, 275, self.y1)
        self.f2 = Footballer(canvas, 275, self.dy + self.y1)
        self.f3 = Footballer(canvas, 275, 2 * self.dy + self.y1)
        self.f4 = Footballer(canvas, 525, self.y2)
        self.f5 = Footballer(canvas, 525, self.dy + self.y1)
        self.f6 = Footballer(canvas, 525, 2 * self.dy + self.y1)
        self.f7 = Footballer(canvas, 755, self.y3)

        self.footballers = [self.f1, self.f2, self.f3, self.f4, self.f5,
                            self.f6, self.f7]

    def bind(self):  # bind button press and release
        pass

    def update_each_footballer(self):
        self.f1.y = self.y1
        self.f2.y = self.dy + self.y1
        self.f3.y = 2 * self.dy + self.y1
        self.f4.y = self.y2
        self.f5.y = self.dy + self.y1
        self.f6.y = 2 * self.dy + self.y1
        self.f7.y = self.y3

    def update(self):
        self.mouse_coords = self.canvas.get_mouse_coords()
        print(self.mouse_coords)
        self.y1 = self.mouse_coords[1] - self.dy
        self.y2 = self.mouse_coords[1] - self.dy
        self.y3 = self.mouse_coords[1]

        self.update_each_footballer()

        for i in range(len(self.footballers)):
            self.footballers[i].update_coords()


class BlueFootballers:
    def __init__(self, canvas):
        self.canvas = canvas

        self.score = 0

        self.id = self.canvas.create_rectangle(150, 0, 160, 600, fill='grey')
        self.id = self.canvas.create_rectangle(400, 0, 410, 600, fill='grey')
        self.id = self.canvas.create_rectangle(650, 0, 660, 600, fill='grey')

        self.x1 = 155
        self.x2 = 405
        self.x3 = 655

        self.y1 = 160
        self.y2 = 160
        self.y3 = 320

        self.dy = 160

        self.r = 30

        self.id = self.canvas.create_oval(self.x3 - self.r, self.y1 - self.r,
                                          self.x3 + self.r, self.y1 + self.r,
                                          fill='blue')
        self.id = self.canvas.create_oval(self.x3 - self.r,
                                          self.dy + self.y1 - self.r,
                                          self.x3 + self.r,
                                          self.dy + self.y1 + self.r,
                                          fill='blue')
        self.id = self.canvas.create_oval(self.x3 - self.r,
                                          2 * self.dy + self.y1 - self.r,
                                          self.x3 + self.r,
                                          2 * self.dy + self.y1 + self.r,
                                          fill='blue')

        self.id = self.canvas.create_oval(self.x2 - self.r, self.y1 - self.r,
                                          self.x2 + self.r, self.y1 + self.r,
                                          fill='blue')
        self.id = self.canvas.create_oval(self.x2 - self.r,
                                          self.dy + self.y2 - self.r,
                                          self.x2 + self.r,
                                          self.dy + self.y2 + self.r,
                                          fill='blue')
        self.id = self.canvas.create_oval(self.x2 - self.r,
                                          2 * self.dy + self.y2 - self.r,
                                          self.x2 + self.r,
                                          2 * self.dy + self.y2 + self.r,
                                          fill='blue')

        self.id = self.canvas.create_oval(self.x1 - self.r, self.y3 - self.r,
                                          self.x1 + self.r, self.y3 + self.r,
                                          fill='blue')

    def bind(self):
        pass

    # def update(self):
    # self.y3 = self.canvas.get_mouse_coords[1] - self.dy
    # self.y2 = self.canvas.get_mouse_coords[1] - self.dy
    # self.y1 = self.canvas.get_mouse_coords[1]


class Field(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background="green")
        self.ball = None
        self.red_footballers = None
        self.blue_footballers = None

        self.out1 = self.create_rectangle(0, 0, 50, 250, fill="brown", width=2)
        self.out2 = self.create_rectangle(0, 350, 50, 600, fill="brown",
                                          width=2)
        self.out3 = self.create_rectangle(850, 0, 900, 250, fill="brown",
                                          width=2)
        self.out4 = self.create_rectangle(850, 350, 900, 600, fill="brown",
                                          width=2)

        self.goals1 = self.create_rectangle(0, 210, 50, 390, outline="black",
                                            fill="silver", width=2)
        self.goals2 = self.create_rectangle(850, 210, 900, 390,
                                            outline="black", fill="silver",
                                            width=2)

    def start(self):
        self.ball = Ball(self)
        self.red_footballers = RedFootballers(self)
        self.blue_footballers = BlueFootballers(self)

    def remove_ball(self):
        self.ball.remove_ball()

    def restart(self):
        self.remove_ball()
        self.start()

    def get_mouse_coords(self):
        abs_x = self.winfo_pointerx()
        abs_y = self.winfo_pointery()
        canvas_x = self.winfo_rootx()
        canvas_y = self.winfo_rooty()
        return [abs_x - canvas_x, abs_y - canvas_y]

    def goal(self):
        if (self.ball.y >= 210) and (self.ball.y <= 390):
            self.ball.remove_ball()
            if self.ball.x >= 855:
                self.master.red_goal()
            if self.ball.x <= 5:
                self.master.blue_goal()

    def check_hit(self):
        for i in range(len(self.red_footballers.footballers)):
            if (self.ball.x - self.red_footballers.footballers[i].x) ** 2 + \
                    (self.ball.y - self.red_footballers.footballers[i].x) ** 2 \
                    <= (
                    self.ball.r - self.red_footballers.footballers[i].r) ** 2:
                self.ball.hit()

    def update(self):  # put root.after here
        self.ball.update()
        self.red_footballers.update()
        self.after(20, self.update)


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.score_red = 0
        self.score_blue = 0

        self.score_red_text = 'Red: {}'
        self.score_blue_text = 'Blue: {}'

        self.score_red_label = tk.Label(
            self,
            text=self.score_red_text.format(self.score_red),
            font=("Times New Roman", 30)
        )
        self.score_blue_label = tk.Label(
            self,
            text=self.score_blue_text.format(self.score_blue),
            font=("Times New Roman", 30)
        )
        self.score_red_label.pack()
        self.score_blue_label.pack()

        self.field = Field(self)
        self.field.pack(fill=tk.BOTH, expand=1)

    def start_game(self):
        self.field.start()
        self.field.update()

    def stop(self):
        pass

    def red_goal(self):
        self.score_red += 1
        self.score_red_label['text'] = self.score_red_text.format(
            self.score_red)

    def blue_goal(self):
        self.score_blue += 1
        self.score_blue_label['text'] = self.score_blue_text.format(
            self.score_blue)

    def update(self):  # put root.after here
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(*WINDOW_SIZE))

        self.main_frame = MainFrame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

    def start_game(self):
        self.main_frame.start_game()


app = App()
app.start_game()
app.mainloop()
