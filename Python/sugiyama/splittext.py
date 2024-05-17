# 準備
import sys
args = sys.argv

# 第二引数設定
n1 = args[1] 

# 第三引数設定
n2 = int(args[2])

# 分割したものを変数へ代入
text = n1.split()

# 取り出し
print(text[n2-1])