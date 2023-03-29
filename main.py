import dice

def main():
    n = int(input('주사위 던질 횟수를 입력하세요:'))
    dice = dice.DiceProbability(n)
    dice.calcProbability()
    dice.printProbability()


