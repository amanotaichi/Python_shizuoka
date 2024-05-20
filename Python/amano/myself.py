import sys
import introduce

# 引数入力
args = sys.argv


# インスタンス作成、初期化時に名前と年齢を設定
myself = introduce.Intro(name = args[1], age = args[2])
# インスタンスから名前と年齢を取得表示
print(myself.name_out())
print(myself.age_out())