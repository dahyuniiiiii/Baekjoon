n = int(input())
for i in range(n):
    sentence = input()
    sentence = sentence[0].upper() + sentence[1:]
    print(sentence)