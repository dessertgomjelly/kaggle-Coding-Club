import random

class Dice:
    def __init__(self):
        self.number = None
        
    def roll(self):
        self.number = random.randint(1, 6)
        return self.number
 
class DiceProbability:
    def __init__(self,n):
        self.n = n
        self.a = []
        self.b = [0]*6
    def calcProbability(self):
        for i in range(self.n):
            num = Dice().roll()
            self.a.append(num)
            self.b[num-1] += 1/self.n
            
    def printProbability(self):
        print('총횟수 : %d' %self.n)
        for i in range(6):
           print('주사위 {}: {:.3f} 비율 : {:.3f}'.format(i+1, self.b[i]*self.n, self.b[i]))
             
       
def main():
    num = int(input("주사위를 몇 번 굴리시나요? "))
    dice = DiceProbability(num)
    dice.calcProbability()
    dice.printProbability()

