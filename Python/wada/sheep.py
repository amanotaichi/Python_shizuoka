import sys
arg = sys.argv

#引数を変数に代入
n = int(arg[1])

#n匹までひつじをカウント
for i in range (1,n+1):
    print(f"ひつじが{i}匹")