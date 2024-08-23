aresult = 0
bresult = 0
for i in range(3):
    a = int(input())
    aresult += a * (3 - i)
for i in range(3):
    b = int(input())
    bresult += b * (3 - i)
if aresult < bresult:
    print('B')
elif aresult > bresult:
    print('A')
else:
    print('T')