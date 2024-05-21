import sys
arg = sys.argv

#引数を変数に代入
n = int(arg[1])

with open("/home/matcha-23training/projects/files/sheep.txt",mode="w", encoding="utf-8") as s:
    for i in range(n):
        s.write("ひつじが"+ str(i+1)+"匹\n")

