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



#   キャラクター管理クラス
class Splite:
    #   キャラクターの座標
    x = 0
    y = 0
    image = None

    #   初期化処理
    def __init__(self, file) -> None:
        #   画像読込
        self.image = pygame.image.load(file)
        pass

    def update(self,window):
        window.blit(self.image, (self.x-20, self.y-20))

    def setXY(self, x, y ):
        self.x = x
        self.y = y


def main():
    #   初期化
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    penguin = Splite( "./image/animal_stand_penguin.png")


    #   メインルーチン
    while True:

        #   画面を白で塗りつぶす
        window.fill((255,255,255))

        #   マウスの座標を取得する
        (x, y) = pygame.mouse.get_pos()
        penguin.setXY( x, y )

        #   ペンギンを表示する
        penguin.update(window)

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
