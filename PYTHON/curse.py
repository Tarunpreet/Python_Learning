import urllib
def read_file():
    path=input("ENTER THE PATH: ")
    readm=open(str(path))
    lines=readm.read()
    print(lines)
    readm.close()
    checkcurse(lines)
def checkcurse(lines1):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+lines1)
    response=connection.read()
    connection.close()
    if "true" in response:
        print("curse found")
    elif "false" in response:
        print("curse not found")
read_file()
