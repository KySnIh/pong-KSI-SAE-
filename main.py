"""
Импортируем библиотеку tkinter для разработки графического интерфейса
Импортируем библиотеку random
"""

from tkinter import *
import random

""" 
Добавляем глобальные переменные
"""

""" 
Ширина и высота окна
"""

WIDTH = 1000
HEIGHT = 400

""" 
Настройки ракеток
"""

""" 
Ширина ракетки
"""

Racket_Width = 10

""" 
Высота ракетки
"""

Racket_Height = 100

""" 
Мячик
"""

"""
Изменение скорости после удара
"""

BALL_SPEED_UP = 1.05

""" 
Максимальная скорость
"""

BALL_MAX_SPEED = 45

""" 
Радиус мяча
"""

BALL_RADIUS = 30

""" 
Начальная скорость мяча
"""

INITIAL_SPEED = 15
X_SPEED = INITIAL_SPEED
Y_SPEED = INITIAL_SPEED

""" 
Очки игроков
"""
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

""" 
Добавим глобальную переменную отвечающую за расстояние
До правого края игрового поля
"""

right_line_distance = WIDTH - Racket_Width

""" 
Добавим глобальные переменные отвечающие за цвета
"""

b = "yellow"
a = "#003300"
d = "yellow"

""" 
Добавим глобальные переменные для скорости движения мяча
"""

"""
По горизонтали
"""

BALL_X_CHANGE = 20

""" 
По вертикали
"""

BALL_Y_CHANGE = 0

""" 
Зададим глобальные переменные скорости движения ракеток
"""

""" 
Скорость с которой будут ездить ракетки
"""

Racket_SPEED = 25
""" 
Скорость левой ракетки
"""

LEFT_RACKET_SPEED = 0

""" 
Скорость правой ракетки
"""

RIGHT_RACKET_SPEED = 0

""" 
Смена цветовых тематик
Цвет фона
Смена цветов шарика
Смена цветов ракеток
"""

def button_click():
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


""" 
Устанавливаем окно
"""

root = Tk()
root.title("Pong_KSI_SAE")
root.geometry('1000x425')

""" 
Устанавливаем кнопку для настроек
"""

btn = Button(text='Настройка цветовой гаммы', command=button_click )
btn.pack()

""" 
Область анимации
"""

c = Canvas(root, width=WIDTH, height=HEIGHT, background=a)
c.pack()

""" 
Создаём само поле
"""

""" 
Левая линия
Правая линия
Центральная линия
"""

c.create_line(Racket_Width, 0, Racket_Width, HEIGHT, fill="white")
c.create_line(WIDTH - Racket_Width, 0, WIDTH - Racket_Width, HEIGHT, fill="white")
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

""" 
Установим игровые объекты
"""

""" 
Создаем мяч
"""

BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill=b)

""" 
Левая ракетка
"""

LEFT_RACKET = c.create_line(Racket_Width / 2, 0, Racket_Width / 2, Racket_Height, width=Racket_Width, fill=d)

""" 
Правая ракетка
"""

RIGHT_RACKET = c.create_line(WIDTH - Racket_Width / 2, 0, WIDTH - Racket_Width / 2,
                          Racket_Height, width=Racket_Width, fill=d)

""" 
Счёт игры
"""

p_1_text = c.create_text(WIDTH - WIDTH / 6, Racket_Height / 4,
                         text=PLAYER_1_SCORE,
                         font="Calibri 18",
                         fill="purple")
p_2_text = c.create_text(WIDTH / 6, Racket_Height / 4,
                         text=PLAYER_2_SCORE,
                         font="Calibri 18",
                         fill="orange")

""" 
Функция отвечающая за подсчёт очков
На вход идёт забивший игрок
"""

def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
    else:
        PLAYER_2_SCORE += 1

"""
Функция изменяющая изображение счёта
На вход идёт забивший игрок
"""

def wrtie_updated_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)


