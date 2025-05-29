import itertools

def solution(word):
    aeiou = ['A', 'E', 'I', 'O', 'U']
    all_words = []

    for i in range(1, 6):
        for p in itertools.product(aeiou, repeat=i):  # 중복 허용
            all_words.append(''.join(p))

    all_words.sort()
    return all_words.index(word) + 1
