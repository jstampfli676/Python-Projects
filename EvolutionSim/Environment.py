import numpy as np
from Food import Food
from Animal import Animal
import math
import copy

class Environment:
    
    def __init__(self, foodCount):
        self.foodCount = foodCount
        self.foodList = []
        self.animalList = []
        self.width = 500
        for i in range(foodCount):
            coords = np.random.randint(self.width, size=foodCount*2)
            energy = 5
            f = Food(energy, coords[i], coords[i+1], "green")
            self.foodList.append(f)
            i+=1
    
    def addAnimal(self, animal):
        self.animalList.append(animal)
        
    def runSim(self):
        while len(self.animalList)>0:#outer loop to keep the sim running while any animals are alive
            for i in range(len(self.animalList)):
                print("from env", self.animalList[i].x, self.animalList[i].y)
                
                
                sortedFoodList = copy.deepcopy(self.foodList)
                sortedAnimalList = copy.deepcopy(self.animalList)
                
                for t in range(len(sortedFoodList)):
                    sortedFoodList[t].x-=self.animalList[i].x
                    sortedFoodList[t].y-=self.animalList[i].y
                for t in range(len(sortedAnimalList)):
                    if t==i:
                        continue
                        #sortedAnimalList[t].x=sys.maxsize
                        #sortedAnimalList[t].y=sys.maxsize
                    sortedAnimalList[t].x-=self.animalList[i].x
                    sortedAnimalList[t].y-=self.animalList[i].y
                
                sortedFoodList.sort()
                sortedAnimalList.sort()
                
                intel = self.animalList[i].intel
                sees = np.zeros(intel*4)
                count = 0
                z=0
                j=1
                while (count<intel and z<len(sortedFoodList) and j<len(sortedAnimalList)):
                    if sortedFoodList[z]<sortedAnimalList[j]:
                        sees[count*4]=0
                        sees[count*4+1]=sortedFoodList[z].x
                        sees[count*4+2]=sortedFoodList[z].y
                        sees[count*4+3]=sortedFoodList[z].energy
                        z+=1
                    else:
                        sees[count*4]=1
                        sees[count*4+1]=sortedAnimalList[j].x
                        sees[count*4+2]=sortedAnimalList[j].y
                        sees[count*4+3]=sortedAnimalList[j].size
                        j+=1
                    count+=1
                
                if count<intel:
                    while j<len(sortedAnimalList) and count<intel:
                        sees[count*4]=1
                        sees[count*4+1]=sortedAnimalList[j].x
                        sees[count*4+2]=sortedAnimalList[j].y
                        sees[count*4+3]=sortedAnimalList[j].size
                        count+=1
                        j+=1
                    while z<len(sortedFoodList) and count<intel:
                        sees[count*4]=0
                        sees[count*4+1]=sortedFoodList[z].x
                        sees[count*4+2]=sortedFoodList[z].y
                        sees[count*4+3]=sortedFoodList[z].energy
                        count+=1
                        z+=1
                    while count<intel:
                        sees[count*4:(count+1)*4]=-1
                        count+=1
                    
                
                if self.animalList[i].takeAction(sees):
                    #currently deleting animals after some animals have calculated their action
                    del self.animalList[i]
                    i-=1
            #for i in range(self.animalList): forgotten about for now
                #find any collisions between animals/food and resolve them
                
    def euclidDist(x1, x2, y1, y2):
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
    
    

