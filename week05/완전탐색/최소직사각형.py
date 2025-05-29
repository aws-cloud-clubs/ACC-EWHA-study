def solution(sizes):
    max_width = 0
    max_height = 0
    for w, h in sizes:
        w, h = max(w, h), min(w, h)
        max_width = max(max_width, w)
        max_height = max(max_height, h)

    return max_width * max_height
