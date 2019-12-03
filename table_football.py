import math
import tkinter as tk
from random import randrange as rnd, choice


WINDOW_SIZE = (900, 600)
FIELD_SIZE = (860, 600)


class Ball():
    def __init__(self, canvas, x, y, vx, vy, color = None): # k - velocity rise coefficient
                                                            # self.life == 0 if there are no balls on the field
        super().__init__()
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
        if color is None:
            self.color = choice(['white'])
        else:
            self.color = color
            
        self.id = self.canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color)
    
    
    def coords(self):
        pass

    def check_walls(self):
        pass

    def hit_footballer(self):
        pass

    def goal(self):
        pass
    
    def update(self):
        pass

class RedFootballers():
    def __init__(self, canvas):

        # sticks
        self.id = canv.create_rectangle(270, 60, 280, 600, fill = 'grey')
        self.id = canv.create_rectangle(520, 60, 530, 600, fill = 'grey')
        self.id = canv.create_rectangle(750, 60, 760, 600, fill = 'grey')

        # footballers' x coords
        self.x1r = 275
        self.x2r = 525
        self.x3r = 755

        self.dx1 = 160
        self.dx3 = 320

        self.r = 30

        self.id = canv.create_oval(self.x1r - self.r, self.dx1 - self.r,
                                   self.x1r + self.r, self.dx1 + self.r,
                                   fill = 'red')
        self.id = canv.create_oval(self.x1r - self.r, 2*self.dx1 - self.r,
                                   self.x1r + self.r, 2*self.dx1 + self.r,
                                   fill = 'red')
        self.id = canv.create_oval(self.x1r - self.r, 3*self.dx1 - self.r,
                                   self.x1r + self.r, 3*self.dx1 + self.r,
                                   fill = 'red')

        self.id = canv.create_oval(self.x2r - self.r, self.dx1 - self.r,
                                   self.x2r + self.r, self.dx1 + self.r,
                                   fill = 'red')
        self.id = canv.create_oval(self.x2r - self.r, 2*self.dx1 - self.r,
                                   self.x2r + r, 2*self.dx1 + self.r,
                                   fill = 'red')
        self.id = canv.create_oval(self.x2r - self.r, 3*self.dx1 - self.r,
                                   self.x2r + self.r, 3*self.dx1 + self.r,
                                   fill = 'red')

        self.id = canv.create_oval(self.x3r - self.r, self.dx3 - self.r,
                                   self.x3r + self.r, self.dx3 + self.r,
                                   fill = 'red')

    def bind(self):
        pass

    def coords(self):
        pass

    def hit_ball(self):
        pass

    def update(self):
        pass

class BlueFootballers():
    def __init__(self, canvas):
        self.id = canv.create_rectangle(150, 60, 160, 600, fill = 'grey')
        self.id = canv.create_rectangle(400, 60, 410, 600, fill = 'grey')
        self.id = canv.create_rectangle(650, 60, 660, 600, fill = 'grey')

        self.x1b = 155
        self.x2b = 405
        self.x3b = 655

        self.id = canv.create_oval(self.x3b - self.r, self.dx1 - self.r,
                                   self.x3b + self.r, self.dx1 + self.r,
                                   fill = 'blue')
        self.id = canv.create_oval(self.x3b - self.r, 2*self.dx1 - self.r,
                                   self.x3b + self.r, 2*self.dx1 + self.r,
                                   fill = 'blue')
        self.id = canv.create_oval(self.x3b - self.r, 3*self.dx1 - self.r,
                                   self.x3b + self.r, 3*self.dx1 + self.r,
                                   fill='blue')

        self.id = canv.create_oval(self.x2b - self.r, self.dx1 - self.r,
                                   self.x2b + self.r, self.dx1 + self.r,
                                   fill = 'blue')
        self.id = canv.create_oval(self.x2b - self.r, 2*self.dx1 - self.r,
                                   self.x2b + self.r, 2*self.dx1 + self.r,
                                   fill = 'blue')
        self.id = canv.create_oval(self.x2b - self.r, 3*self.dx1 - self.r,
                                   self.x2b + self.r, 3*self.dx1 + self.r,
                                   fill='blue')

        self.id = canv.create_oval(self.x1b - self.r, self.dx3 - self.r,
                                   self.x1b + self.r, self.dx3 + self.r,
                                   fill = 'blue')

    def bind(self):
        pass

    def coords(self):
        pass

    def hit_ball(self):
        pass

    def update(self):
        pass

class Field(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background = "green")

    def create_ball(self):
        pass

    def remove_ball(self):
        pass

    def start(self):
        pass

    def restart(self):
        pass

    def get_mouse_coords(self):
        abs_x = self.winfo_pointerx()
        abs_y = self.winfo_pointery()
        canvas_x = self.winfo_rootx()
        canvas_y = self.winfo_rooty()
        return [abs_x - canvas_x, abs_y - canvas_y]

    def goal(self):
        pass

    def update(self): # put root.after here
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
            font=("Times New Roman", 36)
        )
        self.score_blue_label = tk.Label(
            self,
            text=self.score_blue_text.format(self.score_blue),
            font=("Times New Roman", 36)
        )
        self.score_red_label.pack()
        self.score_blue_label.pack()

    def new_game(self):
        pass

    def stop(self):
        pass

    def goal(self):
        pass

    def update(self): # put root.after here
        pass

    
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(*WINDOW_SIZE))

    def new_game(self):
        pass

