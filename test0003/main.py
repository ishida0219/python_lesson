########################################################
#
#   キャラクターを表示するプログラム
#
#   (C) 2021/12/26 Yoshiteru Ishida
#
########################################################

import pygame
from pygame.locals import *
import sys

#   変数定義
WIDTH = 640
HEIGHT = 480

#   初期化
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

#   画像読込
imgPen = pygame.image.load("animal_stand_penguin.png")

#   メインルーチン


def main():
    while True:

        #   ペンギンを表示する
        window.blit(imgPen, (0, 0))

        #   表示を更新する
        pygame.display.update()

        #   イベントを処理する
        for event in pygame.event.get():

            #   閉じるボタンの場合
            if event.type == QUIT:
                #   ウィンドウを閉じる
                pygame.quit()

                #   プログラムを終了する
                sys.exit()


if __name__ == '__main__':
    main()
