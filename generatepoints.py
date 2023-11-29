import random

def generatepoints(seed):
    random.seed(seed)
    points = [random.uniform(0, 1) for _ in range(100)]
    return points