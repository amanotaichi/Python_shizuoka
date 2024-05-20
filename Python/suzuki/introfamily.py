from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, cat):
        super().__init__(name, age)
        self.cat = cat

    def name_out(self):
        return super().name_out()
    
    def age_out(self):
        return super().age_out()
    
    def cat_out(self):
        cattxt = f"飼い猫の名前は、{self.cat}です"
        return cattxt