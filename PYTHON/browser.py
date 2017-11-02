#open webbrowser with a url
import webbrowser
import time
new=1 #new tab in default browser
for i in range(3):
  url="https://www.youtube.com/watch?v=pXPHSaj8qSw"
  print (time.ctime())#show current time
  time.sleep(5)#sleep for 10 second
  webbrowser.open(url,new=new)#open in default browser
#open in safari
#webbrowser.get("safari").open(url,new=new)
