from miniProyecto6 import * 
from miniProyecto62 import * 
from miniProyecto63 import * 


resp = 0
while(resp != 4):
    print("1: 15*x1 + 30*x2 + 4*x1*x2 - 2*x1^2 - 4*x2^2")
    print("2: 3*x1+5*x2")
    print("3: 5*x1 - x1^2 + 8*x2 - 2*x2^2 ")
    print("4: SALIR")
    resp = int(input("Que funcion desea maximizar?: "))
    if(resp == 1):
        print("-"*50)
        pob = poblacionInicial1(12000, 0,15)
        ejecucion1(pob)
        print("-"*50)
    elif(resp == 2):
        print("-"*50)
        pob = poblacionInicial2(3000, 0,10)
        ejecucion2(pob)
        print("-"*50)
    elif(resp == 3):
        print("-"*50)
        pob = poblacionInicial3(5000, 0,10)
        ejecucion3(pob)
        print("-"*50)
        

    