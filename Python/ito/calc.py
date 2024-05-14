#インポート
import sys
args = sys.argv

#引数を変数に代入
try:
    input1 = int(args[1])
    input2 = int(args[2])
    input3 = int(args[3])
except TypeError as e:
    print("入力がありません", e)
#引数を合計
result = input1 + input2 + input3
#結果の表示
print(result, end="")