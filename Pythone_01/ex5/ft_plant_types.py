class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, color):
        super().__init__(name, height, age)
        self.color = color
        self.__is_blooming = 0
    
    def bloom()
        self.__is_blooming = 1

class Tree(Plant):
    def __init__(self, trunck_diameter):
        super().__init__(name, height, age)
        self.trunck_diameter = trunck_diameter
    
    def produce_shade()

class Vegetable(Plant):
    def __init__(self, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value