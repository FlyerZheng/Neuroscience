#for the submission uncomment the submission statements
#so submission.README

from math import *
import numpy as np
from submission import *

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False
    

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")
    
    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "
        
        if d3:
            word+="_"
        else:
            word+=" "
        
        if d2:
            word+="|"
        else:
            word+=" "
        
        print(word)

    

    pattern_b=list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))
        
submission=Submission("Xiangtian ZHENG")
submission.header("Xiangtian ZHENG")

six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)
seven_segment(one)

#weight_matrix
weight_matrix = np.zeros((11,11))

def matrix_formula(i,j):
    total = 0.0
    total += six[i]*six[j]+three[i]*three[j]+one[i]*one[j]
    return total/3


for i in range(11):
    for j in range(11):
        if i != j:
            weight_matrix[i][j] = matrix_formula(i,j)

def energy(pattern):
    total = 0
    for i in range(11):
        for j in range(11):
            total += weight_matrix[i][j]*pattern[i]*pattern[j]
    return -1*total/2

def evolve(pattern):
    copy = pattern.copy()

    def g(x):
        if x>0:
            return 1
        else:
            return -1

    for i in range(11):
        total = np.dot(np.array(copy),weight_matrix[i])
        pattern[i] = g(total)

    print(pattern)
    print("energy:")
    print(energy(test))
    

    if pattern == copy:
        return pattern
    else:
        submission.seven_segment(pattern)
        submission.print_number(energy(pattern))
        submission.qquad()
        evolve(pattern)

##this assumes you have called your weight matrix "weight_matrix"
submission.section("Weight matrix")
submission.matrix_print("W",weight_matrix)

# --------test1--------
print("test1")
submission.section("Test 1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]
seven_segment(test)
submission.seven_segment(test)

##for COMSM0027

#where energy is the energy of test
submission.print_number(energy(test))

#this prints a space
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step
evolve(test)
# ---------test2-------
print("test2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
submission.section("Test 2")

seven_segment(test)


submission.seven_segment(test)

##for COMSM0027
#where energy is the energy of test
submission.print_number(energy(test))

##this prints a space
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step
evolve(test)

submission.bottomer()