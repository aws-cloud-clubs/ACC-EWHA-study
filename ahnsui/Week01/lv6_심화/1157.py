word = input().upper()
word_list = list(set(word))


cnt = [0] * len(word_list)

for i in range(len(word_list)):
  cnt[i] = word.count(word_list[i])
  
if cnt.count(max(cnt)) > 1:
  print('?')
else:
  print(word_list[cnt.index(max(cnt))])