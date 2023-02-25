l1 = [9,9,9,9,9,9,9]
l2=[9,9,9,9]

#print(len(l1))
#print(len(l2))

maxlen = len(l2)
maxlist = l2
minlist = l1

if (len(l1) > len(l2) ) :
    maxlen = len(l1)
    maxlist = l1
    minlist = l2

num = 0
rem =0 
newlist = list()
i = 0
SL= 0
for LL in maxlist :
    if (i < len(minlist)) :
        SL = minlist[i]

    num = LL + SL + rem
    
    if( num > 9) :
        rem = int(num/10)
        num = num%10
    
    newlist.append(num)    
    i = i + 1
    SL = 0

if ( rem > 0) :
    newlist.append(rem)
print(newlist)
            


      