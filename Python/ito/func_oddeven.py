import sys
args = sys.argv

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

#メイン関数
def main():
    #引数を変数に代入
    num = args
    num.pop(0)
    #偶数奇数判定関数呼び出し
    for i in num:
        i = int(i)
        calcvalue(i)

if __name__ == '__main__':
    main()

"""
#インポート
import sys
args = sys.argv

#偶数奇数判定関数定義
def calcvalue(self):
    for i in self:
        i = int(i)
        if i % 2 == 0:
            print(f"{i}は偶数")
        else:
            print(f"{i}は奇数")

#メイン関数
def main():
    #引数を変数に代入
    words_list = args
    words_list.pop(0)
    #偶数奇数判定関数呼び出し
    calcvalue(words_list)

if __name__ == '__main__':
    main()
"""

