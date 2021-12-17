from tkinter import *
import random
# Импортируем библиотеку tkinter для разработки графического интерфейса
# Импортируем библиотеку random

# Добавляем глобальные переменные

WIDTH = 1000
HEIGHT = 400
# Ширина и высота окна

Racket_Width = 10
# Ширина ракетки

Racket_Height = 100
# Высота ракетки

BALL_SPEED_UP = 1.05
# Изменение скорости после удара

BALL_MAX_SPEED = 45
# Максимальная скорость

BALL_RADIUS = 30
# Радиус мяча

INITIAL_SPEED = 15
X_SPEED = INITIAL_SPEED
Y_SPEED = INITIAL_SPEED
# Начальная скорость мяча

PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
# Очки игроков

right_line_distance = WIDTH - Racket_Width
# Добавим глобальную переменную отвечающую за расстояние
# до правого края игрового поля

# Добавим глобальные переменные отвечающие за цвета

b = "yellow"
a = "#003300"
d = "yellow"
# Глобальная переменная а отвечает за цвет фона,глобальная переменная b за цвет шарика,
# а глобальная переменная d за цвет ракеток

# Добавим глобальные переменные для скорости движения мяча

BALL_X_CHANGE = 20
# По горизонтали

BALL_Y_CHANGE = 0
# По вертикали

# Зададим глобальные переменные скорости движения ракеток

Racket_SPEED = 25
# Скорость с которой будут ездить ракетки

LEFT_RACKET_SPEED = 0
# Скорость левой ракетки

RIGHT_RACKET_SPEED = 0
# Скорость правой ракетки

def button_click():
    """
    Смена цветовых тематик:
    Смена цвета фона
    Смена цветов шарика
    Смена цветов ракеток
    a - глобальная переменная отвечающая за смену цвета фона
    b - глобальная переменная отвечающая за смену цвета шарика
    d - глобальная переменная отвечающая за смену цвета ракеток
    """
    global a
    global b
    global d
    if a == "#003300":
        a = "#000000"
        c.configure(background=a)
    elif a == "#000000":
        a = "blue"
        c.configure(background=a)
    elif a == "blue":
        a = "#003300"
        c.configure(background=a)
    if b == "yellow":
        b = "red"
        c.itemconfig(BALL, fill=b)
    elif b == "red":
        b = "orange"
        c.itemconfig(BALL, fill=b)
    elif b == "orange":
        b = "yellow"
        c.itemconfig(BALL, fill=b)
    if d == "yellow":
        d = "red"
        c.itemconfig(LEFT_RACKET, fill=d)
        c.itemconfig(RIGHT_RACKET, fill=d)
    elif d == "red":
        d = "orange"
        c.itemconfig(LEFT_RACKET, fill=d)
        c.itemconfig(RIGHT_RACKET, fill=d)
    elif d == "orange":
        d = "yellow"
        c.itemconfig(LEFT_RACKET, fill=d)
        c.itemconfig(RIGHT_RACKET, fill=d)

root = Tk()
root.title("Pong_KSI_SAE")
root.geometry('1000x425')
# Устанавливаем окно

btn = Button(text='Настройка цветовой гаммы', command=button_click )
btn.pack()
# Устанавливаем кнопку для настроек

c = Canvas(root, width=WIDTH, height=HEIGHT, background=a)
c.pack()
# Область анимации

# Установим игровые объекты

c.create_line(Racket_Width, 0, Racket_Width, HEIGHT, fill="white")
# Левая линия
c.create_line(WIDTH - Racket_Width, 0, WIDTH - Racket_Width, HEIGHT, fill="white")
# Правая линия
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")
# Центральная линия
# Создаём само поле

BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill=b)
# Создаем мяч

LEFT_RACKET = c.create_line(Racket_Width / 2, 0, Racket_Width / 2, Racket_Height, width=Racket_Width, fill=d)
# Левая ракетка

RIGHT_RACKET = c.create_line(WIDTH - Racket_Width / 2, 0, WIDTH - Racket_Width / 2,
                          Racket_Height, width=Racket_Width, fill=d)
# Правая ракетка




p_1_text = c.create_text(WIDTH - WIDTH / 6, Racket_Height / 4,
                         text=PLAYER_1_SCORE,
                         font="Calibri 18",
                         fill="purple")
p_2_text = c.create_text(WIDTH / 6, Racket_Height / 4,
                         text=PLAYER_2_SCORE,
                         font="Calibri 18",
                         fill="orange")
# Счёт игры первого и второго игроков

def update_score(player):
    """
    Функция отвечающая за подсчёт очков
    player - забивший игрок
    """
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
    else:
        PLAYER_2_SCORE += 1

