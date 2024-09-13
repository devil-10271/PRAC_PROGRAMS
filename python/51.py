with open('51.txt','w+')as fo:
    fo.write('hello worla ')
    fo.seek(0) # you remove this you can't print any item 
    print(fo.read())
    print(fo.tell())
    fo.seek(0) # strt from
    print(fo.tell())

    fo.truncate(5)
    print(fo.read())