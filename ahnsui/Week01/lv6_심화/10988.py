w = input()
l = len(w) #5

ans = 0

for i in range (0, l): # i = 0, 1, 2, 3, 4 
  if w[i] != w[l-i-1]: #   = 4, 3, 2, 1, 0
    ans += 1
  else:
    ans += 0
    
if ans==0:
  print(1)
else:
  print(0)
  
# 2번째 풀이
word = list(str(input()))
print(word)

if list(reversed(word)) == word:
    print(1)
else:
    print(0)