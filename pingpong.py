from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Ping-Pong game")



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player_R(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed
class Player_L(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
speed_x = 5
speed_y = 5
ball = GameSprite("ball.png", 200, 250, 5)
game = True
player_l = Player_L("paddle.png", 5, 400, 10)
player_r = Player_R("paddle.png", 630, 400, 10)
font.init()
font = font.SysFont("Arial", 40)
lose1 = font.render(
    "PLAYER 1 LOSES!", True, (255, 0, 0))
lose2 = font.render(
    "PLAYER 2 LOSES!", True, (255, 0, 0))


finish = False
clock = time.Clock()
while game:
    window.fill((255, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        player_r.reset()
        player_r.update()
        player_l.reset()
        player_l.update()
    if ball.rect.y > 435 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x >635:
        finish = True
        window.blit(lose2, (200, 200))
    display.update()
    clock.tick(60)


    
    