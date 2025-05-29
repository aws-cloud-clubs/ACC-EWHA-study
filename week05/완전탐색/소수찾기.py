import itertools

cnt = 0

def find_decimal(number):
    global cnt
    if number < 2:
        return
    for i in range(2, int(number**0.5) + 1): # number도 가능하지만 제곱근+1까지만 계산. 더 빠르다
        if number % i == 0:
            return
    cnt += 1

def solution(numbers):
    all_nums = set()
    
    for i in range(1, len(numbers) + 1):
        perms = itertools.permutations(numbers, i)
        for p in perms:
            num = int(''.join(p))
            all_nums.add(num)
    
    for num in all_nums:
        find_decimal(num)
    
    return cnt

# for p in perms: print(p) => ('1',), ('7',), ('1', '7'), ('7', '1')
