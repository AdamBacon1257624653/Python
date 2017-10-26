# coding=utf8
from random import Random

import pygame
import time
from pygame.locals import *

"""
    Set up main screen
    it's responsible for screen and background image display
"""


class BasePlane(object):
    def __init__(self, x_tmp, y_tmp, screen_tmp, image_source):
        self.x = x_tmp
        self.y = y_tmp
        self.screen = screen_tmp
        self.image = pygame.image.load(image_source)
        self.bullets = []
        self.del_bullets = []

    def fire(self, x_offset, y_offset):
        self.bullets.append(Bullet(self.x + x_offset, self.y + y_offset, self.screen))


class HeroPlane(BasePlane):
    """docstring for HeroPlane"""

    def __init__(self, x_tmp, y_tmp, screen_tmp):
        BasePlane.__init__(self, x_tmp, y_tmp, screen_tmp, "./resources/gameArts/hero_fly_1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.display()
            bullet.move_up()
            if bullet.y <= 0:
                self.del_bullets.append(bullet)
        for bullet in self.del_bullets:
            self.bullets.remove(bullet)
        self.del_bullets.clear()

    def horizontal_move(self, direction):
        """
            direction:
                >= 0: right
                <0 : left
        """
        if direction >= 0:
            distance = 5
        else:
            distance = -5
        self.x += distance


class EnemyPlane(BasePlane):
    """docstring for EnemyPlane"""

    def __init__(self, x_tmp, y_tmp, screen_tmp):
        BasePlane.__init__(self, x_tmp, y_tmp, screen_tmp, "./resources/gameArts/enemy1_fly_1.png")
        self.num = 0
        self.isRight = True
        self.start_boom = False

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        rand_int = Random().randint(1, 100)
        if rand_int == 3 or rand_int == 68:
            self.fire(17, 24)
        for bullet in self.bullets:
            bullet.display()
            bullet.move_down()
        if self.start_boom:
            self.num += 1
            self.boom()

    def horizontal_move(self):
        if self.x <= 0:
            self.isRight = True
        elif self.x >= 446:
            self.isRight = False
        if self.isRight:
            self.x += 3
        else:
            self.x -= 3

    def boom(self):
        if self.num == 1:
            self.image = pygame.image.load("./resources/gameArts/enemy1_blowup_1.png")
        elif self.num == 15:
            self.image = pygame.image.load("./resources/gameArts/enemy1_blowup_2.png")
        elif self.num == 30:
            self.image = pygame.image.load("./resources/gameArts/enemy1_blowup_3.png")
        elif self.num == 45:
            self.image = pygame.image.load("./resources/gameArts/enemy1_blowup_4.png")


class Bullet(object):
    """docstring for BaseBullet"""

    def __init__(self, x_tmp, y_tmp, screen_tmp):
        self.x = x_tmp
        self.y = y_tmp
        self.screen = screen_tmp
        self.image = pygame.image.load("./resources/gameArts/bullet1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5


def key_control(hero_tmp, enemy_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Exit!")
            exit()
        elif event.type == KEYDOWN:
            event_key = event.key
            if event_key == K_a or event_key == K_LEFT:
                print("Left")
                hero_tmp.horizontal_move(-1)
            elif event_key == K_d or event_key == K_RIGHT:
                print("Right")
                hero_tmp.horizontal_move(1)
            elif event_key == K_b:
                print("Enemy boom..")
                enemy_temp.start_boom = True
                enemy_temp.boom()
            elif event_key == K_SPACE:
                print("Fire....")
                hero_tmp.fire(35, -20)


def main():
    pygame.FULLSCREEN
    screen = pygame.display.set_mode((480, 852), 0)

    bg = pygame.image.load("./resources/gameArts/background_2.png")

    x = 220
    y = 700
    hero = HeroPlane(x, y, screen)
    enemy = EnemyPlane(0, 0, screen)
    while True:
        screen.blit(bg, (0, 0))
        hero.display()
        enemy.display()
        enemy.horizontal_move()
        key_control(hero, enemy)
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
