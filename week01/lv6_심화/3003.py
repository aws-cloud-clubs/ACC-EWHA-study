w = list(map(int, input().split()))

list = [1, 1, 2, 2, 2, 8]

for i in range (len(list)):
    if w[i] == list[i]:
        print(0, end=' ')
    else:
        print(list[i]-w[i], end=' ')