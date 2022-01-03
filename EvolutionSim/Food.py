import math

class Food:
    
    def __init__(self, energy, x, y, color):
        self.energy = energy
        self.x = x
        self.y = y
        self.color = color
        
    def __lt__(self, other):
        return self.animalDist()<other.animalDist()
    
    def animalDist(self):
        return math.sqrt(self.x**2+self.y**2)

