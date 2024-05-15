import sys
arg = sys.argv

#引数を変数に代入
i = int(arg[1])
j = str(arg[2])
 
#リストを定義
animal_name = ["giraffe", "tiger", "zebra", "elephant", "lion"]

#第2引数で設定したインデックスの位置に、第3引数の動物名を挿入する
animal_name.insert(i,j)

#リストの最後の要素を削除する
animal_name.pop()

#リストを昇順に並べ替える
animal_name.sort()

#操作した結果のリストを出力
print(animal_name,end="")