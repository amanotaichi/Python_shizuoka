# 指定したn番目の単語を出力
import sys
args = sys.argv

# 文章を入力
sentence = args[1]
# 取り出す単語の番号を指定
number = int(args[2])

if number != 0:
    number = number - 1

# 文章を半角スペースで分割
word_list = sentence.split()
# 指定した番号の単語を取り出す
word = word_list[number]

print(word, end="")