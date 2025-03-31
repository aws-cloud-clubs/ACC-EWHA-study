s_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0, 0.0]
g_list = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']
sum = 0
score_sum = 0

for i in range (20):
  sub, score, grade = input().split()
  sum += float(score) * s_list[g_list.index(grade)]
  if grade=='P':
    score_sum += 0
  else: 
    score_sum += float(score)
  
print(sum / score_sum)