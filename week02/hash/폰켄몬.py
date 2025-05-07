# 풀이 1
def solution(nums):
    mons = {}
    number = len(nums) // 2
    
    for i in nums:
        mons[i] = 0
    
    monsnum = len(mons)
    if number > monsnum:
        return monsnum
    else:
        return number
    
# 풀이 2
def solution2(nums):
    return min(len(nums)/2, len(set(nums)))