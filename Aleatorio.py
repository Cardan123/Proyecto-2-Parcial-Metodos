import math
from random import *

#Clase Aleatorio
class Aleatorio:
    puntos = []
    limites = []
    error = 0
    numeroRestricciones = 0
    aleatorios = []
    restriccion = []
    
#Inicializacion
    def __init__(self,puntos,limites,numeroRestricciones):
        self.puntos = puntos
        self.limites = limites
        self.numeroRestricciones = numeroRestricciones

#Funcion Objetivo Dependiendo del numero de restricciones
    def FO(self,x=None,y=None):
        FO = 0

        for i in range(self.numeroRestricciones):
            FO += ((x-self.puntos[i][0])**2+(y-self.puntos[i][1])**2-self.puntos[i][2]**2)**2

        return FO
         
#Se calculan las restricciones y se guardan sus valores en una lista
    def restricciones(self,x=None,y=None):
        for i in range(self.numeroRestricciones):
            r = (x-self.puntos[i][0])**2+(y-self.puntos[i][1])**2-self.puntos[i][2]**2
            self.restriccion.append(r)

#Se borra las restricciones de la lista de valroes
    def restriccionesv(self):
        for i in range(self.numeroRestricciones):
            self.restriccion.pop()
#Se comprueba que x y y cumplan con las restricciones
    def comprobacion(self,i):
        c = 0
        self.error = (self.FO(0,0)**(1/2)/self.numeroRestricciones)*0.05   
        self.restricciones(self.aleatorios[i][0],self.aleatorios[i][1])
        for i in range(self.numeroRestricciones):
            if self.restriccion[i] <= self.error:
                c = 1
            else:
                self.restriccionesv()
                return 0
        self.restriccionesv()
        return c

#Genera Numeros aleatorios
    def aleatorio(self):
        x = float(uniform(self.limites[0][0],self.limites[0][1]))
        y = float(uniform(self.limites[1][0],self.limites[1][1]))
        self.aleatorios.append([x,y])


#Se itera hasta encontrar la solucion   
    def iterar(self,iteraciones):
        posiciones = []
        z = []

        for i in range(iteraciones):    
            self.aleatorio()
            if self.comprobacion(i) == 1:
                posiciones.append(i)
            
        for i in posiciones:
            z.append(self.FO(self.aleatorios[i][0],self.aleatorios[i][1]))

        
        dic = dict(zip(z,posiciones))

        print("Solucion : x = {} y = {}".format(self.aleatorios[dic[min(z)]][0],self.aleatorios[dic[min(z)]][1]))   
        return self.aleatorios[dic[min(z)]][0],self.aleatorios[dic[min(z)]][1]