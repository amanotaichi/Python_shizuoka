#import
import sys
arg = sys.argv
from func_salary import calcsalary

#メイン関数
def main():
    #入力値を整える
    arg.pop(0)
    #一つずつ取り出して関数へ渡す
    for i in arg:
        i = int(i)
        #関数の実行と返り値取得
        pay,tax = calcsalary(i)
        #表示
        print("支給額:" + pay + "、" + "税額:" + tax)

if __name__ == '__main__':
    main()
