import time
t=time.time()
print("start")
a=0
b=100000000
while a<b:
    a=a+1
tt=time.time()
print("time while",tt-t)
i=0
a=0
c=range(b)
t=time.time()
for i in c:
    a=a+1
tt=time.time()
print("time for  ",tt-t)
print("end")
while True:
    a=10
