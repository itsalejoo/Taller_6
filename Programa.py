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