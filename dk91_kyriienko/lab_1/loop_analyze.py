import time 

rep = int(input())

st_time_for = time.time()

for i in range(rep):
	print(f'for|{i}')

print('Time for: %f' % (time.time()-st_time_for))

st_time_while = time.time()

i = 0
while i < rep:
	print(f'while|{i}')
	i += 1

print('Time while: %f' % (time.time()-st_time_while))