import numpy as np

# Second Addition 
def vecadd2D(v1,v2):
     a = v1[0] + v2[0]
     b = v1[1] + v2[1]
     return [int(a),int(b)]
def vecadd3D(v1,v2):
     a = v1[0] + v2[0]
     b = v1[1] + v2[1]
     c = v1[2] + v2[2]
     return [int(a),int(b),int(c)]

def scalevec(v,s): # Returns Scale Value
    return s*v # Formula for Scalar * Vector

def vecmult2D(v1,v2): # Quick Addition of 2D dot productw
    return v1[0]*v2[0] + v1[1]*v2[1]

def vecmult3D(v1,v2): # Returns Dot Product
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2] #Formula For Dot Product

# print (scalevec(np.array([1,2,3]),2)) #Test Output
# print (vecmult3D(np.array([1,2,3]),np.array([1,2,3]))) #Test Output
# print (vecmult3D(np.array([1,2]),np.array([1,2])))

# print (vecadd2D(np.array([1,2]),np.array([1,2])))
# print (vecadd3D(np.array([1,2,3]),np.array([1,2,3])))
#Next Steps: Learn the Cross Product and remake it into here, and add any other miscellaneous vector functions like addition
