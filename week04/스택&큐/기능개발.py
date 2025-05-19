def solution(progresses, speeds):
    answer = []
    rest = []
    count = 1
    
    # rest 계산
    for i in range(len(progresses)):
        rest.append(100-progresses[i])
        if rest[i] % speeds[i] > 0:
            rest[i] = rest[i] // speeds[i] + 1
        else:
            rest[i] = rest[i] // speeds[i]
    
    # 앞이 더 크면 앞이랑 같은 수로 수정
    for j in range(len(rest)-1):
        if rest[j] > rest[j+1]:
            rest[j+1] = rest[j]
            
    # 같은 수 count
    for k in range(len(rest)-1):
        if rest[k] == rest[k+1]:
            count += 1
        else:
            answer.append(count)
            count = 1

  # 마지막 count 추가
    answer.append(count)
        
    return answer