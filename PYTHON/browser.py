#open webbrowser with a url
import webbrowser
import time
new=1 #new tab in default browser
for i in range(2):
  url="https://www.youtube.com/watch?v=ORIpWftFyqo"
  print (time.ctime())#show current time
  time.sleep(2)#sleep for 10 second
  webbrowser.open(url,new=new)#open in default browser
  url="https://www.youtube.com/watch?v=HC172grgTwU"
  time.sleep(300)#sleep for 10 second
  webbrowser.open(url,new=new)#open in default browser
  url="https://www.youtube.com/watch?v=2tIulahZbvo"
  time.sleep(300)#sleep for 10 second
  webbrowser.open(url,new=new)#open in default browser
#open in safari
#webbrowser.get("safari").open(url,new=new)
