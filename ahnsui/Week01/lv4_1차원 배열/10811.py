N, M = map(int, input().split())
arr = [0] * (N+1)
tmp = [0] * (N+1)

for a in range (N+1):
  arr[a] = a
  
for _ in range (M):
  i, j = map(int, input().split())
  tmp = arr[i:j+1]
  tmp.reverse()
  arr[i:j+1] = tmp

for i in range(1, N+1):
  print(arr[i], end=' ')