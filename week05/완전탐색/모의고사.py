def solution(answers):
    ans = []
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0

    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    del a[len(answers):]
    del b[len(answers):]
    del c[len(answers):]

    for i in range(len(answers)):
        if answers[i] == a[i]:
            cnt_a += 1
        if answers[i] == b[i]:
            cnt_b += 1
        if answers[i] == c[i]:
            cnt_c += 1
    
    cnt_max = max(cnt_a, cnt_b, cnt_c)
    if cnt_max == cnt_a:
        ans.append(1)
    if cnt_max == cnt_b:
        ans.append(2)
    if cnt_max == cnt_c:
        ans.append(3)
        
    return ans