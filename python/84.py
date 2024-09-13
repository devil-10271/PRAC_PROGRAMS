import time

def foreach():
    for i in range(100):
        print(i)

def whilelo():
    i=0
    while(i<100):
        print(i)
        i+=1


# a=time.time()
# foreach()
# timefor=time.time()-a
# print(timefor)
# a=time.time()
# whilelo()
# timewhile=time.time()-a
# print(timefor,timewhile)

#time.sleep(12)

print(time.localtime())
formated=time.strftime("%Y : %m : %d %H : %M : %S",time.localtime())
print(formated)