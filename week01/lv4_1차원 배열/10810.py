N, M = map(int, input().split())

arr = [0] * (N+1)

for a in range (0, M):
  i, j, k = map(int, input().split())
  for b in range (i, j+1):
    arr[b] = k
   
for c in range(1, N+1):
  print(arr[c], end=' ')  