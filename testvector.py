import numpy as np

# Addizione
u = np.array([1,2])
v = np.array([3,1])
z = u+v

print(z)

# Moltiplicazione
y = np.array([1,2])
x=2*y
print(x)

w=u*v
print(w)

# Somma di a1*a2+b1*b2
a = np.dot(u,v)
print(a)

# Aggiungi 1 a tutto l'array
u=np.array([1,2,3,-1])
z=u+1
print(z)

# Calcolo media
b=np.array([1,-1,1,-1])
mean_b=b.mean()
print(mean_b)

# Trovare il maggiore
b = np.array([1,-2,3,4,5])
max_b=b.max()
print(max_b)

#Pi Greco
x=np.array([0,np.pi/2,np.pi])
print(x)
#Seno (applicato a tutto il vettore)
y=np.sin(x)
print(y)

#Linespace
print(np.linspace(-2,2,num=9))