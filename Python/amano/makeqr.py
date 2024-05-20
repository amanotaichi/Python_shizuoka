import os
import sys
import qrcode

# 引数入力（url, ファイル名
args = sys.argv
url = args[1]
name = args[2]
# パス指定
path = os.path.join("qr", name + ".png")
# QR生成
img = qrcode.make(path)

# 画像保存
img.save(path)