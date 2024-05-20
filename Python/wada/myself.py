from introduce import Intro

import sys
args = sys.argv

name = args[1]
age = args[2]

myself = Intro(name,age)
print(myself.name_out())
print(myself.age_out())