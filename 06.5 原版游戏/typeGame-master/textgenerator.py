# -*- coding: utf-8 -*-

import re


class TextGeneratorFromFile():
    '''
    从文件产生文本
    numWords: 每次出现的单词数量
    '''

    def __init__(self, path, numWords):
        self.path = path
        self.pos = 0
        self.numWords = numWords
        with open(self.path, 'r', encoding='utf-8') as f:
            self.text = re.findall(r'\w+', f.read())

    def getText(self):
        if self.pos + self.numWords >= len(self.text):
            self.pos = 0
        text = " ".join(self.text[self.pos: self.pos+self.numWords])
        self.pos += self.numWords
        return text
