# импортируем библиотеку tkinter для разработки графического интерфейса
from tkinter import *
# импортируем библиотеку random
import random

# Добавляем глобальные переменные

# глобальные переменные
# ширина и высота окна
WIDTH = 1000
HEIGHT = 400

# настройки ракеток

# ширина ракетки
Racket_Width = 10
# высота ракетки
Racket_Height = 100

# мячик
# изменение скорости после удара
BALL_SPEED_UP = 1.05
# Максимальная скорость
BALL_MAX_SPEED = 45
# радиус мяча
BALL_RADIUS = 30
# начальная скорость мяча
INITIAL_SPEED = 15
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED

# Очки игроков
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

# Добавим глобальную переменную отвечающую за расстояние
# до правого края игрового поля
right_line_distance = WIDTH - Racket_Width
# Добавим глобальные переменные отвечающие за цыета
b = "yellow"
a = "#003300"
d = "yellow"

# добавим глобальные переменные для скорости движения мяча
# по горизонтали
BALL_X_CHANGE = 20
# по вертикали
BALL_Y_CHANGE = 0

# зададим глобальные переменные скорости движения ракеток
# скорось с которой будут ездить ракетки
Racket_SPEED = 25
# скорость левой ракетки
LEFT_RACKET_SPEED = 0
# скорость правой ракетки
RIGHT_RACKET_SPEED = 0

def button_click():
    # смена цветовых тематик
    global a
    global b
    global d
    # цвет фона
    if a == "#003300":
        a = "#000000"
    elif a == "#000000":
        a = "blue"
    elif a == "blue":
        a = "#003300"
    # смена цветов шарика
    if b == "yellow":
        b = "red"
    elif b == "red":
        b = "orange"
    elif b == "orange":
        b = "yellow"
    # смена цветов ракеток
    if d == "yellow":
        d = "red"
    elif d == "red":
        d = "orange"
    elif d == "orange":
        d = "yellow"


def repainting():
    # смена цветовых тематик
    global a
    global b
    global d
    # цвет фона
    c.configure(background=a)
    # цвет шарика
    c.itemconfig(BALL, fill=b)
    # цвет ракеток
    c.itemconfig(LEFT_RACKET, fill=d)
    c.itemconfig(RIGHT_RACKET, fill=d)
# устанавливаем окно

root = Tk()
root.title("Pong_KSI_SAE")
root.geometry('1000x425')
# устанавливаем кнопку для настроек
btn = Button(text='Настройка цветовой гаммы', command=button_click and repainting)
btn.pack()


# область анимации
# #003300
c = Canvas(root, width=WIDTH, height=HEIGHT, background=a)
c.pack()

# создаём само поле

# левая линия
c.create_line(Racket_Width, 0, Racket_Width, HEIGHT, fill="white")
# правая линия
c.create_line(WIDTH - Racket_Width, 0, WIDTH - Racket_Width, HEIGHT, fill="white")
# центральная линия
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

# установим игровые объекты

# создаем мяч
BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill=b)

# левая ракетка
LEFT_RACKET = c.create_line(Racket_Width / 2, 0, Racket_Width / 2, Racket_Height, width=Racket_Width, fill=d)

# правая ракетка
RIGHT_RACKET = c.create_line(WIDTH - Racket_Width / 2, 0, WIDTH - Racket_Width / 2,
                          Racket_Height, width=Racket_Width, fill=d)
# счёт игры
p_1_text = c.create_text(WIDTH - WIDTH / 6, Racket_Height / 4,
                         text=PLAYER_1_SCORE,
                         font="Calibri 18",
                         fill="purple")
p_2_text = c.create_text(WIDTH / 6, Racket_Height / 4,
                         text=PLAYER_2_SCORE,
                         font="Calibri 18",
                         fill="orange")


def update_score(player):
    # просто функция отвечающая за подсчёт очков
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
    else:
        PLAYER_2_SCORE += 1


def wrtie_updated_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)

