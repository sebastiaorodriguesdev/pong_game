def verify_point_score(ball, paddle1, paddle2):
    if ball.x < paddle1.rect.x + paddle1.rect.width and ball.x > paddle1.rect.x:
        return True, 2 #because paddle 1 is on the left
    elif ball.x > paddle2.rect.x and ball.x < paddle2.rect.x + paddle2.rect.width:
        return True, 1 #because paddle 2 is on the right

    return False, None