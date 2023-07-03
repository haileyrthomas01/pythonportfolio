import tkinter as tk
import random

window = tk.Tk()
window.title("Pong Game")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)
canvas = tk.Canvas(window, width=500, height=400, bd=0, highlightthickness=0)
canvas.configure(bg="#e3f2fd")
canvas.pack()
window.update()

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 60, 10, fill="#2196f3")
        self.canvas.move(self.id, 220, 380)  # Set paddle's initial position
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def move_left(self, event):
        self.x = -1

    def move_right(self, event):
        self.x = 1

    def move(self):
        paddle_pos = self.canvas.coords(self.id)
        if paddle_pos[0] <= 0 and self.x < 0:
            self.x = 0
        elif paddle_pos[2] >= 500 and self.x > 0:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

class Ball:
    def __init__(self, canvas, paddle, start_text_id):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(0, 0, 15, 15, fill="#64b5f6")
        self.canvas.move(self.id, 245, 200)  # Set ball's initial position
        self.x = 0
        self.y = 0
        self.is_game_over = False
        self.is_game_started = False
        self.start_text_id = start_text_id

    def move(self):
        if self.is_game_started and not self.is_game_over:
            self.canvas.move(self.id, self.x, self.y)
            ball_pos = self.canvas.coords(self.id)
            if ball_pos[1] <= 0:
                self.y *= -1
            if ball_pos[3] >= 400:
                self.y = 0
                self.x = 0
                self.is_game_over = True
                canvas.create_text(250, 200, text="Game Over!", font=("Helvetica", 30), fill="#0d47a1")
            if ball_pos[0] <= 0 or ball_pos[2] >= 500:
                self.x *= -1
            if self.hit_paddle(ball_pos):
                self.y *= -1

    def hit_paddle(self, ball_pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if paddle_pos[0] <= ball_pos[2] and paddle_pos[2] >= ball_pos[0]:
            if paddle_pos[1] <= ball_pos[3] <= paddle_pos[3]:
                return True
        return False

    def start_game(self, event=None):
        if not self.is_game_started:
            self.is_game_started = True
            self.x = random.choice([-2, -1, 1, 2])
            self.y = -2
            self.canvas.delete(self.start_text_id)

paddle = Paddle(canvas, "#64b5f6")
start_text_id = canvas.create_text(250, 200, text="Press Left or Right Arrow Key to Start", font=("Helvetica", 16), fill="black")
ball = Ball(canvas, paddle, start_text_id)

def on_key_press(event):
    if not ball.is_game_started:
        if event.keysym == 'Left' or event.keysym == 'Right':
            ball.start_game()

window.bind('<KeyPress>', on_key_press)

while not ball.is_game_over:
    paddle.move()
    ball.move()
    window.update_idletasks()
    window.update()
    window.after(10)

window.mainloop()

# python ponggame.py
