'''
Print Minimum, Maximum and average Random Numbers  in python 
'''
import numpy as np
import random
N=20
Num=np.array([0 for i in range(N)])
for i in range(N):
    Num[i]=random.randrange(1,50)
_Max=max(Num)
_Min=min(Num)
_Sum=sum(Num)
_len=len(Num)
average=_Sum/_len
print("Maximum value is ",_Max)
print("Minimum value is ",_Min)
print("Average value is ",average)