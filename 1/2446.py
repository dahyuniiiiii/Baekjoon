n = int(input())
for i in range(n):
    print(' '*(i)+'*'*(2*(n-i)-1))
for i in range(n-1):
    print(' '*(n-i-2)+'*'*(2*i+3))
