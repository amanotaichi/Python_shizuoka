#インポート
import sys
args = sys.argv

#入力内容(引数)を変数に代入
number = int(args[1])
#奇数偶数判定
if number % 2 == 0:
    print("偶数",end="")
else:
    print("奇数",end="")
