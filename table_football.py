import math
import tkinter as tk
from random import randrange as rnd, choice


WINDOW_SIZE = (900, 600)
FIELD_SIZE = (860, 600)


class Ball():
    def __init__(self, canvas, x, y, vx, vy): # k - velocity rise coefficient
                                              # self.life == 0 if there are no balls on the field
        pass

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
        pass

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
        pass

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

