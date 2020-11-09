# Gustavo de Leon
# Andres Urizar
import numpy as np
import random

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
    print(probabilidad)


pob = poblacionInicial1(10, 0,30)
respuestas, z,x,c = calcularFitness1(pob)
print(pob)
print(respuestas)
seleccion(pob,respuestas)
