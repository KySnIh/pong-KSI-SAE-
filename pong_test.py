import main


def test_update_score():
    for i in range(100):
        main.update_score("right")
    for i in range(50):
        main.update_score("left")
    assert main.PLAYER_1_SCORE == 100
    assert main.PLAYER_2_SCORE == 50


def test_button_click():
    for i in range(10):
        assert ((main.a == "#003300" and main.b == "yellow" and main.d == "yellow") or (main.a == "#000000" and main.b == "red" and main.d == "red") or (main.a == "blue" and main.b == "orange" and main.d == "orange"))

def test_KP_stop_racket():





