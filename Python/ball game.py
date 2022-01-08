from tkinter import *
import random, time

tk = Tk()
tk.title("Paddle Ball")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)  # 使画布外无边框
canvas.pack()
txt_id = canvas.create_text(90, 50, anchor=NW, text="游戏结束", font=('pingfang', 80), state="hidden")
score_id = canvas.create_text(25, 25, anchor=NW, text=f"分数: 0", font=('pingfang', 15))
tk.update()


class Ball:
    def __init__(self, canvas, paddle, color='red'):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id, 245, 100)
        # self.x = random.randint(-3,3)
        # self.y = -1
        self.x = 0
        self.y = 0
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.alive = True
        self.cnt = 0

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or self.hit(pos):
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.width:
            self.x = -self.x
        elif pos[3] >= self.height:
            self.alive = False
            print("Game Over")

    def hit(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
            and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.cnt += 1
            self.canvas.itemconfig(score_id, text=f'分数: {self.cnt}')
            self.x += 0.5
            self.y += 0.5
            self.paddle.level += 1
            print("当前速度:", self.paddle.level)

            return True
        else:
            return False


class Paddle:
    def __init__(self, canvas, color='brown'):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)
        self.level = 0

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.width:
            self.x = 0

    def left(self, event):
        self.x = -2 * 1.1 ** self.level

    def right(self, event):
        self.x = 2 * 1.1 ** self.level


def start(event):
    while 1:
        if event.num == 1:
            ball.x = random.randint(-3, 3)
            ball.y = -1
            break


if __name__ == '__main__':
    paddle = Paddle(canvas)
    ball = Ball(canvas, paddle)
    canvas.bind_all("<Button-1>", start)

    # tk.mainloop()
    while 1:
        if ball.alive:
            ball.draw()
            paddle.draw()
        else:
            canvas.itemconfig(txt_id, state='normal')
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
