def fimo(n):
    fimolis=[0,1]
    # a=len(fimolis)
    for i in range(2,n+1):
        fimolis.append(fimolis[i-1]+fimolis[i-2])
    print(fimolis[n])
    print(fimolis)
    


n=int(input("the number : "))        
fimo(n)