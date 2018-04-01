import os
def rename():
    name=input("ENTER THE PATH ")
    file_list=os.listdir(str(name))#List the files in directory.....
    print(file_list)#print the list
    working=os.getcwd()#get current working directory
    print(working)
    os.chdir(str(name))#CHANGE directory to path
    for file_name in file_list:
    os.rename(file_name,file_name.translate(None,"1234567890"))#.String function translate string first table (what chat changes to what) second except those char
    os.chdir(working)
    working=os.getcwd()
    print(working)
if __name__ == "__main__":
     rename()
