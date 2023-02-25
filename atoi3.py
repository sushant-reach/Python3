import math
import numpy as np

i=int(1)
j=int(1)
k=0
nums1 = [1,3] 
nums2 = [4,5]
fin= []
total = len(nums1) + len(nums2) + 1
print("---", total)
while (i+j) <= total : 
    k=k+1
    if(nums1[i-1:i] and nums2[j-1:j]) :
        if (nums1[i-1:i] > nums2[j-1:j] ): 
           print("---",nums2[j-1:j])
           fin.append(nums2[j-1:j])
           j+=1
        else :  
           print("++++",nums1[i-1:i])
           fin.append(nums1[i-1:i])
           i+=1
    else :
        if (nums2[j-1:j]) :
            fin.append(nums2[j-1:j])
            j+=1
        if(nums1[i-1:i]) :
            fin.append(nums1[i-1:i])
            i+=1     
    print("Iternation = ", k, i , j,"=====",fin)    
print(i,j)

print(fin) 

mysize=len(fin)

print("-----------",len(fin))

print("=========",mysize%2)

if (int(mysize%2) == 1) :
    mysize=mysize/2
    mysize=math.floor(mysize)
    print(fin[mysize:mysize+1])
    myvalue = int(fin[mysize:mysize+1])
else:
    i=int(mysize/2)
    array1 = np.asarray(fin[i-1:i])
    array2 = np.asarray(fin[i:i+1])         
    avg = (array1 + array2) / 2
    print(avg)
    myvalue = float(avg)

print(myvalue)    





     
     

