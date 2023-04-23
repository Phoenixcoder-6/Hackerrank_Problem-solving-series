import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p,q,r=0,0,0
    for i in range(0,len(arr)):
        if arr[i]>0:
            p=p+1
        elif arr[i]<0:
            q=q+1
        else:
            r=r+1
            
    print(p/len(arr))
    print(q/len(arr))
    print(r/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
