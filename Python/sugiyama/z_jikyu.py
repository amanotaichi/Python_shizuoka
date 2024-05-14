# 時給計算プログラム

# 時給の入力
User     = input("時給はいくらですか？")
jikyu    = int(User)

# 時間の入力
User     = input("何時間働きましたか？")
jikan    = int(User)

# 計算
kyuryou  = jikyu * jikan

# 結果を表示
fmt = """
時給は{0}円で、{1}時間働いたので…
給料は、{2}円です。
"""

desc = fmt.format(jikyu, jikan, kyuryou)
print(desc)