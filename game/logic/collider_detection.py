#check collisions here

def check_collision(paddles, ball):
    for paddle in paddles:
        if paddle.rect.colliderect(ball.hitbox):
            ball.velocity_x *= -1
            #so the angle changes when the ball hits the paddle, relative to each centers
            paddle_center = paddle.rect.centery
            ball_center = ball.y
            offset = ball_center - paddle_center
            ball.velocity_y = offset // 7
            