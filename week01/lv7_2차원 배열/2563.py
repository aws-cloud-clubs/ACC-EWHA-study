N = int(input())
ans = 0
arr = [[0]*100 for _ in range (100)]

for _ in range(N):
  y, x = map(int, input().split())
  
  for i in range(x, x+10):
    for j in range(y, y+10):
      arr[i][j] = 1

for i in range(100):
  ans += arr[i].count(1)

print(ans)