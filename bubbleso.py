'''def sorting2(n,ar):#print in descending order
    for j in range(n):
        for i in range(0,n-j-1): 
            if ar[i]<ar[i+1]:         
                ar[i],ar[i+1]=ar[i+1],ar[i]'''
from array import *
ar= array('i',[42,23,74,11,65,58,94,36,99,87])   
n=len(ar)
      
def sorting1(n,ar): 
    for j in range(n): #print in ascending order
        for i in range(n-j-1): 
            if ar[i]>ar[i+1]:        
                ar[i],ar[i+1]=ar[i+1],ar[i]
                print(j,ar)        
               
sorting1(n,ar)