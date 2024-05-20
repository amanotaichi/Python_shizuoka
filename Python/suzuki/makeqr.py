import os
import qrcode
import sys

url = sys.argv[1]
file_name = sys.argv[2] + ".png"

img = qrcode.make(url)
directory_path = "../../../files"
path = os.path.join(directory_path, file_name)

img.save(path)