import sys
args = sys.argv
 
def calcvalue(n):
  #remainderは余りの変数
  remainder = n % 2
  if remainder==0:
    print(f'{n}は偶数')
  else:
    print(f'{n}は奇数')
 
for arg in args[1:]:
  calcvalue(int(arg))

