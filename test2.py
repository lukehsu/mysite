import datetime
import time
time1 = datetime.date.today()
t = time.time()

s = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
time = str(time)
a = {"a":time}
print  s