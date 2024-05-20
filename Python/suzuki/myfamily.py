from introfamily import IntroFam
import sys

myname = sys.argv[1]
myage = sys.argv[2]
mycat = sys.argv[3]

myfamily = IntroFam(myname, myage, mycat)
print(myfamily.name_out())
print(myfamily.age_out())
print(myfamily.cat_out())
