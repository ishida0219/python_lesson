########################################################
#
#   マウスでキャラクターを動かすプログラム
#
#   (C) 2021/12/27 Yoshiteru Ishida
#
########################################################

import pygame
from pygame.locals import *
import sys

#   変数定義
WIDTH = 640
HEIGHT = 480

#   キャラクターの座標
x = 0
y = 0

#   初期化
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

#   画像読込
imgPen = pygame.image.load("./image/animal_stand_penguin.png")

#   メインルーチン


def main():
    while True:

        #   画面を白で塗りつぶす
        window.fill((255,255,255))

        #   マウスの座標を取得する
        (x, y) = pygame.mouse.get_pos()

        #   ペンギンを表示する
        window.blit(imgPen, (x-20, y-20))

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
