
from introfamily import IntroFam
import sys
args = sys.argv

family = IntroFam(args[1],args[2],args[3])

print(family.name_out())
print(family.age_out())
print(family.cat_out())
