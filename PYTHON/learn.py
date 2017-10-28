def main():
 name=input("Enter the name ")
 name1="hello "+str(name)
 print(name1)
 a=10 #a is refrence to 10
 b=20.5
 ll="sum is" + str(a+b)
 print(ll)
 a=a+b
 print (type(a))
 print (a)
 print (id(a)) #gives address to which a points
 print (len(name))
 b=a #b is pointing to same object that of a
 b=b+1
 #b now points to another object that contain 11
 print (name[0:3])
 mylist=[1,11,9,5,6]
 print(mylist)
 mylist1=sorted(mylist)#SORT MYLIST AND SAVE IT AS COPY.DOESNOT CHANGE MYLIST 
 print(mylist)
 print(mylist1)
 mylist.sort()#SORT MYLIST AND DOES CHANGE MYLIST 
 print (len(mylist))
 print (mylist[1])
 mylist[1]=66
 #name[1]='A' NOT ALLOWED
 print (mylist)
 mylist=mylist+mylist1#CONCANATE MYLIST
 print (mylist)
 print (sorted(mylist,reverse=1))
 mylist3=[1,2,2]
 mylist3=mylist3*2 #DUPLICATE THE LIST 2 TIMES
 print(mylist3)
 for i in range(3):
  print("hello ",end="")
 a=123
 print("hello {}".format(a))
if __name__ == "__main__":
     main()
