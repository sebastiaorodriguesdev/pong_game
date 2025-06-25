def verify_point_score(ball, screen_width):
    if ball.x - ball.radius < 0:
        return True, 2 #because paddle 1 is on the left
    elif ball.x + ball.radius > screen_width:
        return True, 1 #because paddle 2 is on the right

    return False, None