
import numpy as np


m1 =([3,2,1],
     [4,5,6],
     [9,7,8]
     )

# 3*1 + 2*9 + 1*4
# #3+18+4
# 25
m2 =([1,2,3],
     [9,5,5],
     [4,7,8]
     )
result1 = np.add(m1 , m2)
result2 = np.subtract(m1 , m2)
result3 = np.dot(m1 , m2)
print(result1)
print(result2)
print(result3)