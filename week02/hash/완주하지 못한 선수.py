def solution(participant, completion):
    people = {}
    
    for name in participant:
        if name in people:
            people[name] += 1
        else:
            people[name] = 1
    
    for name in completion:
        people[name] -= 1

    for key in people:
        if people[key] != 0:
            return key
