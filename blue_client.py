import tkinter as tk
import pickle
import socket
from tkinter import messagebox

WINDOW_SIZE = (900, 650)
FIELD_SIZE = (860, 600)
DT = 30


class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = self.canvas.recv_data['ball_x']
        self.y = self.canvas.recv_data['ball_y']
        self.r = 20

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
        self.canvas.master.master.update()

    def remove_ball(self):
        self.canvas.delete(self.id)

    def update(self):
        self.x = self.canvas.recv_data['ball_x']
        self.y = self.canvas.recv_data['ball_y']
        self.update_coords()


class Footballer:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas

        self.x = x
        self.y = y
        self.r = 30

        self.id = self.canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=color)

    def update_coords(self):
        self.canvas.coords(self.id,
                           self.x - self.r,
                           self.y - self.r,
                           self.x + self.r,
                           self.y + self.r)

    def remove(self):
        self.canvas.delete(self.id)


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

        self.vy = 0
        self.pry = 0

        self.f1 = Footballer(canvas, 275, self.y1, 'red')
        self.f2 = Footballer(canvas, 275, self.dy + self.y1, 'red')
        self.f3 = Footballer(canvas, 275, 2 * self.dy + self.y1, 'red')
        self.f4 = Footballer(canvas, 525, self.y2, 'red')
        self.f5 = Footballer(canvas, 525, self.dy + self.y1, 'red')
        self.f6 = Footballer(canvas, 525, 2 * self.dy + self.y1, 'red')
        self.f7 = Footballer(canvas, 755, self.y3, 'red')

        self.footballers = [self.f1, self.f2, self.f3, self.f4, self.f5,
                            self.f6, self.f7]

    def update_each_footballer(self):
        self.f1.y = self.canvas.recv_data['red_footb_y'] - self.dy
        self.f2.y = self.canvas.recv_data['red_footb_y']
        self.f3.y = self.canvas.recv_data['red_footb_y'] + self.dy
        self.f4.y = self.canvas.recv_data['red_footb_y'] - self.dy
        self.f5.y = self.canvas.recv_data['red_footb_y']
        self.f6.y = self.canvas.recv_data['red_footb_y'] + self.dy
        self.f7.y = self.canvas.recv_data['red_footb_y']

    def update(self):
        self.update_each_footballer()
        for i in range(len(self.footballers)):
            self.footballers[i].update_coords()

    def remove_footballers(self):
        for i in range(len(self.footballers)):
            self.footballers[i].remove()


class BlueFootballers:
    def __init__(self, canvas):
        self.canvas = canvas
        self.mouse_coords = [None, None]

        self.score = 0

        self.id = self.canvas.create_rectangle(150, 0, 160, 600, fill='grey')
        self.id = self.canvas.create_rectangle(400, 0, 410, 600, fill='grey')
        self.id = self.canvas.create_rectangle(650, 0, 660, 600, fill='grey')

        self.x1 = 155
        self.x2 = 405
        self.x3 = 655

        self.y3 = 160
        self.y2 = 160
        self.y1 = 320

        self.dy = 160

        self.r = 30

        self.vy = 0
        self.pry = 0

        self.f1 = Footballer(canvas, 655, self.y2, 'blue')
        self.f2 = Footballer(canvas, 655, self.dy + self.y2, 'blue')
        self.f3 = Footballer(canvas, 655, 2 * self.dy + self.y2, 'blue')
        self.f4 = Footballer(canvas, 405, self.y3, 'blue')
        self.f5 = Footballer(canvas, 405, self.dy + self.y3, 'blue')
        self.f6 = Footballer(canvas, 405, 2 * self.dy + self.y3, 'blue')
        self.f7 = Footballer(canvas, 155, self.y1, 'blue')

        self.footballers = [self.f1, self.f2, self.f3, self.f4, self.f5,
                            self.f6, self.f7]

    def update_each_footballer(self):
        self.f1.y = self.canvas.recv_data['blue_footb_y'] - self.dy
        self.f2.y = self.canvas.recv_data['blue_footb_y']
        self.f3.y = self.canvas.recv_data['blue_footb_y'] + self.dy
        self.f4.y = self.canvas.recv_data['blue_footb_y'] - self.dy
        self.f5.y = self.canvas.recv_data['blue_footb_y']
        self.f6.y = self.canvas.recv_data['blue_footb_y'] + self.dy
        self.f7.y = self.canvas.recv_data['blue_footb_y']

    def update(self):
        self.update_each_footballer()
        for i in range(len(self.footballers)):
            self.footballers[i].update_coords()

    def remove_footballers(self):
        for i in range(len(self.footballers)):
            self.footballers[i].remove()


