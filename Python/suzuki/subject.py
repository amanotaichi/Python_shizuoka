# 数学、国語、英語の得点を引数に設定し、2つの合格基準を満たすか満たさないか判定
import sys
args = sys.argv

math_score = int(args[1])
japanese_score = int(args[2])
english_score = int(args[3])
sum_score = math_score + japanese_score + english_score

# 合格基準1を満たすか検証
if (
    math_score >= 70
    and japanese_score >= 70
    and english_score >= 70
    ) or (
        sum_score >= 220
    ):
# 合格基準1を満たす場合、合格基準2を満たすか検証
# 50点未満は不合格→50点以上は合格
    if (
        math_score >= 50
        and japanese_score >= 50
        and english_score >= 50
    ):
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")