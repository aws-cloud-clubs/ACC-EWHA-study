# 풀이 1
import sys
s = sys.stdin.readlines()

for i in s:
  print(i.rstrip())
  
# 풀이 2
while True:
  try:
    print(input())
  except EOFError:
    break
  
# 풀이 3
import sys

while True:
  s = sys.stdin.readline().rstrip()
  if s == '':
    break
  else:
    print(s)
  