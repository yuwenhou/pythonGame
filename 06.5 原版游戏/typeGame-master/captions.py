# -*- coding: utf-8 -*-

import pygame


class Caption(pygame.sprite.Sprite):
    '''
    实时显示打字性能
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.text = "Speed: %.1f/min, correct words: %s/%s" % (0, 0, 0)
        self.update()

    def update(self):
        self.image = pygame.font.Font(None, 26).render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()

    def setText(self, speed, words, corrWords):
        self.text = "Speed: %.1f/min, correct words: %s/%s" % (
            speed, corrWords, words)
