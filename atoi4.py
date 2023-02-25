
from re import X


s="  -42"
print(s)

x=s.split()

num = 0
neg=False
for s1 in x :
    s1=s1.strip()
    print(s1)
    if(s1.find("-") != -1) :
        neg = True
        s1=s1.replace("-","0")
        print(s1)
    elif(s1.find("+") != -1):
        neg = False
        s1=s1.replace("+","0")
    if(s1.isnumeric()) :
       num = int(s1,10)
    else:
        temp=""
        org=""
        print("####")
        for i in range(0,len(s1)) :
            org+=s1[i:i+1]
            print("#####",org)
            if(org.isnumeric()):
               temp=org 
            else:
                break
        print("+++++",temp)    
        if(temp.isnumeric()):
           num = int(temp,10) 
         
    if(neg):
       num = -num

print(num)

