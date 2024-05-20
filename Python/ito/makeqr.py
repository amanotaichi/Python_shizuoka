#パッケージのインポート
import qrcode
import sys
import os
args = sys.argv

file_name = args[2]
dir_path = f"./files/{file_name}.png"
#QRコード生成
img = qrcode.make(args[1])
#pathの指定
path = os.path.join(dir_path)
#保存
img.save(path)