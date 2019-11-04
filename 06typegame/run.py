import pygame
from pygame.locals import *
from captions import Caption
from setting import InputData
import sys
import time
from music import runMusic


class Game():
    '''
    图形用户界面
    '''

    def __init__(self, textSource):
        self.textSource = textSource
        self.speedLimit = 70
        self.clock = pygame.time.Clock()
        self.screenRect = Rect(0, 0, 640, 480)
        self.screen = pygame.display.set_mode(self.screenRect.size)
        self.background = pygame.Surface(self.screenRect.size).convert()
        self.elements = pygame.sprite.RenderUpdates()
        self.inputData = InputData(textSource)
        self.music = runMusic()
        self.caption = Caption()
        self.game_over = True
        self.elements.add(self.caption)
        self.background.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

        self.coverText = self.inputData.getWelcomeWords()
        pygame.display.set_caption('王者打字游戏')
        pygame.display.update()

    def start(self):
        self.music.run()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                    # 忽视功能键
                    if len(event.unicode) > 0:
                        self.inputData.keyin(event.unicode)
                elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标抬起
                    if self.game_over:
                        self.game_over = False
                        startTime = self.inputData.getStartTime()

            if self.game_over:
                cover = self.inputData.getCover()
                self.screen.blit(cover, (0, 0))
                self.caption.print_text(self.screen, 10, 400, self.coverText, (232, 206, 144))

            else:
                typingSpeed = self.inputData.getSpeed()
                words = self.inputData.getWords()
                corrWords = self.inputData.getCorrWords()
                countDown = 60 - (time.time() - startTime)
                self.caption.setText(typingSpeed, words, corrWords, countDown)

                # 根据打字速度改变背景颜色
                if typingSpeed > self.speedLimit:
                    typingSpeed = self.speedLimit
                self.screen.fill([(int)(255 - 255 * typingSpeed / self.speedLimit),
                                  (int)(255 * typingSpeed / self.speedLimit),
                                  0])

                self.inputData.update()
                self.elements.update()
                self.elements.draw(self.screen)
                self.clock.tick(30)
                if countDown <= 0:
                    self.coverText = self.inputData.getResult()
                    self.game_over = True
                    self.inputData = InputData(self.textSource)
            pygame.display.update()


def main():
    dataFile = 'files/speed.txt'
    pygame.init()
    g = Game(dataFile)
    g.start()


if __name__ == '__main__':
    main()
