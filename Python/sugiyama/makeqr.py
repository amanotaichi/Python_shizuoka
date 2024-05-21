# 準備
import sys
args = sys.argv

#パッケージをインポート
import qrcode

#モジュール「os」のimport
import os

#引数を変数に渡す
qr_url = args[1]
qr_file = args[2] + ".png"


#qrコードを作成
img = qrcode.make(qr_url)


#os.path.joinを利用して相対パスを生成する
#相対パス("../files/~~.png")となる
file_class = "../../../files"
path = os.path.join(file_class, qr_file)

#pngファイルの生成
img.save(path)