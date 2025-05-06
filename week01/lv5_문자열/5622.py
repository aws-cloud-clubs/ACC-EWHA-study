s = input()
ans = 0
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(s)):
  if s[i] in abc[0:3]:
    ans += 3
  elif s[i] in abc[3:6]:
    ans += 4
  elif s[i] in abc[6:9]:
    ans += 5
  elif s[i] in abc[9:12]:
    ans += 6
  elif s[i] in abc[12:15]:
    ans += 7
  elif s[i] in abc[15:19]:
    ans += 8
  elif s[i] in abc[19:22]:
    ans += 9
  elif s[i] in abc[22:]:
    ans += 10

print(ans)
