import time 

start_time_loop_for = time.time()

for i in range(10):
	print("Loop <for>...%d" % (i))

print("Time loop for: %s \n" % (time.time() - start_time_loop_for))

start_time_loop_while  = time.time()

i = 0
while i < 10:
	print("Loop <while>...%d" % (i))
	i += 1

print("Time loop for: %s" % (time.time() - start_time_loop_while))