def spawn_ball():
    global BALL_X_SPEED
    # Ставим мяч по центру
    c.coords(BALL, WIDTH / 2 - BALL_RADIUS / 2,
             HEIGHT / 2 - BALL_RADIUS / 2,
             WIDTH / 2 + BALL_RADIUS / 2,
             HEIGHT / 2 + BALL_RADIUS / 2)
    # Направляем мяч проигравшему игроку
    # и снижаем скорость до изначальной
    if BALL_X_SPEED > 0:
        BALL_X_SPEED = INITIAL_SPEED
    else:
        BALL_X_SPEED = -INITIAL_SPEED


# Отскок мяча
def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED
    # Удар ракеткой
    if action == "hor_reb":
        BALL_Y_SPEED = -BALL_Y_SPEED
    elif action == "hit":
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) >= BALL_MAX_SPEED:
            BALL_X_SPEED = -BALL_X_SPEED
        else:
            BALL_X_SPEED *= -BALL_SPEED_UP


def moving_ball():
    # определяем положение мяча
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2
    # вертикальный отскок
    # Если мы далеко от вертикальных линий просто передвигаем мяч
    if not ((ball_right + BALL_X_SPEED) >= right_line_distance or (ball_left + BALL_X_SPEED) <= Racket_Width):
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
    # Если мяч касается своей правой или левой стороной границы поля
    elif ball_right == right_line_distance or ball_left == Racket_Width:
        # Проверяем правой или левой стороны мы касаемся
        if ball_right > WIDTH / 2:
            # Для правой сравниваем позицию центра мяча с позицией правой ракетки
            # И если мяч в пределах ракетки делаем отскок
            if c.coords(RIGHT_RACKET)[1] < ball_center < c.coords(RIGHT_RACKET)[3]:
                bounce("hit")
            else:
                # Иначе игрок пропустил
                update_score("left")
                wrtie_updated_score("left")
                spawn_ball()
        else:
            # Для левой сравниваем позицию центра мяча с позицией левой ракетки
            # И если мяч в пределах ракетки делаем отскок
            if c.coords(LEFT_RACKET)[1] < ball_center < c.coords(LEFT_RACKET)[3]:
                bounce("hit")
            else:
                # Иначе игрок пропустил
                update_score("right")
                wrtie_updated_score("right")
                spawn_ball()
    # Проверка ситуации, в которой мячик может вылететь за границы игрового поля.
    # В таком случае просто возвращаем его к границе поля.
    else:
        if ball_right <= WIDTH / 2:
            c.move(BALL, -ball_left + Racket_Width, BALL_Y_SPEED)
        else:
            c.move(BALL, right_line_distance - ball_right, BALL_Y_SPEED)
    # горизонтальный отскок
    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("hor_reb")


# функция движения обеих ракеток
def move_rackets():
    # словарь ракетка - скорость
    rackets = {LEFT_RACKET: LEFT_RACKET_SPEED,
            RIGHT_RACKET: RIGHT_RACKET_SPEED}
    # перебираем ракетки
    for Racket in rackets:
        # двигаем ракетку с её скоростью
        c.move(Racket, 0, rackets[Racket])
        # если ракетка вылезает возвращаем
        if c.coords(Racket)[3] > HEIGHT:
            c.move(Racket, 0, HEIGHT - c.coords(Racket)[3])
        elif c.coords(Racket)[1] < 0:
            c.move(Racket, 0, -c.coords(Racket)[1])


# сделаем так чтобы Canvas реагировал на нажатия клавиш
c.focus_set()


# реакция на нажатие клавиши
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


# добавим в Canvas
c.bind("<KeyPress>", KP_move_racket)


# реагирование на отпускание клавиши
def KP_stop_racket(event):
    global LEFT_RACKET_SPEED, RIGHT_RACKET_SPEED
    if event.keysym in ("Up", "Down"):
        RIGHT_RACKET_SPEED = 0
    elif event.keysym in "WwSs":
        LEFT_RACKET_SPEED = 0


def start():
    moving_ball()
    move_rackets()
    # вызываем саму себя каждые 17 миллисекунд
    root.after(17, start)


# добавим в Canvas
c.bind("<KeyRelease>", KP_stop_racket)

# запускаем игру
start()

# запускаем окно
root.mainloop()
