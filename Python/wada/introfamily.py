from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, catname):
        super().__init__(name, age)
        self.catname = catname
    
    def cat_out(self):
        catnametxt = "猫の名前は、" + self.catname + "です"
        return catnametxt