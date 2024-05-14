# 嫌いな食べ物を引数に指定し、文章を出力
import sys
args = sys.argv
food = args[1]
print("I don't like \"{}\"".format(food), end="")