class Field(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background="green")
        self.ball = None
        self.red_footballers = None
        self.blue_footballers = None

        self.recv_data = None

        self.mouse_coords = [None, None]
        self.an = None
        self.sin = None
        self.cos = None

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

        self.win_text = self.create_text(
            WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2, text='aaaa', font=360)

    def start(self, data):
        self.recv_data = data
        self.ball = Ball(self)
        self.red_footballers = RedFootballers(self)
        self.blue_footballers = BlueFootballers(self)
        self.update_canvas(self.recv_data)

    def remove_ball(self):
        self.ball.remove_ball()
        self.red_footballers.remove_footballers()
        self.blue_footballers.remove_footballers()

    def restart(self):
        self.remove_ball()
        self.after(1500, self.start(recv_data))

    def get_mouse_coords(self):
        abs_x = self.winfo_pointerx()
        abs_y = self.winfo_pointery()
        canvas_x = self.winfo_rootx()
        canvas_y = self.winfo_rooty()
        return [abs_x - canvas_x, abs_y - canvas_y]

    def check_win(self):
        if self.recv_data['score_red'] == 6:
            messagebox.showinfo("Winner", "Red team won!")
        if self.recv_data['score_blue'] == 6:
            messagebox.showinfo("Winner", "Blue team won!")

    def update_canvas(self, data):
        self.recv_data = data
        self.master.score_red_label[
            'text'] = self.master.score_red_text.format(
            self.recv_data['score_red'])
        self.master.score_blue_label[
            'text'] = self.master.score_blue_text.format(
            self.recv_data['score_blue'])
        self.ball.update()
        self.red_footballers.update()
        self.blue_footballers.update()


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
            font=("Times New Roman", 25)
        )
        self.score_blue_label = tk.Label(
            self,
            text=self.score_blue_text.format(self.score_blue),
            font=("Times New Roman", 25)
        )
        self.score_red_label.pack(side=tk.TOP)
        self.score_blue_label.pack(side=tk.TOP)

        self.field = Field(self)
        self.field.pack(fill=tk.BOTH, expand=1)

    def start_game(self, data):
        self.field.start(data)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(*WINDOW_SIZE))

        self.main_frame = MainFrame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

    def start_game(self, data):
        self.main_frame.start_game(data)



HOST = 'localhost'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    color = pickle.dumps('blue')
    s.sendall(color)

    app = App()
    recv_data = s.recv(1024)
    recv_data = pickle.loads(recv_data)
    app.start_game(recv_data)
    mouse_coords_blue = app.main_frame.field.get_mouse_coords()
    mouse_coords_blue = pickle.dumps(mouse_coords_blue)
    s.sendall(mouse_coords_blue)

    while True:
        app.main_frame.field.check_win()
        recv_data = s.recv(1024)
        recv_data = pickle.loads(recv_data)
        app.main_frame.field.update_canvas(recv_data)
        mouse_coords_blue = app.main_frame.field.get_mouse_coords()
        mouse_coords_blue = pickle.dumps(mouse_coords_blue)
        s.sendall(mouse_coords_blue)
    app.mainloop()
