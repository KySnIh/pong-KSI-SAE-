from tkinter import *
# импортируем библиотеку random
import random

# Добавляем глобальные переменные

# глобальные переменные
# настройки окна
WIDTH = 900
HEIGHT = 300

# настройки ракеток

# ширина ракетки
Racket_Width = 10
# высота ракетки
Racket_Height = 100

# настройки мяча
# Насколько будет увеличиваться скорость мяча с каждым ударом
BALL_SPEED_UP = 1.05
# Максимальная скорость мяча
BALL_MAX_SPEED = 40
# радиус мяча
BALL_RADIUS = 30

INITIAL_SPEED = 20
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED

# Счет игроков
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

# Добавим глобальную переменную отвечающую за расстояние
# до правого края игрового поля
right_line_distance = WIDTH - Racket_Width


def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)


def spawn_ball():
    global BALL_X_SPEED
    # Выставляем мяч по центру
    c.coords(BALL, WIDTH / 2 - BALL_RADIUS / 2,
             HEIGHT / 2 - BALL_RADIUS / 2,
             WIDTH / 2 + BALL_RADIUS / 2,
             HEIGHT / 2 + BALL_RADIUS / 2)
    # Задаем мячу направление в сторону проигравшего игрока,
    # но снижаем скорость до изначальной
    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)


# функция отскока мяча
def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED
    # ударили ракеткой
    if action == "strike":
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
        BALL_Y_SPEED = -BALL_Y_SPEED
b = "white"
a = "#003300"
d = "yellow"
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
    else:
        a = "#003300"
        c.configure(background=a)
    if b == "white":
        b = "yellow"
        c.itemconfig(BALL,fill = b)
    elif b == "yellow":
        b = "black"
        c.itemconfig(BALL, fill=b)
    else:
        b = "white"
        c.itemconfig(BALL,fill = b)
    if d == "yellow":
        d = "red"
        c.itemconfig(LEFT_RACKET, fill=d)
        c.itemconfig(RIGHT_RACKET, fill=d)
    elif d == "red":
        d = "green"
        c.itemconfig(LEFT_RACKET, fill=d)
        c.itemconfig(RIGHT_RACKET, fill=d)
    else:
        d = "yellow"
        c.itemconfig(LEFT_RACKET, fill=d)
        c.itemconfig(RIGHT_RACKET, fill=d)

# устанавливаем окно
root = Tk()
root.title("PythonicWay Pong")
# устанавливаем кнопку для настроек
root.title('12')
root.geometry('900x325')
btn = Button(text='Настройка цветовой гаммы', command=button_click)
btn.pack()
# btn2 = Button(text='Уменьшение скорости мячика', command=change_speed)
# btn2.pack()

# область анимации
# #003300
c = Canvas(root, width=WIDTH, height=HEIGHT, background=a)
c.pack()

# элементы игрового поля

# левая линия
c.create_line(Racket_Width, 0, Racket_Width, HEIGHT, fill="white")
# правая линия
c.create_line(WIDTH - Racket_Width, 0, WIDTH - Racket_Width, HEIGHT, fill="white")
# центральная линия
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

# установка игровых объектов

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

p_1_text = c.create_text(WIDTH - WIDTH / 6, Racket_Height / 4,
                         text=PLAYER_1_SCORE,
                         font="Arial 20",
                         fill="white")

p_2_text = c.create_text(WIDTH / 6, Racket_Height / 4,
                         text=PLAYER_2_SCORE,
                         font="Arial 20",
                         fill="white")

# добавим глобальные переменные для скорости движения мяча
# по горизонтали
BALL_X_CHANGE = 20
# по вертикали
BALL_Y_CHANGE = 0


def move_ball():
    # определяем координаты сторон мяча и его центра
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2

    # вертикальный отскок
    # Если мы далеко от вертикальных линий - просто двигаем мяч
    if ball_right + BALL_X_SPEED < right_line_distance and \
            ball_left + BALL_X_SPEED > Racket_Width:
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
    # Если мяч касается своей правой или левой стороной границы поля
    elif ball_right == right_line_distance or ball_left == Racket_Width:
        # Проверяем правой или левой стороны мы касаемся
        if ball_right > WIDTH / 2:
            # Если правой, то сравниваем позицию центра мяча
            # с позицией правой ракетки.
            # И если мяч в пределах ракетки делаем отскок
            if c.coords(RIGHT_RACKET)[1] < ball_center < c.coords(RIGHT_RACKET)[3]:
                bounce("strike")
            else:
                # Иначе игрок пропустил - тут оставим пока pass, его мы заменим на подсчет очков и респаун мячика
                update_score("left")
                spawn_ball()
        else:
            # То же самое для левого игрока
            if c.coords(LEFT_RACKET)[1] < ball_center < c.coords(LEFT_RACKET)[3]:
                bounce("strike")
            else:
                update_score("right")
                spawn_ball()
    # Проверка ситуации, в которой мячик может вылететь за границы игрового поля.
    # В таком случае просто двигаем его к границе поля.
    else:
        if ball_right > WIDTH / 2:
            c.move(BALL, right_line_distance - ball_right, BALL_Y_SPEED)
        else:
            c.move(BALL, -ball_left + Racket_Width, BALL_Y_SPEED)
    # горизонтальный отскок
    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("ricochet")


# зададим глобальные переменные скорости движения ракеток
# скорось с которой будут ездить ракетки
Racket_SPEED = 20
# скорость левой платформы
LEFT_RACKET_SPEED = 0
# скорость правой ракетки
RIGHT_RACKET_SPEED = 0


# функция движения обеих ракеток
def move_rackets():
    # для удобства создадим словарь, где ракетке соответствует ее скорость
    rackets = {LEFT_RACKET: LEFT_RACKET_SPEED,
            RIGHT_RACKET: RIGHT_RACKET_SPEED}
    # перебираем ракетки
    for Racket in rackets:
        # двигаем ракетку с заданной скоростью
        c.move(Racket, 0, rackets[Racket])
        # если ракетка вылезает за игровое поле возвращаем ее на место
        if c.coords(Racket)[1] < 0:
            c.move(Racket, 0, -c.coords(Racket)[1])
        elif c.coords(Racket)[3] > HEIGHT:
            c.move(Racket, 0, HEIGHT - c.coords(Racket)[3])


def main():
    move_ball()
    move_rackets()
    # вызываем саму себя каждые 10 миллисекунд
    root.after(20, main)


# Установим фокус на Canvas чтобы он реагировал на нажатия клавиш
c.focus_set()


# Напишем функцию обработки нажатия клавиш
def movement_handler(event):
    global LEFT_RACKET_SPEED, RIGHT_RACKET_SPEED
    if event.keysym in "Ww":
        LEFT_RACKET_SPEED = -Racket_SPEED
    elif event.keysym in "Ss":
        LEFT_RACKET_SPEED = Racket_SPEED
    elif event.keysym == "Up":
        RIGHT_RACKET_SPEED = -Racket_SPEED
    elif event.keysym == "Down":
        RIGHT_RACKET_SPEED = Racket_SPEED


# Привяжем к Canvas эту функцию
c.bind("<KeyPress>", movement_handler)


# Создадим функцию реагирования на отпускание клавиши
def stop_racket(event):
    global LEFT_RACKET_SPEED, RIGHT_RACKET_SPEED
    if event.keysym in "WwSs":
        LEFT_RACKET_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_RACKET_SPEED = 0


# Привяжем к Canvas эту функцию
c.bind("<KeyRelease>", stop_racket)

# запускаем движение
main()

# запускаем работу окна
root.mainloop()
