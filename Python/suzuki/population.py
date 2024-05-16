# タプルに定義した世界人口ランキングから、引数に指定した順位の国名を出力
import sys 
index = int(sys.argv[1])

if (index >= 1 and index <= 10):
    index = index - 1
else:
    index = 0

population = (
    "China", "India", "U.S.A", "Indonesia", "Pakistan", 
    "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(population[index], end="")