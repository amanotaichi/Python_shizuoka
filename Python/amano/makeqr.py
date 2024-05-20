import os
import sys
import qrcode

args = sys.argv
url = args[1]
name = args[2]
path = os.path.join("qr", name + ".ping")
img = qrcode.make(path)

img.save(path)