import numpy as np
A=np.arange(1,101).reshape(10,10)
asqrd=A**2
div=asqrd[asqrd%3==0]
print("Matrix A")
print(asqrd)
print("Elements divisble by 3")
print(div)
np.save('div_by_3', div)