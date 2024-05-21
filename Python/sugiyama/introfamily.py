#準備
#基底クラスIntroを読み込む
from introduce import Intro

#派生クラス IntroFam
class IntroFam(Intro):

    def __init__(self, generate_name_intro, generate_age_intro, cat):
        self.cat = cat


    def cat_out(self):
        return f"飼い猫の名前は、{self.cat}です。"

