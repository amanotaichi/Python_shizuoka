import sys
arg = sys.argv

#引数を変数に代入
pos = int(arg[1])
#tupple作成
population = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
print(population[pos-1], end="")