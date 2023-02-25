def solve(A):
    l = len(A)
    mid = int(l/2)
    j = l -1
    max = 1
    for i in range(0, mid+1) :
        for j in range(mid,len(A)):
            print(f"i = {i} and j = {j}")
            print(f"max ={max}")
            if  i != j :
                if max < A[i]%A[j] :git 
                   max = A[i]%A[j]
                   print(f"==>A[i]={A[i]} and A[j] = {A[i]}")
                if max < A[j]%A[i]:
                   max = A[j]%A[i]
                   print(f"<==A[i]={A[i]} and A[j] = {A[i]}")
    return max

#A = [1, 2, 44, 3]
A = [2, 6, 4, 7, 8]
print(solve(A))
