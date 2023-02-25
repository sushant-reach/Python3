from xmlrpc.client import boolean

def IsPalandrome(s:str) -> boolean :
    l= len(s)
    temp1=""
    temp2=""
    h=int(l/2)
    temp1=s[0:h]
    if(l%2 != 0) :
       h=h+1 
    temp2=s[h:l]
    print("===>",temp1)
    print(temp2,"<===")
    temp2=temp2[::-1]

    if (temp1 == temp2) :
            status = True
    else :
            status = False
    return status

s="aba"
temp=""
org=""
s1=""
k=0
l=len(s)
if(IsPalandrome(s)):
    print(s)
    org=s
else:
    for j in range(k,l):
        s1=""
        s1=s[k:l]
        k=k+1
        for i in range(0,len(s1)):
            temp+=s1[i:i+1]
            print("====",temp)
            if(IsPalandrome(temp)) :
                if(len(org) <= len(temp)):
                    org= temp
        temp=""
print("Largest substring", org)
     




