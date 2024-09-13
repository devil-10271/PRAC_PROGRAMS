import os
import pathlib


def fun(path):
    path=path.replace('\\','/')
    path=path+'/'
    path_che=os.path.exists(path)
    
    print(path)
    if(True == path_che):
       # print('path is exist')
        pass
    else:
        print('path is not exist')
        return 

    files=os.listdir(path)
    oldpath=path
    new_files=list()
    for i in files:
        if i.endswith('.txt'):
            new_files.append(i)



    for i,file in enumerate(new_files,start=1):
        path=oldpath
        path+=file
        if(path.endswith('.txt')):
            newpath=oldpath+str(i)+'.txt'
            os.rename(path,newpath)
        
            



if __name__ == "__main__":
    a=input("Enter the path of the file : ")
    fun(a)
