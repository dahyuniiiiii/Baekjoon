result = 0
result1 = 0
for i in range(3):
    a = int(input())
    result += a
for i in range(3):
    b = int(input())
    result1 += b
if result > result1 :
    print('A')
if result < result1 :
    print('B')
else :
    print('T')