""" 
Ставим мяч по центру
Направляем мяч проигравшему игроку
И снижаем скорость до изначальной
"""

def spawn_ball():
    global X_SPEED
    c.coords(BALL, WIDTH / 2 - BALL_RADIUS / 2,
             HEIGHT / 2 - BALL_RADIUS / 2,
             WIDTH / 2 + BALL_RADIUS / 2,
             HEIGHT / 2 + BALL_RADIUS / 2)
    if X_SPEED > 0:
        X_SPEED = INITIAL_SPEED
    else:
        X_SPEED = -INITIAL_SPEED


""" 
Отскок мяча
Удар ракеткой
"""

def bounce(action):
    global X_SPEED, Y_SPEED
    if action == "hor_reb":
        Y_SPEED = -Y_SPEED
    elif action == "hit":
        Y_SPEED = random.randrange(-10, 10)
        if abs(X_SPEED) >= BALL_MAX_SPEED:
            X_SPEED = -X_SPEED
        else:
            X_SPEED *= -BALL_SPEED_UP

""" 
Определяем положение мяча
Вертикальный отскок
Если мы далеко от вертикальных линий просто передвигаем мяч
Если мяч касается своей правой или левой стороной границы поля
Проверяем правой или левой стороны мы касаемся
Для правой сравниваем позицию центра мяча с позицией правой ракетки
И если мяч в пределах ракетки делаем отскок
Иначе игрок пропустил
Для левой сравниваем позицию центра мяча с позицией левой ракетки
И если мяч в пределах ракетки делаем отскок
Иначе игрок пропустил
Проверка ситуации, в которой мячик может вылететь за границы игрового поля
В таком случае просто возвращаем его к границе поля
И горизонтальный отскок
"""

def moving_ball():
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


""" 
Функция движения обеих ракеток
Словарь ракетка - скорость
Перебираем ракетки
Двигаем ракетку с её скоростью
Если ракетка вылезает возвращаем
"""

def move_rackets():
    rackets = {LEFT_RACKET: LEFT_RACKET_SPEED,
            RIGHT_RACKET: RIGHT_RACKET_SPEED}

    for Racket in rackets:
        c.move(Racket, 0, rackets[Racket])
        if c.coords(Racket)[3] > HEIGHT:
            c.move(Racket, 0, HEIGHT - c.coords(Racket)[3])
        elif c.coords(Racket)[1] < 0:
            c.move(Racket, 0, -c.coords(Racket)[1])


""" 
Сделаем так чтобы Canvas реагировал на нажатия клавиш
"""

c.focus_set()


""" 
Реакция на нажатие клавиши
"""

def KP_move_racket(event):
    global LEFT_RACKET_SPEED, RIGHT_RACKET_SPEED
    if event.keysym == "Up":
        RIGHT_RACKET_SPEED = -Racket_SPEED
    elif event.keysym == "Down":
        RIGHT_RACKET_SPEED = Racket_SPEED
    elif event.keysym in "Ww":
        LEFT_RACKET_SPEED = -Racket_SPEED
    elif event.keysym in "Ss":
        LEFT_RACKET_SPEED = Racket_SPEED


""" 
Добавим в Canvas
"""

c.bind("<KeyPress>", KP_move_racket)


""" 
Реагирование на отпускание клавиши
"""

def KP_stop_racket(event):
    global LEFT_RACKET_SPEED, RIGHT_RACKET_SPEED
    if event.keysym in ("Up", "Down"):
        RIGHT_RACKET_SPEED = 0
    elif event.keysym in "WwSs":
        LEFT_RACKET_SPEED = 0

"""
Вызываем функцию каждые 17 миллисекунд
"""

def start():
    moving_ball()
    move_rackets()
    root.after(17, start)

""" 
Добавим в Canvas
"""

c.bind("<KeyRelease>", KP_stop_racket)

""" 
Запускаем игру
"""

start()

""" 
Запускаем окно
"""

root.mainloop()
