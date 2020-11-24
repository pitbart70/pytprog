n = input("Vvedite chislo \n")
i=0
k=1
while i<len(n)-1:
    if(n[i]>n[k]):
        max=n[i]
    else:
        max=n[k]
    i+=1
    k+=1
print(max)