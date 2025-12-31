#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
class FloweringPlant(Plant):
    def __init__(self, flower_color, is_blooming):
        super().__init__(name, height, age)
        self.flower_color = color
        self.is_blooming = False

class PrizePlant(FloweringPlant):
    def __init__(self, prize_points):
        super().__init__(name, height, age, flower_color, is_blooming)
        self.prize_points
