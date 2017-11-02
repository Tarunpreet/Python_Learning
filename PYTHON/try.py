name=input("ENTER: ")
path=input("ENTER THE PATH: ")
i=len(name)
j=0
name1=""
while(j<i):
    if(j>len(path)):
        name1=name1+name[j]
    j=j+1
print(name1)
