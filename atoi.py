num1=1534236469
num2=0
num3=num1
i=0
while(num3):
    num3=int(num3/10)
    i = i + 1
    print("====",num3)
print(num3,"----",i)

while(i>0):
    rem=num1%10
    num1=int(num1/10)
    num2=num2 + rem*pow(10,i-1)
    i=i-1
print("========",num2)

