import math
import numpy as np
stativ_høyde = 2 #stativet er 1,5 over bakken
def a_sektor(a):    #grader fra rett ned (0*)
    a = math.radians(a)
    return round((1/math.cos(a))*math.sin(a),2)  #sec(x) = 1/cos(x)

def c_sektor(c):    #grader over 90* (som er rett frem)
    c = math.radians(c)
    return round(stativ_høyde*math.sin(c)*(1/math.cos(c)),2)

def høyde(a,c):
    return a_sektor(a)*c_sektor(c)+stativ_høyde

for i in range(75, 89):
    print(f"{i}°: {a_sektor(i)}")
print("-----------------------")
for i in range(0, 75):
    print(f"{i}°: {c_sektor(i)}")