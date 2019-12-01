import math

def aoc011(filename, ):

    B = open(filename).read().split('\n')
    B = [x for x in B if x]
    for i, v in enumerate(B): B[i] = math.floor(int(v)/3) - 2

    print(sum(B))

def aoc012(filename):

    B = open(filename).read().split('\n')
    B =  [x for x in B if x]
    A = []
    for i, v in enumerate(B):
        S = 0 
        s = math.floor(int(v)/3) - 2
        S += s
        while s > 0:
            s = math.floor(s/3) - 2 
            if s > 0 : S += s   
        A.append(S)
    print(sum(A)) 

#aoc011('days/input011.txt')
aoc012('days/input011.txt')