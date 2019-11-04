# -*- coding: utf-8 -*-
"""
设置参数
"""

import time
import pygame
from text import Text


class InputData():
    '''
    输入的动画显示
    '''
    def __init__(self, path):
        self.textGenerator = Text(path, 60)
        self.text = self.textGenerator.getText()
        # 逻辑部分
        self.time = time.time()  # 开始时间
        self.words = 0  # 总字数
        self.speed = 0  # 打字速度
        self.flag = True  # 正确的字数
        self.wordsCorr = 0  # 错误的字数
        self.countdown = 60
        self.startTime = 0
        self.result = ''
        self.welcomeWords = '欢迎来到王者打字游戏\n请点击屏幕开始游戏'
        # 图形部分
        self.cover = pygame.image.load('files/cover.jpeg')
        self.pos = 0  # 输入位置
        self.wordsPage = 0  # Nb of words passed by in single page
        self.vMargin = 10  # 垂直距离
        self.hMargin = 10  # 水平距离
        self.paddingX = 10  # 距离界面左部距离
        self.paddingY = 50  # 距离界面顶部距离
        # 空格宽度
        self.space = pygame.font.Font("files/ziti.ttf", 36).size(' ')[0]
        # 最大宽度
        self.surface = pygame.display.get_surface()
        max_width, _ = self.surface.get_size()
        self.max_width = max_width - self.hMargin
        self.update()


    def update(self):
        '''
        多行字进行渲染
        '''
        self.speed = self.words/(time.time()-self.time+1e-6)*60
        self.countdown = 60 - (time.time()-self.time)
        words = self.text.split(' ')
        global x, y
        x, y = self.paddingX, self.paddingY
        count = 0

        def renderWord(wordText, color, highlight):
            global x, y
            word_surface = pygame.font.Font(
                "files/ziti.ttf", 36).render(wordText, 1, color)
            word_width, word_height = word_surface.get_size()
            word_height += self.vMargin
            if x + word_width >= self.max_width:
                x = self.paddingX
                y += word_height
            if highlight is not None:
                word_surface.blit(highlight, (0, 0))
            self.surface.blit(word_surface, (x, y))
            x += word_width + self.space

        # 打字
        for i in range(self.wordsPage):
            renderWord(words[i], (255, 255, 255), None)
            count += len(words[i])+1
        
        # 单词被输入之后
        highlight = pygame.font.Font("files/ziti.ttf", 36).render(
            words[self.wordsPage][:self.pos-count], 1, (255, 255, 255))
        renderWord(words[self.wordsPage], (0, 0, 0), highlight)

        # 单词没有被输入
        for i in range(1+self.wordsPage, len(words)):
            renderWord(words[i], (0, 0, 0), None)

    def getSpeed(self):
        return self.speed

    def getWords(self):
        return self.words

    def getCorrWords(self):
        return self.wordsCorr

    def getCountDown(self):
        return self.countdown
    
    def getStartTime(self):
        self.startTime = time.time()
        return self.startTime
    
    def getCover(self):
        return self.cover

    def getWelcomeWords(self):
        return self.welcomeWords

    def getResult(self):
        return self.welcomeWords + '\n一分钟打字战绩:\n  速度:%.1f/min\n  错误单词: %s/%s'% (
            self.speed, self.wordsCorr, self.words)  
    
    def countWords(self):
        self.words += 1
        self.wordsPage += 1
        if self.flag:
            self.wordsCorr += 1
        self.flag = True

    def keyin(self, key):
        if self.text[self.pos] == " ":
            self.countWords()
        elif key != self.text[self.pos]:
            self.flag = False

        self.pos += 1
        if len(self.text) == self.pos:
            self.pos = 0
            self.text = self.textGenerator.getText()
            self.countWords()
            self.wordsPage = 0
