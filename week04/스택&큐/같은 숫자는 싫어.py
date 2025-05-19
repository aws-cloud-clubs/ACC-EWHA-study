def solution1(arr):
    answer = []

    for num in arr:
        if len(answer) == 0 or answer[-1] != num:
            answer.append(num)
    return answer
  
def solution2(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i] = 10
            
    answer = []
    
    for num in arr:
        if num != 10:
            answer.append(num)
    return answer