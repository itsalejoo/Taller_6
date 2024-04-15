#taller Numpy
#numpy Biblioteca para realizar calculos en arreglos  N-DIMENSIIONALES
import numpy as np 

#crear un ndarray de 2 dimensiones apartir de una lista

A=np.array([[1,5],[7,9]])
B=np.array([[2,0],[1,3]])

#producto punto entre nparray
C=np.dot(A,B)
print (C)

#Solucion de un sistema de ecuaciones con numpy 
m_solucion=np.array([5,17])
m=np.linalg.solve(A,m_solucion)
print(m)
#matplotlib biblioteca de Python para realizar graficos cientificos.
#tiene muchos módulos : subcarpeta, que se deben importar uno a uno 
#pyplot para hacer dibujos y graficar
import numpy as np
import matplotlib.pyplot as plt 
#dibujar una funcion seno 
#crear un ndarray de 1 dimensión, 100 elementos equispaciados, desde 0 a 2*PI

x=np.linspace(0, 2*np.pi, 100)
y=np.sin(x)
#usar matplotlib 
plt.figure(figsize=(8,4))
plt.title("mi primer grafica cientifico en programación")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("seno de x")
plt.grid(True)
plt.show() 