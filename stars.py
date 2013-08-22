"""
Author: Novanator 2012
Program: STARS
""" 

def writestars(n):                  
    for j in range(n): 
        print ("*",end="")
    print()

writestars(5)

#A block of 17x4 stars
n=17
for k in range(4):                   
    for j in range(n): 
        print ("*",end="")
    print()

#Prints FEL in star letters
for n in [5,1,3,1,1,0,5,1,3,1,5,0,1,1,1,1,5,-8,-5]:
    for j in range(n):                  
        print ("*",end="")
    print()
    
#User input for stars
for k in range(4):
    n=int(input("Number of stars *:"))
    for j in range(n):             
        print ("*",end="")
    print()



