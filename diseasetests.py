import numpy as np

class Person:
    def __init__(self):
        self.hasDisease = np.random.choice([0,1],p=[9999/10000, 1/10000])

def blah():
    print("HERE !!!")