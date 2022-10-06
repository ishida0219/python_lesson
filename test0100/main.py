########################################################
#
#   ランダムな文字列を生成する
#
#   (C) 2021/12/29 Yoshiteru Ishida
#
########################################################

import string
import random
import secrets
import time

#   ランダムな文字列を作る関数1
def random_string1( n ):
    #   乱数を初期化する
    random.seed()

    #   文字を取り出すテーブル
    table = "abcdefghijklmnopqrstuvwxyz0123456789"

    #   値を格納する文字列
    result = ""

    #   指定回数ループする
    for i in range( 0, n ):

        #   乱数を生成する
        r = random.randint(0,len(table)-1)

        #   文字列を取り出して結果に連結
        result = result + table[r] 

    return result

#   ランダムな文字列を作る関数2
def random_string2( n ):
    #   乱数を初期化する
    random.seed()

    #   文字を取り出すテーブル
    table = string.ascii_letters + string.digits

    #   ランダムな文字列を取り出す
    result = "".join( [random.choice(table) for i in range(n)])

    return result


#   ランダムな文字列を作る関数3
def random_string3( n ):
    return secrets.token_urlsafe(n)[0:n]


def main():
    t = time.localtime(None)
    while time.localtime(None) == t :
        pass
        
    i = 0
    t = time.localtime(None)
    while time.localtime(None) == t :
        result = random_string3( 32 )
        i = i + 1

if __name__ == '__main__':
    main()

