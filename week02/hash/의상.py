def solution(clothes):
    category = {}
    for clothe in clothes:
        category[clothe[1]] = category.get(clothe[1], 0) + 1
        
    answer = 1
    for key in category:
        category[key] += 1
        answer *= category[key]

    return answer-1