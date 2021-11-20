import numpy as np
phone = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],int)
d1 = np.where(phone==7)

print(abs(d1[0][0]-3+d1[1][0]-1))