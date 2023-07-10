import numpy as np

class Predict:
    def __init__(self):
        details = open("Predector\Contents.txt","r")
        self.requirements = []
        for i in details:
            self.requirements.append(float(i))


    def transform(self,X):
            return np.array((X - self.requirements[1])/self.requirements[0])
        
    def reverse(self,X):
        return self.addComma(str(int(X * self.requirements[0] + self.requirements[1])))
        
    def predict(self,X):
        return np.array(self.requirements[2] * X + self.requirements[3])
    
    def addComma(self,x):
        
        x = x[::-1]
        y = ''

        for i in range(len(x)):
            if i%3 == 0 and i!= 0:
                y += ','
                
            y+= x[i]

        return y[::-1]
