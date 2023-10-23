# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:56:11 2023

@author: pbria
"""
import math as m 
import numpy as np
import matplotlib.pyplot as plt 

print ("Goodbye, cruel world!")

type("Goodbye, cruel world!")

num1=3
num2=2

add=num1+num2
print (add)

sus=num1-num2
print(sus)

div=num1/num2
print (div)

mult=num1*num2
print (mult)

exp=num1**num2
print (exp)

num3=3.2
num4=4.14
type(num3)
num3=str(num3)
num4=str(num4)
type(num3)
print(num3+num4)

print("café\ncoffee\nKaffe\ncaffé")

def exo3 () :
    num=input("How much ?")
    num=float(num)
    print(2.5+num)
    
def exo4 () :
    num1=223/71
    num2=(1+1/10)**10
    num3=(1+1/100)**100
    num4=(1+1/1000)**1000
    num1=str(num1)
    num2=str(num2)
    num3=str(num3)
    num4=str(num4)
    
    
    print(num1+ "\n"+ num2 +"\n" +num3 +"\n"+ num4)
    
def exo5 () :
    if 'aog'>'cat' :
        return True
    else : return False 
    
    #ilovebro : TD2

T=5
P=2
print("The temperature is {} and the pressure {}".format(T,P)) 

def complex(a,b):
    c=complex(a,b)
    print(c)
    
def GP(V,n,R,T):
    R=0.08206
    n=float(input ("What is the number of moles ?"))
    V=float(input("What is the volume ?"))
    T=float (input ("What is the temperature ?"))
    P=n*R*T/V
    print ("The pressure of the gaz is {}".format(P))
    
    
def volume(r,h):
    r=float(input("Entrez le rayon "))
    h=float(input("Entrez la hauteur"))
    V=float(1/3*3.14*r**2*h)
    print(V)
    
def conversionCtoK():
    C=float(input("Entrez la temperature en Celsius"))
    K=C+273.15
    print("La temperature en Kelvin est {}".format(K))
    
def ticket():
    banknote10=float(input("Enter the number of banknote 10euros"))
    banknote20=float(input("Enter the number of banknote 20euros"))
    banknote50=float(input("Enter the number of banknote 50euros"))
    
    
def circle():
    radius=float(input("Entrez le rayon du cercle"))
    perimeter=2*m.pi*radius
    area=m.pi*radius**2
    print("Le perimetre du cerlcle est {} et son aire est {}".format(perimeter,area))
    
    
def Lengthsidetriangle():
    a=float(input("Entrez la longueur du premier coté"))
    b=float(input("Entrez la longueur du deuxieme coté"))
    angle=float(input("Entrez la valeur de l'angle entre les deux cotés en degrés"))
    c=m.sqrt(a**2+b**2-2*a*b*m.cos(angle))
    print("Le troisième coté mesure {}".format(angle))
    
    
     #ilovebro : TD3
     
def liste():
    
    liste1=[2,9,0,19,8]     
    liste2="bonjour Mit Patel"
    
    print(liste1[0])
    print(liste2[0]+liste2[9:11]+liste2[15])
    
    print(len(liste1)) #longueur de la liste
    print(liste2.upper()) #maj
    print(liste2.lower()) #min
    print(liste2.count('a')) #compte le nombre de char
    
    
    

def BMI():
    poids=input("Enter your bodyweight in kilos ")
    taille=input("Enter your height in meters ")
    poids=float(poids)
    taille=float(taille)
    
    BMI=poids/(taille**2)

    if BMI<18:
        print("You are underweight")
    elif BMI>25:
        print("You are overweigth")
    elif BMI>30:
        print("You are obese")
    else :
        print("You have a normal weight")
        
    BMI=str(BMI)
    print("Your BMI is "+BMI)


def Divisiblenaturalnumber():
    
    nat1=input("Enter the first natural number")
    nat2=input("Enter the second natural number")
    
    if nat1%nat2==0:
        resul=nat1/nat2
        resul=str(resul)
        print(resul)
        
def bill():
    
    unit=int(input("Enter the number of units"))
    prix=0
    
    if unit<100:
        print("No charge")
    elif unit<=200:
        prix=prix+(unit-100)*5
    elif unit>200:
        prix=prix+500+(unit-200)*10
        
        prix=str(prix)
        print(prix)
        
def sum22():
    
    for i in range (0,10):
        for j in range(0,10):
            for k in range (0,10):
                if i+j+k==22:
                    print("{}{}{}".format(i,j,k))
                    
def cube():
    for i in range (0,10):
        for j in range(0,10):
            for k in range (0,10):
                if i**3+j**3+k**3==(i*100+j*10+k):
                    print("{}{}{}".format(i,j,k),end="")
                    
def prime():
    
    num=int(input("Entrez un nombre "))
    a=0
    for i in range(1,num):
        if num%i==0:
            a=a+1
    if a!=1:
        return True
    else:
        return False

def fibo():
    salo=int(input("Entrez le terme de la suite que vous voulez "))
    num1=0
    num2=1
    memoire=0
    for i in range (1,salo):
        memoire=num2
        num2=num1+num2
        num1=memoire
        print(num2)
        
def mito():
    a=[1,3,5,7,11]
    b=[13,17]
    c=a+b
    print("First instruction print: ()".format(c))
    b[0]=-1
    d=[]
    for e in a:
        d.append(e+1)
    print("Second instruction print: ()".format(d))
    d.append(b[0]+1)
    d.append(b[-1]+1)
    print("Third instruction print: ()".format(d))
    print("Fourth instruction print : {} ".format(d[-2:]))
    print("Fifth instruction print : {} ".format(d[:-1]))
    print("Sixth instruction print : {} ".format(d[1:4]))
            
def squarelist():
        n=input("Entrez un entier naturel")  
        liste=[]        
        for e in n:
            liste.append(e**2)
        print(liste)
        
def Vendredi15Septembre():
    
    liste=[]
    liste2=[]
    while True:
        i = input("Enter name (or Enter to quit): ")
        if not i:
            break
        else:
            liste.append(i)

        j = int(input("Enter grade (or Enter to quit): "))
        if not j:
            break
        else: 
            liste2.append(j)
    print(liste)    
    print(liste2)  
    moy = sum(liste2)/len(liste2)
    print(moy)
    
    
def dico1():
    
    country_capitals={
        "United States" : "Washington D.C",
        "Italy" : "Rome",
        "England" : "London",
        "Culottes" : "Rouges"
        }
    print(country_capitals["United States"])
    print(country_capitals["England"])
    print(country_capitals["Culottes"])
    
def convertlisttodico():
    keys=['Ten','Twenty','Thirty']
    values=[10,20,30]
    dico=dict(zip(keys,values))
    print(dico)


def PythonProblem():
    
    names=[]
    grades=[]
    while True:
        name = input("Enter name (or Enter to quit): ")
        if not name:
            break
        else:
            names.append(name)

        grade = int(input("Enter grade (or Enter to quit): "))
        if not grade:
            break
        else: 
            grades.append(grade)
            
    print ("{:14} {:5}".format("Name", "Grade"))
    for name, grade in zip(names, grades):
        print ("{:14} {:5.1f}".format(name, grade))
    
    moy = sum(grades)/len(grades)
    print(moy)
            
elements = {
        'H': {'boiling_point': 20, 'melting_point': 14},
        'He': {'boiling_point': 4, 'melting_point': 1},
        'Bi': {'boiling_point': 1603, 'melting_point': 453},
        'Be': {'boiling_point': 2742, 'melting_point': 1560},
        'B': {'boiling_point': 4200, 'melting_point': 2349},
        'C': {'boiling_point': 3915, 'melting_point': 3915},
        'N': {'boiling_point': 77, 'melting_point': 63},
        'O': {'boiling_point': 90, 'melting_point': 54},
        'F': {'boiling_point': 85, 'melting_point': 53},
        'Ne': {'boiling_point': 27, 'melting_point': 25}
                }
print(elements)

def exo2():
    while True:
            ans = input("Donne élément ")
            if ans == "":
                break
            a=0
            while a==0:
                if (ans in elements):
                    a=1
                if a==0:
                    print("mal orthographié ou existe pas")
                    ans = input("Donne élément ")
            temp=int(input("Donne température"))
            if(temp>elements[ans]['boiling_point']):
                print("votre "+ans+" c'est du gaz")
            elif (temp<elements[ans]['boiling_point'] and temp>elements[ans]['melting_point']):
                print("votre "+ans+" c'est du liquide")
            else:
                print("votre "+ans+" c'est du solide")
    
def exolisterank():
    liste=[]
    for i in range(0,5):
        liste.append(int(input("Entrez un nombre ")))
    liste.sort()
    print("The largest among the numbers is"+str(liste[4])+"and the smallest is"+str(liste[0]))
    
    
def oddeven():
    try:
        number=int(input("Entrez un nombre : "))
        
        if number%2==0:
            print("even")
        else:
            print("odd")        
    except ValueError as error:
                print(error)

                
def primenumber():
    number=int(input("Entrez un nombre : "))
    b=0
    try:
        for a in (2,number):
            if number%a==0:
                b=b+1
        if b!=1:
            print("Number isnt prime")
        else:
            print("Number is prime")

    except ValueError as e:
       print("Not ok")
       
      
def vect():
    nel=int(input("Enter the number of element in the vector : "))
    lvec= [] 
    for i in range (nel):
        comp=input("Enter the value of component {} :".format(i))
        lvec.append(float(comp))
    vec=np.array(lvec)
    print(vec)

def vectlist():
    lin=input("Enter the components of a vector in a line : ")
    smooth=lin.split()
    vec=np.float_ (smooth)
    print("List: {}".format(smooth))
    print("Vector: {}".format(vec))
    
def inversevect():
    
    A=np.zeros((2,2))
    B=np.zeros((2,2))
    AB=np.zeros((2,2))

    for i in range (2):
        for j in range (2):
            A[i,j]=float(input("Valeur de [{},{}]".format(i,j)))
            B[i,j]=float(input("Valeur de [{},{}]".format(i,j)))
            
    AB=np.matmul(A,B)
    print (AB)
    
    AB_inv=np.linalg.inv(AB)
    print (AB_inv)
    
    A_inv=np.linalg.inv(A)
    B_inv=np.linalg.inv(B)
    B_invA_inv=np.matmul(B_inv,A_inv)
    
  
    if B_invA_inv==AB_inv:
        print("True")
    else:
        print("False")
        
def inversevect2():
    
    A=np.zeros((2,2))
    B=np.zeros((2,2))
    C=np.zeros((2,2))

    for i in range (2):
        for j in range (2):
            A[i,j]=float(input("Valeur de A[{},{}]".format(i,j)))
            B[i,j]=float(input("Valeur de B[{},{}]".format(i,j)))
        
    A_inv=np.linalg.inv(A)
    B_inv=np.linagl.inv(B)
    
    X=np.matmul(A_inv,C,B_inv)
    
def graphtest():
        
    x=np.linspace(-2,2,101)
    y=x**2
    y2=x**4
    y3=x**3
    print(x)
    plt.xlabel('x') #Nom de l'abscisse
    plt.ylabel('f(x)') #Nom de l'ordonnée
    plt.xlim(-1.5,1.5) #Zoom sur x
    plt.ylim(-0.5,2.5) #Zoom sur y
    plt.title("Chart Title") #Titre du graph
    plt.plot(x,y, label="x^2") #Tracage graph nom graph label
    plt.plot(x,y2, label="x^4") 
    plt.plot(x,y3, 'ro', label="x^3") #'ro': r=rouge et o=gros points
    plt.legend() #Fais apparaitre les legendes (label)
    plt.savefig("fig2.jpg") #Save le graph dans un fichier 
    plt.show()

                    
            
            
        
    

    
 
    
    


