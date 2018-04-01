#open webbrowser with a url
import webbrowser
import time
import vlc

new=1 #new tab in default browser
url="https://www.youtube.com/watch?v=ORIpWftFyqo"
print (time.ctime())#show current time
print ("WARMUP FOR 10 MIN")
mins=0
while mins != 10:
        print(mins)
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
min=0
start=vlc.MediaPlayer("file:///Users/SINGH/Desktop/GITHUB/Python_Learning/PYTHON/START.wav")
stop=vlc.MediaPlayer("file:///Users/SINGH/Desktop/GITHUB/Python_Learning/PYTHON/STOP.wav")
while min != 10:
        print(mins)
        # Sleep for a minute
        start.play()
        time.sleep(30)
        # Increment the minute total
        stop.play
        time.sleep(30)
        mins += 1


