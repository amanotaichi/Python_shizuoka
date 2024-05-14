# 自分の名前を表示
import sys
args = sys.argv
name = args[1]
print(f"Hello", name, "!", end="")

# ↓fstring
# print(f"Hello {name} !", end="")