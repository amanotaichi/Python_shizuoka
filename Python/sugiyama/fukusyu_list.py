# 準備
import sys
args = sys.argv

#代入
animal1 = int(args[1])
animal2 = args[2]

#リスト作り
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

#リストへ挿入
animals.insert(animal1, animal2)

#リスト