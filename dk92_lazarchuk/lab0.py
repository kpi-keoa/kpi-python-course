def avgg(agrs):
    summ = 0
    for i in range(len(agrs)):
        summ += float(agrs[i])
    return summ / len(agrs)

i_d = []
for i in range(100):
    sw = input()
    if(sw == 'avg'):
        print(f'average: {avgg(i_d)}')
        break
    else:
        i_d.append(sw)