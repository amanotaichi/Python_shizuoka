#パッケージのインポート
from introfamily import IntroFam
import sys
args = sys.argv

def main():
    #クラスintroduceを元にオブジェクトを生成する
    fam_intro = IntroFam(args[1], args[2], args[3])
    #メソッドの呼び出し
    print(fam_intro.name_out())
    print(fam_intro.age_out())
    print(fam_intro.cat_out())

if __name__ == '__main__':
    main()