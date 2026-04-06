import time
from winotify import Notification

# change this to how often you want to take a break
mins = 20
secs = mins * 60

# notificaiton pop-up
toast = Notification(
  app_id="Reminder",
  title="Eye Break!",
  msg="Take a 20 second break for your eyes",
  duration="short"
)

while True:
  toast.show()  
  time.sleep(secs)
