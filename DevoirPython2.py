import numpy as np
import random

def Exo1():
    vect=np.arange(0,21)
    for i in range (9,16):
        vect[i]=-vect[i]
    print(vect)
    

def Exo2():
    vect=np.arange(15,56)
    for i in range(1,len(vect)):
        print(vect[i])

def Exo3():
    n1=int(input("Enter the minimum value for the matrix"))
    n2=int(input("Enter the maximum value for the matrix"))
    matrix=np.random.randint(n1,n2,size=(3,4))
    print(matrix)
    
def Exo4():
    vect=np.linspace(5,50,10)
    print(vect)
    
def Exo5():
    vect=np.random.randint(0,10,size=5) 
    print(vect)
    
def Exo6():
    vect1=np.random.randint(0,10,size=5) 
    print(vect1)
    vect2=np.random.randint(0,10,size=5)
    print(vect2)
    matrix=np.matmul(vect1,vect2)
    print(matrix)

def Exo7():
    matrix=np.random.randint(10,22,size=(3,4))
    print(matrix)
    
def Exo8():
    matrix=np.random.randint(10,21,size=(3,4))
    print(matrix)
    nbrows=len(matrix)
    nbcol=len(matrix[1])
    print("Number of rows is {} and number of columns is {}".format(nbrows,nbcol))
    
def Exo9(): 
    matrix=np.empty((4,4))
    for i in range(0,4):
        for j in range(0,4):
            matrix[i,j]=random.randint(0,1)
            if(i==j):
                matrix[i,j]=0
    print(matrix)

def Exo10():
    
    Array1=np.array[0,10,20,40,60]
    Array2=np.array[10, 30, 40]
    J=[]
    for i in range(len(Array1)):
        for j in range(len(Array2)):
            if(Array1[i]==Array2[j]):
                J.append(Array1[i])
    
    print("Array1 : {}".format(Array1))
    print("Array2 : {}".format(Array2))
    print("Common values beetwen two arrays : {} ".format(J))
    
def Exo11():
    
    array1=np.array([10,10,20,20,30,30])
    array2=np.array(([1,1]),([2,3]))
    L1=[]
    L2=[]
    for i in range(len(array1)):
        if array1[i] not in L1:
            L1.append(array1[i])
    for i in range(len(array2)):
        for j in range(len(array2[0])):
            if array2[i,j] not in L2:
                L2.append(array2[i,j])
                
    print("Original Array \n{} ".format(array1))
    print("Unique Elements of the above array : \n{} ".format(L1))
    print("Original Array \n{} ".format(array2))
    print("Unique elements of the above array : \n{} ".format(L2))

def Exo12():
    
    vect1=np.random.randint(0,10,size=5) 
    vect2=np.random.randint(0,10,size=5) 
    crossprod=np.cross(vect1,vect2)
    print(crossprod)
    
def Exo14():
    vect=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24
,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74
,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99])
    
    value=float(input("Enter the value you want to compare "))
    
    L=[]
    
    for i in range(len(vect)):
        if(value<=vect[i]):
            L.append(vect[i]-value)
        else:
            L.append(value-vect[i])
    Array=np.array(L)
    print(vect[Array.argmin()])
    
    
    

                
