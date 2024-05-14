#インポート
import sys
args = sys.argv

#入力内容(引数)を変数に代入
name = args[1]
try:
    #表示
    print("Hello", name, "!", end="")
except:
    print("入力がありません")
