# 時給の計算
# 時給の入力
user = input("時給はいくらですか？")
jikyu = int(user)

# 時間の入力
user = input("何時間働きました？")
jikan = int(user)

# 計算
kyuuryou = jikyu * jikan

# 表示
fmt = """
時給{0}円で、{1}時間働いたので...
給料は、{2}円です。
"""
desc = fmt.format(jikyu, jikan, kyuuryou)
print(desc)