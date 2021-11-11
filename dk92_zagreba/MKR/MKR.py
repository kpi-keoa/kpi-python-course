from collections import Counter
 
print("Ведите желаемое сопротивлеине, потом какие подключено резисторы, в конце введите q")
R = []
i=0;
while 1>0:
    T = input()
    if T=="q" or T=="Q" or T=="й" or T=="Й":
        break
    R.append(T)
print("Вы ввели ",R)
print("Бажанно ",R[0])

c = Counter(R)
ii=0

while ii<len(c):
    print(R[ii]," всего ",c[R[ii]])
    ii+=1
iii=1
R_oll=0
while iii<len(R):
    R_oll+=1/int(R[iii])
    iii+=1
R_oll=1/R_oll
print("реально ",R_oll)
OUT = (c,float(R[0])-R_oll)
print("выход ",OUT)
input()










