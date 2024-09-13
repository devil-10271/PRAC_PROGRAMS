with open('50.txt','r') as nf:
    while True:
        
        print(nf.readline())

        if not nf.readline():
            print(nf.readline())
            break