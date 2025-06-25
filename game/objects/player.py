class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.score = 0
    
    def draw(self, screen, x, y, font, color):
        text = font.render(f"{self.name}: {self.score}", True, color)
        screen.blit(text, (x, y))