from sys import argv

print(argv)

bit_depth = 2**int(argv[1])

rezult = (int(argv[2]) * int(argv[3])) / bit_depth

print(f"Output freq NCO generator: {rezult}")