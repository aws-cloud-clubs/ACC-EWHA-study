N = int(input())

for i in range (1, 2*N, 2): #1, 3, 5, 7, 9 / 4, 3, 2, 1, 0
  print(' ' * ((2*N-1-i)//2) + '*' * i)
  
for i in range (2*N-3, 0, -2): #7, 5, 3, 1 / 1, 2, 3, 4
  print(' ' * ((2*N-1-i)//2) + '*' * i)
