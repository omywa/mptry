import numpy as np

# generate random n-dim(col) vector
row = int(raw_input("Total number of points:"))
col = int(raw_input("Demension of each vectors:"))
a=[[0 for r in range(row)]for c in range(col)]
for i in range(5):
    a[i]= np.random.random_integers(100,size=8)
    print a[i]

#calculate L2 distances
