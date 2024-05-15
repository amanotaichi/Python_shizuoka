import sys
args = sys.argv

num = int(args[1])

total = 0

while total < 100:
    total += num
    if total == 100:
        print("Just 100!")
        break
    elif total >= 100:
        print("Over!")
        break