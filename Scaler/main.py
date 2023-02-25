A = [88, 2, 46, 66,89, -79, 36, 72, 30, 60, 89, 23, 60, 26, -43, -14, 20, 92, -48, 45, 84, -22, 65, -57, 7]
sum = 0
for i in range (0 ,len(A)):
   sum = sum - A[i]
   if sum in A:
      print("**1")
   else:
         j = i+1
         rem = sum - A[j]
         print(rem)
         if rem in A:
            print("==1")


print("0")





