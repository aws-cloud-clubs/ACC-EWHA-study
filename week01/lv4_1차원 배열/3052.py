arr=[0] * 10
ans = 0

for i in range (10):
  n = int(input())
  arr[i] = n%42

# set은 중복 요소를 삭제해주고 집합{} 형태로 바꿔줌
print(len(set(arr)))
  