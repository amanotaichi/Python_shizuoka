import sys
import introfamily

# 引数入力
args = sys.argv

# インスタンス作成、初期化時に名前と年齢を設定
myself = introfamily.IntroFam(name = args[1], age = args[2], cat_name = args[3])
# インスタンスから名前と年齢を取得表示
print(myself.name_out())
print(myself.age_out())
print(myself.cat_out())
