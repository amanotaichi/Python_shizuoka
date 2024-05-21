# 準備
from introduce import Intro
import sys
args = sys.argv

#引数を変数に代入
Intro_name = args[1]
Intro_age = args[2]

#Introに変数を渡す
myself = Intro(Intro_name, Intro_age)

#出力
print(myself.generate_name_intro)
print(myself.generate_age_intro)



