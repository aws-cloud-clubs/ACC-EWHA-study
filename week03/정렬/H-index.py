def solution(citations):
    n = len(citations)
    citations.sort()
    for i in range(n):
        h = n - i  # 인용 수가 h 이상인 논문 수
        if citations[i] >= h:  # 그 중 첫 논문의 인용 수가 h 이상이어야 함
            return h
    return 0
