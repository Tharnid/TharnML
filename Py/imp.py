import datetime
import time

a = datetime.date.today()
print(a)

b = time.strftime("%H:%M")
print(b)

# Day AM or PM
c = time.strftime("%A:%p")
print(c)
