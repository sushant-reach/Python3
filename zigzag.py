s="PAYPALISHIRING"
row=3
col=len(s)
arr = [[0 for i in range(col)] for j in range(row)]
temp=""
i=0
j=0
k=0
for i in range(0,col):
    for j in range(0,row):
        arr[j][i]= " "
        sum= i+ j
        if((i%(row-1)==0) or (sum%(row-1)==0)):
            print(i,"--->",j,"====", s[k:k+1] )
            arr[j][i]=s[k:k+1] 
            k=k+1
        else:
            print(i,"--->",j,"====")    

print(arr) 
temp=""
for i in range(0,row):
    for ch in arr[i]:
        temp+=ch
        
temp=temp.strip(" ")
print(temp)


fin=str("")

for ch in temp:
    if(ch.isspace()==False):
      fin+=ch

print(fin)      





        
         










                






