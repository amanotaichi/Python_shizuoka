from introduce import Intro
import sys

myname = sys.argv[1]
myage = sys.argv[2]

myself = Intro(myname, myage)
print(myself.name_out())
print(myself.age_out())