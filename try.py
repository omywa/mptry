import numpy as np
import math

# generate random vectors,using array
RN = 10
row = int(raw_input("Total number of points:"))
col = int(raw_input("Demension of each vectors:"))
rawvec=np.zeros((row,col),dtype = int)
for i in range(row):
    rawvec[i]= np.random.randint(RN,size=col)
    print rawvec[i]
print "\n"

# calculate L2 distances

dist=np.zeros((row,row),dtype = float)
for i in range(row):
    for j in range(row):            
            L1dist = rawvec[j]-rawvec[i]
            # print L1dist
            dist[j][i]=dist[i][j]= math.sqrt(sum([elem**2 for elem in L1dist]))
            # print dist[j][i]

print dist # matrix :store distance between two points
print "\n"

# hash functions H. Each h in H has independent a and b

# generate ai of N(0,1) Gaussian distribution
mu,sigma = 0, 1
a = np.random.normal(mu, sigma, col)

# generate bi of U[0, W) uniform distribution.W=??
low,high = 0, W
b = np.random.normal(low, high, col)
