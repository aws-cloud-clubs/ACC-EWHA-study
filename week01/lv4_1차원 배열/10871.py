N, X = map(int, input().split())
arr = list(map(int, input().split()))

for num in arr:
  if num < X:
    print(num, end=' ')