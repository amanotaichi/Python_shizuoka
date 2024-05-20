#パッケージのインポート
from introduce import Intro
import sys
args = sys.argv

def main():
    #クラスintroduceを元にオブジェクトを生成する
    my_intro = Intro(args[1], args[2])
    #メソッドの呼び出し
    print(my_intro.name_out())
    print(my_intro.age_out())

if __name__ == '__main__':
    main()