def wrtie_updated_score(player):
    """
    Функция изменяющая изображение счёта
    На вход идёт забивший игрок
    """
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)




def spawn_ball():
    """
    Ставим мяч по центру
    Направляем  проигравшему с изначальной скоростью
    """
    global X_SPEED
    c.coords(BALL, WIDTH / 2 - BALL_RADIUS / 2,
             HEIGHT / 2 - BALL_RADIUS / 2,
             WIDTH / 2 + BALL_RADIUS / 2,
             HEIGHT / 2 + BALL_RADIUS / 2)
    if X_SPEED > 0:
        X_SPEED = INITIAL_SPEED
    else:
        X_SPEED = -INITIAL_SPEED




def bounce(action):
    """
    Функция отвечающая за отскок мяча и удар ракеткой
    action - действие происходящее с мячом удар или горзонатльный отскок
    """
    global X_SPEED, Y_SPEED
    if action == "hor_reb":
        Y_SPEED = -Y_SPEED
    elif action == "hit":
        Y_SPEED = random.randrange(-10, 10)
        if abs(X_SPEED) >= BALL_MAX_SPEED:
            X_SPEED = -X_SPEED
        else:
            X_SPEED *= -BALL_SPEED_UP

def moving_ball():
    """
    Функция отвечающая за положение и отскок шарика,
    а также не дающая мячку вылететь за игрвоую площадку
    """
    l, t, r, bot = c.coords(BALL)
    ball_center = (t + bot) / 2
    if not ((r + X_SPEED) >= right_line_distance or (l + X_SPEED) <= Racket_Width):
        c.move(BALL, X_SPEED, Y_SPEED)
    elif r == right_line_distance or l == Racket_Width:
        if r > WIDTH / 2:
            if c.coords(RIGHT_RACKET)[1] < ball_center < c.coords(RIGHT_RACKET)[3]:
                bounce("hit")
            else:
                update_score("left")
                wrtie_updated_score("left")
                spawn_ball()
        else:

            if c.coords(LEFT_RACKET)[1] < ball_center < c.coords(LEFT_RACKET)[3]:
                bounce("hit")
            else:
                update_score("right")
                wrtie_updated_score("right")
                spawn_ball()
    else:
        if r <= WIDTH / 2:
            c.move(BALL, -l + Racket_Width, Y_SPEED)
        else:
            c.move(BALL, right_line_distance - r, Y_SPEED)
    if t + Y_SPEED < 0 or bot + Y_SPEED > HEIGHT:
        bounce("hor_reb")

def move_rackets():
    """
    Функция отвечающая за положение и движение ракеток,
    а также не дающая ракетке выехать за игрвоую площадку
    """
    rackets = {LEFT_RACKET: LEFT_RACKET_SPEED,
            RIGHT_RACKET: RIGHT_RACKET_SPEED}

    for Racket in rackets:
        c.move(Racket, 0, rackets[Racket])
        if c.coords(Racket)[3] > HEIGHT:
            c.move(Racket, 0, HEIGHT - c.coords(Racket)[3])
        elif c.coords(Racket)[1] < 0:
            c.move(Racket, 0, -c.coords(Racket)[1])

c.focus_set()
# Сделаем так чтобы Canvas реагировал на нажатия клавиш

def KP_move_racket(event):
    """
    Функция отвечающая за реакцию на нажатие клавиш
    event - какая именно клавиша была отпущена
    """
    global LEFT_RACKET_SPEED, RIGHT_RACKET_SPEED
    if event.keysym == "Up":
        RIGHT_RACKET_SPEED = -Racket_SPEED
    elif event.keysym == "Down":
        RIGHT_RACKET_SPEED = Racket_SPEED
    elif event.keysym in "Ww":
        LEFT_RACKET_SPEED = -Racket_SPEED
    elif event.keysym in "Ss":
        LEFT_RACKET_SPEED = Racket_SPEED


c.bind("<KeyPress>", KP_move_racket)
# Добавим в Canvas


def KP_stop_racket(event):
    """
    Функция отвечающая за реагирование на отпускание клавиши
    event - какая именно клавиша была отпущена
    """
    global LEFT_RACKET_SPEED, RIGHT_RACKET_SPEED
    if event.keysym in ("Up", "Down"):
        RIGHT_RACKET_SPEED = 0
    elif event.keysym in "WwSs":
        LEFT_RACKET_SPEED = 0


def start():
    """
    Функция вызывающая игру
    Вызывает себякаждые 17 миллисекунд
    """
    moving_ball()
    move_rackets()
    root.after(17, start)

c.bind("<KeyRelease>", KP_stop_racket)
# Добавим в Canvas

start()
# Запускаем игру

root.mainloop()
# Запускаем окно