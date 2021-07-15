import random

meter_in_kilometer = 1000
beatles = ["Yannick","Loembet"]

def getFileExt(filename):
    return filename[filename.index(".") + 1:]

def rollDice(num):
    return random.randint(1,num)