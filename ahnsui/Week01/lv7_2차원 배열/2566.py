A = []

# 최댓값
M = 0

# 행, 열
x = 0
y = 0

for i in range (9):
  a = list(map(int, input().split()))
  A.append(a)
  
for i in range (9):
  if max(A[i]) > M:
    M = max(A[i])
    x = i
    y = A[i].index(max(A[i]))
    

print(M)
print(x+1, y+1)