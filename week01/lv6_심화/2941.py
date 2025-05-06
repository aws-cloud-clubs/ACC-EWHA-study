word = input()
croatia_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_a:
  word = word.replace(i, '*')

print(len(word))