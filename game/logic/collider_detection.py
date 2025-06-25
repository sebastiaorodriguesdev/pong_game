#check collisions here

def check_collision(paddles, ball):
    for paddle in paddles:
        if paddle.rect.colliderect(ball.hitbox):
            ball.velocity_x *= -1