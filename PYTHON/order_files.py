import os
def rename_files():
    path=input("ENTER THE PATH: ")
    file_list=os.listdir(str(path))
    i=len(file_list)
    j=0
    working=os.getcwd()
    os.chdir(str(path))
    while(j<i):
        name=input("ENTER FILE: ")
        length=len(name)
        name1=""
        k=0
        while(k<length):
            if(k>len(path)):
                name1=name1+name[k]
            k=k+1
        os.rename(name1,str(j+1)+name1)
        j=j+1
    os.chdir(working)
rename_files()
