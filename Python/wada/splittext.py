import sys
arg = sys.argv

#引数を変数に代入
i = str(arg[1])
j = int(arg[2])

#指定した位置の単語を出力する
i = i.split( )
print(i[j-1],end="")