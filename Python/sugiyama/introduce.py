class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def generate_name_intro(self):
        return f"私の名前は、{self.name}です"

    def generate_age_intro(self):
        return f"私の年齢は、{self.age}歳です"
    
    