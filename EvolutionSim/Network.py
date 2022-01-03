import numpy as np

class Network:
    
    
    def __init__(self, inputsize):
        self.h1 = np.random.rand(16, inputsize)
        self.h2 = np.random.rand(8, 16)
        self.output = np.random.rand(2, 8)
        
    def relu(self, value):
        return np.maximum(value, 0)
    
    def sigmoid(self, value):
        return (1/(1+np.exp(-value)))
    
    def tanh(self, value):
        return 2*self.sigmoid(2*value)-1
    
    def prediction(self, inputData):
        o1 = self.tanh(np.dot(self.h1, inputData))
        o2 = self.tanh(np.dot(self.h2, o1))
        return self.tanh(np.dot(self.output, o2))
