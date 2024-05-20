import sys
arg = sys.argv

import os
import qrcode

creat_url = arg[1]
file_name = arg[2] + ".png"

#QRコードを生成
img = qrcode.make(creat_url)

# http://job.mynavi.jp/26/pc/toppage/displayTopPage/index"

#相対パスを生成
directory_path = "../../../files"
path = os.path.join(directory_path,file_name)

#pingファイルの生成
img.save(path)