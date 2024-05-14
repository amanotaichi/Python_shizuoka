user = input("時給はいくらですか？")
jikyuu = int(user)

user = input("何時間働きましたか？")
jikan = int(user)

kyuryou = jikan*jikyuu

fmt = """
時給{0}円で、{1}時間働いたので．．．
給料は、{2}円です。
"""
desc = fmt.format(jikyuu,jikan,kyuryou)
print(desc)
