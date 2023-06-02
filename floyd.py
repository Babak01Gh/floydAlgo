import numpy

infinit = float('inf')
weighted = numpy.array([
    [0,1,8,infinit],
    [3,0,infinit,5],
    [2,4,0,7],
    [infinit,infinit,6,0]
])
dim = len(weighted)
R = numpy.zeros((dim,dim) , dtype=int)
# A[i][j](k) = min(A[i][j](k-1) , A[i][k](k-1) + A[k][j](k-1))

def floyd(weighted):
    for k in range(1, dim+1):
        for i in range(dim):
            for j in range(dim):
                if weighted[i][j]>weighted[i][k-1] + weighted[k-1][j]:
                    weighted[i][j] = weighted[i][k-1] + weighted[k-1][j]
                    R[i][j] = k
          
floyd(weighted)
print(weighted)
print(R)