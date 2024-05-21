import sys
num = int(sys.argv[1])

TEXT_PATH = "../../../files/sheep.txt"
sheep_file = open(TEXT_PATH, mode="w", encoding="utf-8")

for i in range(num):
    sheep_file.write("ひつじが"+str(i+1)+"匹\n")

sheep_file.close()