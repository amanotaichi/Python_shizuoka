import sys
arg = sys.argv

#引数を変数に代入
pos = int(arg[1])
ani = str(arg[2])
#リストを定義
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
#第2引数で設定したインデックスの位置に、第3引数の動物名を挿入する
animals.insert(pos,ani)
#リストの最後の要素を削除する
animals.pop()
#リストを昇順に並べ替える
animals.sort()
#操作した結果のリストを出力
print(animals,end="")