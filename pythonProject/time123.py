import datetime
import time
# Get Current Date with Current Time
dt=datetime.datetime.now()
print(dt.strftime("%Y-%b-%d %H:%M"))

#strftime function is useful

#returns actual date
td=datetime.date.today()
print(td.strftime("%B-%Y-%d"))

#prints time in ascci
tt=time.asctime(time.localtime(time.time()))
print(tt)

tt=time.localtime().tm_year
print(tt)
tt=time.localtime().tm_mon
print(tt)
tt=time.localtime().tm_hour
print(tt)
