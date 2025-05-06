N = int(input())

scores = list(map(int, input().split()))

M = max(scores)
sum = 0

for score in (scores):
  score = score/M*100
  sum += score
  
print(sum/N)