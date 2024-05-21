import sys
arg = sys.argv

#引数を変数に代入
country = int(arg[1])

#タプルに世界人口ランキングを定義
population= (
    "China", 
    "India", 
    "U.S.A", 
    "Indonesia", 
    "Pakistan", 
    "Brazil", 
    "Nigeria", 
    "Bangladesh", 
    "Russia", 
    "Mexico"
    )

#引数に指定した順位の国名を出力
if 1 <= country <= 10:
    print(population[country-1],end="")
else:
    print("1から10までの整数を入力してください")