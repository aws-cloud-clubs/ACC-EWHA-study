def solution(brown, yellow):
    sum_xy = (brown - 4) // 2
    x = 0
    y = 0
    
    for i in range(1, sum_xy+1):
        if i * (sum_xy-i) == yellow:
            x = i
            y = sum_xy-i
    
    answer = [max(x, y)+2, min(x, y)+2]
    return answer