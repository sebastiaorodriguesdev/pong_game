#class to the main game run
from logic.collider_detection import check_collision
from logic.score_point import verify_point_score
from logic.score import player_score
def run_game(paddles, ball, players):
    ball.update_position()
    check_collision(paddles, ball)
    scored, scoring_player = verify_point_score(ball, paddles[0], paddles[1])
    if scored:
        for player in players:
            if player.id == scoring_player:            
                player_score(player)
                ball.reset()