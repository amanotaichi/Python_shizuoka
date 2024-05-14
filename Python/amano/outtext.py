# ライブラリインポート
import sys

# 引数入力
args = sys.argv
# 出力
# print("I don't like \"" + args[1] + "\"", end="")
print("I don't like \"{0}\"".format(args[1]), end="")