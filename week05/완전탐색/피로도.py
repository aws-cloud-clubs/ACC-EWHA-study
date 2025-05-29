# 순열 사용
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for (need, spend) in p:
            if tmp >= need:
                cnt += 1
                tmp -= spend
        answer = max(answer, cnt)
        
    return answer
  
  
# dfs 사용
def solution(k, dungeons):
  visited = [False] * len(dungeons)
  max_cnt = 0

  def dfs(current_k, cnt):
      nonlocal max_cnt
      max_cnt = max(max_cnt, cnt)

      for i in range(len(dungeons)):
          need, spend = dungeons[i]
          if not visited[i] and current_k >= need:
              visited[i] = True
              dfs(current_k - spend, cnt + 1)
              visited[i] = False  # 백트래킹

  dfs(k, 0)
  return max_cnt