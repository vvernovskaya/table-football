import math
import tkinter as tk
from random import randrange as rnd
from random import randrange as rnd, choice

WINDOW_SIZE = (900, 700)
FIELD_SIZE = (860, 600)


class Ball():
    def __init__(self, canvas):  # k - velocity rise coefficient
        # self.life == 0 if there are no balls on the field
        self.canvas = canvas
        self.x = rnd(0, 800)
        self.y = rnd(60, 600)
        self.r = 10
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)

        self.id = self.canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill='white', outline='black')

    def coords(self):
        self.canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def remove_ball(self):
        self.canvas.delete(self.id)

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


class RedFootballers:
    def __init__(self, canvas):
        self.canvas = canvas

        self.score = 0

        # sticks
        self.id = self.canvas.create_rectangle(270, 0, 280, 600, fill='grey')
        self.id = self.canvas.create_rectangle(520, 0, 530, 600, fill='grey')
        self.id = self.canvas.create_rectangle(750, 0, 760, 600, fill='grey')

        # footballers' x coords
        self.x1 = 275
        self.x2 = 525
        self.x3 = 755

        self.y1 = 160
        self.y2 = 160
        self.y3 = 320

        self.dy = 160

        self.r = 30

        self.id = self.canvas.create_oval(self.x1 - self.r, self.y1 - self.r,
                                          self.x1 + self.r, self.y1 + self.r,
                                          fill='red')
        self.id = self.canvas.create_oval(self.x1 - self.r,
                                          self.dy + self.y1 - self.r,
                                          self.x1 + self.r,
                                          self.y1 + self.dy + self.r,
                                          fill='red')
        self.id = self.canvas.create_oval(self.x1 - self.r,
                                          2 * self.dy + self.y1 - self.r,
                                          self.x1 + self.r,
                                          2 * self.dy + self.y1 + self.r,
                                          fill='red')

        self.id = self.canvas.create_oval(self.x2 - self.r, self.y2 - self.r,
                                          self.x2 + self.r, self.y2 + self.r,
                                          fill='red')
        self.id = self.canvas.create_oval(self.x2 - self.r,
                                          self.dy + self.y1 - self.r,
                                          self.x2 + self.r,
                                          self.dy + self.y1 + self.r,
                                          fill='red')
        self.id = self.canvas.create_oval(self.x2 - self.r,
                                          2 * self.dy + self.y1 - self.r,
                                          self.x2 + self.r,
                                          2 * self.dy + self.y1 + self.r,
                                          fill='red')

        self.id = self.canvas.create_oval(self.x3 - self.r, self.y3 - self.r,
                                          self.x3 + self.r, self.y3 + self.r,
                                          fill='red')

    def bind(self):  # bind button press and release
        pass

    def update(self):
        self.y1 = self.canvas.get_mouse_coords[1] - self.dy
        self.y2 = self.canvas.get_mouse_coords[1] - self.dy
        self.y3 = self.canvas.get_mouse_coords[1]


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
        self.red_footballers = RedFootballers(self)
        self.blue_footballers = BlueFootballers(self)
        self.ball = None

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

    def new_ball(self):
        self.ball = Ball(self)

    def start(self):
        pass

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

    def update(self):  # put root.after here
        pass


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

    def new_game(self):
        pass

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

    def new_game(self):
        pass


app = App()
app.new_game()
app.mainloop()
