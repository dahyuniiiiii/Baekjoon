n = int(input())
nums=[] #list라는 리스트명은 사용 금지
for i in range(n):
    a = int(input())
    nums.append(a) #리스트에 입력값 추가
nums.sort() #오름차순 정렬
for i in nums:
    print(i) #하나씩 요소 출력
