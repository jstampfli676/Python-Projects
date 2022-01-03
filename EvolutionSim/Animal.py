from Network import Network
import math

class Animal:
    
    def __init__(self, speed, size, intel, x, y, color):
        self.speed = speed
        self.size = size
        self.intel = intel
        self.x = x
        self.y = y
        self.color = color
        self.network = Network(4*intel)
        self.curEnergy = 10
        
    def takeAction(self, visual):
        n,w = self.network.prediction(visual)
        
        self.x -= int(w * self.speed)
        self.y -= int(n * self.speed)
        print("took action",self.x,self.y)
        return self.consumeEnergy()
        
    def __lt__(self, other):
        return self.animalDist()<other.animalDist()
    
    def animalDist(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def consumeEnergy(self):
        self.curEnergy-=1
        if self.curEnergy<=0:
            return True
        return False
        
    

