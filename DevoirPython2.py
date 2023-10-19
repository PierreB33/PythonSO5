import numpy as np
import matplotlib.pyplot as plt

def S10_6():
    numberdots=int(input("Enter the number of dots to draw "))
    startvalue=int(input("Enter the start value "))
    endvalue=int(input("Enter the end value "))
    x=np.linspace(startvalue,endvalue,numberdots)
    s=float(input("Enter the width (s) "))
    x0=int(input("Enter the center of the gaussian (x0) "))
    y=1/np.sqrt(2*np.pi)*np.exp((-1/2)*(x-x0)**2/s**2)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x,y,label="Gaussienne")
    plt.legend()
    plt.show()
    
def S10_7():
       
    x=np.linspace(0,4,100)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    y=np.exp(-x)
    plt.plot(x,y,label="sin")
    y2=np.sin(3*np.pix)*np.exp(-x)
    plt.plot(x,y2,label="exp")
    plt.legend()
    plt.show()
    
def S10_10():
    
    nbcourbes=int(input("Enter the number of functions you want to draw "))
    for i in range (0,nbcourbes):
        numberdots=int(input("Enter the number of dots to draw "))
        startvalue=int(input("Enter the start value "))
        endvalue=int(input("Enter the end value "))
        x=np.linspace(startvalue,endvalue,numberdots)
        s=float(input("Enter the width (s) "))
        x0=int(input("Enter the center of the gaussian (x0) "))
        y=1/np.sqrt(2*np.pi)*np.exp((-1/2)*(x-x0)**2/s**2)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Gaussian function")
        plt.plot(x,y,label="x0="+str(x0)+",s="+str(s))
        plt.legend()
        
    plt.savefig("guassianes.png")
    plt.show()