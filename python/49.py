# f=open('test.txt','w')
# f.write("hello world")
# f.close()


with open('test.txt','a') as a :
    a.write('\nhello world')