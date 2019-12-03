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
        self.canvas.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

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

    def create_field(self):
        canv.field = canv.create_rectangle (100, 100, 800, 600, outline = "black", fill = "green", width = 2)

    def create_ball(self):
        r = 10
        canv.ball = canv.create_oval (450-r, 300-r, 450+r, 300+r, outline = "black",  fill = "blue", width = 2)
    
    def create_goals(self):
        canv.goals1 = canv.create_rectangle (0, 250, 50, 350, outline = "black", fill = "silver", width = 2)
        canv.goals2 = canv.create_rectangle (850, 250, 900, 350, outline = "black", fill = "silver", width = 2) 

    def out_of_goals(self):
        canv.out1 = canv.create_rectangle (0, 0, 50, 250, fill = "brown", width = 2)
        canv.out2 = canv.create_rectangle (0, 350, 50, 600, fill = "brown", width = 2)
        canv.out3 = canv.create_rectangle (850, 0, 900, 250, fill = "brown", width = 2)
        canv.out4 = canv.create_rectangle (850, 350, 900, 600, fill = "brown", width = 2)
    
    def rods():
        a = 5
        canv.rod1 = canv.create_rectpangle (135 - a, 100, 135 + a, 600, fill = "silver", width = 2)
        canv.rod2 = canv.create_rectpangle (225 - a, 100, 225 + a, 600, fill = "silver", width = 2)
        canv.rod3 = canv.create_rectpangle (315 - a, 100, 315 + a, 600, fill = "silver", width = 2)
        canv.rod4 = canv.create_rectpangle (405 - a, 100, 405 + a, 600, fill = "silver", width = 2)
        canv.rod5 = canv.create_rectpangle (495 - a, 100, 495 + a, 600, fill = "silver", width = 2)
        canv.rod6 = canv.create_rectpangle (585 - a, 100, 585 + a, 600, fill = "silver", width = 2)
        canv.rod7 = canv.create_rectpangle (675 - a, 100, 675 + a, 600, fill = "silver", width = 2)
        canv.rod8 = canv.create_rectpangle (765 - a, 100, 765 + a, 600, fill = "silver", width = 2)
          
    def remove_ball(self):
        pass

    def start(self):
        pass

    def restart(self):
        self.stop()
        self.remove_ball()
        self.start()
        
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
        self.battlefield.restart()
        
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
        
        self.main_frame = MainFrame(self.master)

    def new_game(self):
        pass

app = App()
app.new_game()
app.mainloop()
