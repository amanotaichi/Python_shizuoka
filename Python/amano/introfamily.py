import introduce

class IntroFam(introduce.Intro):
    def __init__(self, name, age, cat_name):
        super().__init__(name, age)
        self.cat_name = cat_name
    def name_out(self):
        return super().name_out()
    def age_out(self):
        return super().age_out()
    def cat_out(self):
        cat_name = "飼い猫の名前は、" + self.cat_name + "です"
        return cat_name
