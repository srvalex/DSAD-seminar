from functools import reduce
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time



numere =[]
for each in range(20):
    if each%2==0:
        numere.append(each**2)
# print(numere)

#intr un list comprehension sunt relevante 3 blocuri
# repetitivva: for x in range(20)
# transformare aplicata pe elemente citite (in cazul asta luam elementele ca atare)
# al treilea: filtre aplicate pe elementele citite din fiecare iterartie


numere = [x**2 for x in range(20) if x % 2==0]

# print(numere)

#dict

nume = ["Ana","Andrei","Alina"]

note = [10,9.5,4]
catalog = {k:v for k,v in zip(nume,note)}
print(catalog,type(catalog),catalog.keys(),type(catalog.keys())
      ,catalog.values(),type(catalog.values())
      ,catalog.items(),type(catalog.items())
      )

celsius = [10,-3,0,19,25]
farenheit = [round(c*9/5+32,2) for c in celsius]
# print(celsius,farenheit)



#lambda,map,filter,reduce

secventa = (1,2,3,4,5)
result = map(lambda x: x**3,secventa)
# print(result,type(result),list(result))

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = list((1,2,3,4,5))
l3 = list("ana")
s1 = set("analiza datelor")
s2 = {"analiza datelor"}
# print(l1,l2,l3,s1,s2)


#filter

result = filter(lambda x: x>=0,celsius)
#echivalent cu lambda

print(type(result),list(result))

note = [3,7,4,5,9,10,5,6,]
promovat = [p for p in note if p >=5]
status= ["promovat" if p>=5 else "restant" for p in note]
print(promovat)
print(status)
print(note)


emails = ["john.doe@gmail.com","student@ase.ro","support@google.com"]


valid = filter(lambda e: e.endswith("ase.ro"),emails)

print(list(valid))


# reduce


suma = reduce(lambda a,b: a+b,note)
print(suma)
print(type(suma))
print("media notelor", round(suma/len(note),2))

############################            NUMPY

#spre deosebire de o lista simpla care accepta elemente de tipuri
#un ndarray forteaza un singur tip


#proptietati ale ndarray
a = np.array([1,2,3,4],dtype='int16')
b = np.array([[5.4,3.2],[2.2,7.8]])
print("Numpy arrays: ")
print("a: ",a)
print("b: ",b)

print("Shape:",b.shape)
print("Numar dimensiuni:",b.ndim)
print("Data type: ",b.dtype)
print("Dim unui elem:",b.itemsize)
print("Dim. totala:",b.nbytes)

#indexing & slicing

print("Acces elemente")

c = [1,2,3,4,5]

print(c[0:len(c)])
print(c[len(c)-1])
print(c[0:len(c)+100])
print(c[0:len(c)-1])


#indexing

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("a:\n")
print(a)
print(a[1,2])
print(a[0,1])

#slicing

print(a[0,1:-1]) #linia 0, de la 1 pana la penultimul elemente
print(a[0,1:-1:2])# linia 0, de la 1 pana la penultimul din 2 in 2
print(a[0,:])# linia 0, toate coloanele
print(a[0,::2])# linia 0, toate elementele din 2 in 2
print(a[:-1,3])# ultima linie, elementul 3

#colectii predefintie

print("Zeros: \n",np.zeros((3,3),dtype=int)) #3 liniii 3 coloana
print("Ones: \n",np.ones((2,2),dtype=int)) #2 linii 2 coloane
print("FULL: \n",np.full((3,3),23)) # 3 x 3
print("random integers0\n",np.random.randint(-100,100,size=(3,3))) # 3 x3
