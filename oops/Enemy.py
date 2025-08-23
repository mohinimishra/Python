# Abstraction example class
class Enemy:
    def __init__(self,type_of_enemy,name, language,health_point=10): #initialize 
        self.type_of_enemy=type_of_enemy
        self.health_point=health_point
        self.name=name
        self.language=language
    def talk(self):
        print(f'I am a {self.type_of_enemy}. Be prepared!')
        
    def  walk_forward(self):
        print(f'{self.type_of_enemy} attacking you. Your health point is {self.health_point}')
        
    def intro(self, name, language):
        self.name = name
        self.language = language
        print(f"My name is {self.name} and i Love {self.language}")
        