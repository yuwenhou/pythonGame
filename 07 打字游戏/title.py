# -*- coding: utf-8 -*-
"""
控制文字的输入
"""
import pygame


class Title(pygame.sprite.Sprite):
    '''
    实时显示打字性能
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.text = "速度: %.1f/分钟, 正确单词: %s/%s,倒计时: %d 秒" % (0, 0, 0, 60)
        self.update()

    def update(self):
        self.image = pygame.font.Font("files/ziti.ttf", 26).render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()

    def setText(self, speed, words, corrWords,countdown):
        self.text = "速度: %.1f/min,  正确单词: %s/%s,  倒计时: %d 秒" % (
            speed, corrWords, words, countdown)
     
    def print_text(self,screen,x,y,text,color = (232,206,144),size = 38):
        words = text.split('\n')
        cow = 0
        for i in words:
            imgText1 = pygame.font.Font("files/ziti.ttf", 38).render(i, True, color)  # 创建字体，三个参数是文本.抗锯齿.颜色
            screen.blit(imgText1, (10, 250+cow))  # built screen 创建文本窗口
            cow += 40
