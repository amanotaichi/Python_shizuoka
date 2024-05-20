#パッケージのインポート
from introduce import Intro

class IntroFam(Intro):
    #初期化
    def __init__(self, name, age ,cat_name):
        super().__init__(name, age)
        self.cat = cat_name
    #猫の名前メソッド
    def cat_out(self):
        cattext = "飼い猫の名前は、" + self.cat + "です"
        return cattext
    

