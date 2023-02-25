def findit(mainstr,findsubstr,mylen, start, end) :
    print("In fun ====",findsubstr,"====")
    mytemp1 =""
    mytemp2=""
    mylen = len(findsubstr) 
    mytemp1+=findsubstr[mylen-1:mylen]
    print("Substring select", mytemp1,"===")
    print(findsubstr.find(mytemp1))

    if (findsubstr.count(mytemp1) == 2):
       return  mainstr.find(mytemp1, start, end) 
    return -1
  
str = "nfpdmpi"
i = 0
j = 0
orglen = len(str) + 1
temp=""
maxlength = 0
if (str == " ") :
    maxlength = 1
for i in range (1,orglen) :
        temp=str[j:i]

        if(findit(str,temp,i,j,orglen) > -1) :
            orgstr=str[j:i-1]
            j = findit(str,temp,i, j,orglen) + 1
            print("------",j)
            print("Org string " ,orgstr,"===",len(orgstr) )
            print("---------",maxlength)
            if(maxlength <= len(orgstr)): 
               maxlength = len(orgstr)
        else : 
            if (maxlength <= len(temp)) :
                maxlength = len(temp)



    
print("========",maxlength,"=========")        
    