import main

def test_update_score():
    for i in range(100):
        main.update_score("right")
    for i in range(50):
        main.update_score("left")
    assert main.PLAYER_1_SCORE == 100
    assert main.PLAYER_2_SCORE == 50
