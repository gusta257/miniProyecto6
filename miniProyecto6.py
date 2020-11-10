# Gustavo de Leon
# Andres Urizar
import numpy as np
import random
from itertools import combinations

def poblacionInicial1(n, limiteI, limiteS):
    poblacion = []
    while(len(poblacion) < n):
        genX1 = random.randint(limiteI, limiteS)
        genX2 = random.randint(limiteI, limiteS)
        cond = genX1 + 2*genX2
        if(cond <= 30):
            poblacion.append([genX1,genX2])
    return poblacion
    
def funcionFitness1(x1, x2):
    return 15*x1 + 30*x2 + 4*x1*x2 - 2*x1**2 - 4*x2**2


def calcularFitness1(poblacion):
    respuestas = []
    for i in poblacion:
        funcionF = funcionFitness1(i[0],i[1])
        #print("Individuo: (", i[0],",",i[1],")")
        #print("Fitness:",funcionF)
        respuestas.append(funcionF)
    best = np.max(respuestas)
    indexBest = respuestas.index(best)
    solBest = poblacion[indexBest]
    print("Mejor respuesta:", best)
    print("Index de Mejor: ", indexBest)
    print("Mejor solucion: ", solBest)
    return respuestas, best, indexBest, solBest
        
def seleccion(pob, resp):
    probabilidad = []
    for i in pob:
        prob = resp[pob.index(i)]/sum(resp)
        probabilidad.append(prob)
    elegido = random.choices(pob, probabilidad)
    indice_selec = pob.index(elegido[0])
    primerselec = pob.pop(indice_selec)
    primerprob = probabilidad.pop(indice_selec)
    elegido2 = random.choices(pob,probabilidad)
    pob.insert(indice_selec,primerselec)
    probabilidad.insert(indice_selec,primerprob)
    # print("Pareja elegida:",elegido[0])
    # print("Probabilidad de eleccion:",probabilidad[indice_selec])
    # print("Pareja elegida 2:",elegido2[0])
    # print("Probabilidad de eleccion:",probabilidad[pob.index(elegido2[0])])
    return elegido[0],elegido2[0]
    
cont = 0
pob = poblacionInicial1(100, 0,30)

while cont <= 1000:
   
    respuestas, z,x,c = calcularFitness1(pob)

    print(respuestas)
    pareja1,pareja2 = seleccion(pob,respuestas)
    progenitores =  np.concatenate((pareja1,pareja2))

    descendencia = combinations(progenitores,2)
    descendencia = list(descendencia)

    print("Descendencia",descendencia)
    desctemp = []

    for x in descendencia:
        temp = [x[0],x[1]]
        desctemp.append(temp)

    descendencia = desctemp
    print("Descendencia",descendencia)

    for hijo in descendencia:
        prob_mutacion = random.uniform(0,1)
        valor_indice = random.randint(0,len(descendencia)-1)

        print("Descendencia antes",descendencia)

        if prob_mutacion <= 0.1:
            descendencia[valor_indice][0] += 1
            descendencia[valor_indice][1] += 1

        print("Descendencia despues",descendencia)

    pob = descendencia
    

    cont+=1

print("Primer resultado de la poblacion",descendencia)


