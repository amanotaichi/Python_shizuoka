# 準備
import sys
args = sys.argv

# 代入
sheep = int(args[1])

#読み書き処理
with open("/home/matcha-23training/files/sheep.txt", mode="w", encoding="utf-8") as f:
    # for文
    for i in range(sheep):         
        f.write("ひつじが" + str(i + 1) + "匹\n")




