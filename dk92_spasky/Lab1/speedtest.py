import time

start_for = time.time()

for i in range(15):
  print("for", i)

print("Time for:", (time.time() - start_for))

start_while  = time.time()

i = 0
while i < 15:
  print("while", i)
  i += 1

print("Time  while: ", (time.time() - start_while))
