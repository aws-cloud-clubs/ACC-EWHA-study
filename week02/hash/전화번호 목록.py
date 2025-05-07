# 풀이 1
def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
            return False
            break
    return True
  

# 풀이 2  
def solution2(phone_book):
    phones = {}
    
    for phone in phone_book:
        phones[phone] = 0
    
    for phone in phones:
        temp = ''
        for num in phone:
            temp += num
            if temp in phones and temp != phone:
                return False
                break
    return True
                