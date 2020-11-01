import pygame
import random

window_width = 700
window_hight = 700
grey = (128, 128, 128)
blue = (0, 0, 255)
yellow = (255, 255, 0)
radius = 10
player_hight = 15
player_width = 50
ball_val = 1
player_val = 3
refresh_rate = 120
size = (window_width, window_hight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('catch the ball')


class Player():
    def __init__(self, x, y, width, hight, color, vel):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.color = color
        self.rect = (x, y, width, hight)
        self.vel = vel

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            if self.x < 0:
                self.x = 0
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            if self.x > window_width - self.width:
                self.x = window_width - self.width
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.hight)

    def get_position(self):
        return self.x, self.y

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Ball():
    def __init__(self, x, y, radius, color, vel):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 3

    def move(self):
        self.y += self.vel

    def get_position(self):
        return self.x, self.y

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.get_position(), self.radius)


def redrawWindoe(screen, player, ball):
    screen.fill(grey)
    ball.draw(screen)
    player.draw(screen)
    pygame.display.flip()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    finish = False
    b_x_pos_start = radius + int(random.random() * (window_width - 2 * radius))
    b_y_pos_start = radius
    p_x_pos_start = (window_width - player_width) / 2
    p_y_pos_start = window_hight - player_hight
    player = Player(p_x_pos_start, p_y_pos_start, player_width, player_hight, blue, player_val)
    ball = Ball(b_x_pos_start, b_y_pos_start, radius, yellow, ball_val)

    while not finish:
        clock.tick(refresh_rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    b_x_pos_start = radius + int(random.random() * (window_width - 2 * radius))
                    ball.update_position(b_x_pos_start, b_y_pos_start)
                    player.update_position(p_x_pos_start, p_y_pos_start)

        ball.move()
        player.move()
        ball_x = ball.get_position()[0]
        ball_y = ball.get_position()[1]
        player_x = player.get_position()[0]
        player_y = player.get_position()[1]

        if (
                ball_y >= window_hight - player_hight - radius and ball_x >= player_x - radius and ball_x <= player_x + player_width + radius):
            b_x_pos_start = radius + int(random.random() * (window_width - 2 * radius))
            ball.update_position(b_x_pos_start, b_y_pos_start)
            player.update_position(p_x_pos_start, p_y_pos_start)

        redrawWindoe(screen, player, ball)
    pygame.quit()


if __name__ == '__main__':
    main()

