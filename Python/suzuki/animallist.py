# 動物の名前リストを定義し、リストを操作
import sys
index = int(sys.argv[1])
animal_name = sys.argv[2]
animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 第2引数で設定したインデックスの位置に、第3引数の動物名を挿入する
# インデックスが1以上4以下の時は、インデックスとリストの番号を揃えるため-1する
# インデックスが0のとき、-1してしまうとエラーになるのでそのままにする
# インデックスが5以上の時はリストの一番最後に要素を追加する
if (index == 0):
    index = 0
    animal_list.insert(index, animal_name)
elif (index <= 4):
    index -= index
    animal_list.insert(index, animal_name)
else:
    animal_list.append(animal_name)

# リストの最後の要素を削除する
animal_list.pop()

# リストを昇順に並び替える
animal_list.sort()
print(animal_list, end="")

