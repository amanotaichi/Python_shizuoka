#インポート
import sys
args = sys.argv

#引数を変数に代入
words = str(args[1])
pos = int(args[2])
#分割
words = words.split()
#出力
print(words[pos-1], end="")