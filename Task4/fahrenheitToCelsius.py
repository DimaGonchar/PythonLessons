from typing import DefaultDict

def toCelsius(value):
    value= float(value)
    cel = 5.0*(value - 32) / 9
    return round(cel,1)
    
import math  
import sys

def geronSquare(a, b, c):
    p= float((a+b+c)/2)
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return float(s)

if __name__ == "__main__":
 print(geronSquare(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])))
    

