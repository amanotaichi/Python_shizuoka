import sys
args = sys.argv

animal_arg1 = int(args[1])
animal_arg2 = args[2]

animal = ["giraffe","tiger","zebra","elephant","lion"]

# 第二引数…
animal.insert(animal_arg1, animal_arg2)

# リストの最後の要素を削除する
animal.pop()

# リストを昇順に変更
animal.sort()

# 出力
print(animal,end="")
