arr = []

for _ in range (0, 9):
  a = int(input())
  arr.append(a)
  
M = max(arr)
print(M)
print(arr.index(M) + 1)