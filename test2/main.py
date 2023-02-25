n=[_+1 for _ in range(100)]
i=1

while len(n)>1:
    print(n)
    if(i>=len(n)):
        i%=len(n)
    n.pop(i)
    i+=1

print(n)