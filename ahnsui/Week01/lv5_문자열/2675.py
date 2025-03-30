N = int(input())

for _ in range (N):
  num, str = input().split()
  for i in range (len(str)):
    print(int(num) * str[i], end='')
  print()