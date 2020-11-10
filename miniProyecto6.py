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
    temp_resp = resp.copy()
    temp_resp.sort(reverse=True)
    temp_resp0 = temp_resp[0]
    temp_resp1 = temp_resp[1]
    print("temp_resp0 ",temp_resp0)
    # for i in pob:
    #     prob = resp[pob.index(i)]/sum(resp)
    #     probabilidad.append(prob)
    # elegido = random.choices(pob, probabilidad)
    indice_selec = resp.index(temp_resp0)
    indice_selec2 = resp.index(temp_resp1)
    primerselec = pob[indice_selec]
    primerselec2 = pob[indice_selec2]
    elegido = [primerselec,primerselec2]
    # primerprob = probabilidad.pop(indice_selec)
    # elegido2 = random.choices(pob,probabilidad)
    # pob.insert(indice_selec,primerselec)
    # probabilidad.insert(indice_selec,primerprob)
    # # print("Pareja elegida:",elegido[0])
    # print("Probabilidad de eleccion:",probabilidad[indice_selec])
    # print("Pareja elegida 2:",elegido2[0])
    # print("Probabilidad de eleccion:",probabilidad[pob.index(elegido2[0])])
    print("Elegido",elegido)
    return elegido[0],elegido[1]
    
cont = 0
pob = poblacionInicial1(30, 0,30)
maximo = 0

# print("Poblacion inicial ",pob)
# respuesta, val_max, x, c = calcularFitness1(pob)
# res_1, res_2 = seleccion(pob,respuesta)
# print("Respuesta ",respuesta)
# print("Valor max ",val_max)
# print("x ",x)
# print("c ",c)
# print("Res1 ",res_1)
# print("Res2 ",res_2)

while cont != 100:
   
    respuestas, valor_max,x,c = calcularFitness1(pob)

    if valor_max > maximo:
        maximo = valor_max
    elif valor_max == maximo:
        cont += 1
    
    print("Contador",cont)
    
    pareja1,pareja2 = seleccion(pob,respuestas)
    progenitores =  np.concatenate((pareja1,pareja2))

    descendencia = combinations(progenitores,2)
    descendencia = list(descendencia)

    print("Descendencia",descendencia)
    desctemp = []
    pob = []

    for x in descendencia:
        temp = [x[0],x[1]]
        desctemp.append(temp)

    descendencia = desctemp
    print("Descendencia",descendencia)

    pob.append(pareja1)
    pob.append(pareja2)

    for hijo in descendencia:
        prob_mutacion = random.uniform(0,1)
        valor_indice = random.randint(0,1)

        print("Descendencia antes",pob)

        if prob_mutacion <= 0.8:
            hijo[valor_indice] += 1
        #x1+2 x2 <=
        if (hijo[0]+(2*hijo[1])) <= 30:
            pob.append(hijo)

        print("Descendencia despues",pob)

    # pob = descendencia
res_final, val_max_final, x_final, c_final = calcularFitness1(descendencia)

final = []
for x in descendencia:
    if(x[0]+(2*x[1])<=30):
        final.append(x)

print("Final ",final)

res_final, val_max_final, x_final, c_final = calcularFitness1(final)

indice_final = res_final.index(val_max_final)

print("Resultado final: ",final[indice_final])
# print("Respuesta ",res_final)
# print("Valor max ",val_max_final)
# print("x ",x_final)
# print("c ",c_final)

# print("Primer resultado de la poblacion",final)


