import sys
arg = sys.argv

#引数を変数に代入
n = int(arg[1])

#n匹までひつじをカウント
for i in range (1,n+1):
    print("ひつじが"+ str(i) +"匹")
    i += 1