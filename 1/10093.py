a, b = map(int, input().split())
# 두 수의 범위 사이에 있는 숫자를 모두 출력하기 위해 min과 max를 사용
if a < b:
    start, end = a + 1, b
else:
    start, end = b + 1, a

# 두 수 사이의 숫자 개수 출력
count = end - start
print(count)

# 두 수 사이의 숫자를 오름차순으로 출력
if count > 0:
    for i in range(start, end):
        print(i, end=' ')
    print()
else:
    print()







