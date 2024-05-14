import sys
arg = sys.argv

#引数を変数に代入
math = int(arg[1])
japanese = int(arg[2])
english = int(arg[3])

#点数を合計
sum = math+japanese+english

if (math >= 70 and japanese >= 70 and english >=70)or(sum >= 220):
    if (math < 50 or japanese < 50 or english < 50):
        print("不合格",end="")
    else:
        print("合格",end="")
else:
    print("不合格",end="")