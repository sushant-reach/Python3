         
         

x = 121
num = 0

if(x < 0): 
    num = 0 
y=x   

count=0   
count=len(str(x))

print(".............",count)
              

while(count>0):
    rem = x%10   
    num = num + rem*pow(10,count-1)   
    x=int(x/10)
    count = count -1

print(num)     
print(count)    
