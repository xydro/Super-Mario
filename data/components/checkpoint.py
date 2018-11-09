__author__ = 'CPSC 386 Dai Kieu, Trong To, Carlos Serna'

import pygame as pg
from .. import settings as s


class Checkpoint(pg.sprite.Sprite):
    """Invisible sprite used to add enemies, special boxes
    and trigger sliding down the flag pole"""
    def __init__(self, x, name, y=0, width=10, height=600):
        super(Checkpoint, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(s.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name




