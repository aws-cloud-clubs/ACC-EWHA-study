def solution(genres, plays):
    type = {}  # 장르별 총 재생 수
    song = {}  # idx: {'genre': 장르, 'play': 재생 수}
    
    for i in range(len(genres)):
        type[genres[i]] = type.get(genres[i], 0) + plays[i]
        song[i] = {'genre': genres[i], 'play': plays[i]}
    
    # [["pop",3100],["classic",1450]]
    type = sorted(type.items(), key=lambda x: x[1], reverse=True) 
    
    song = sorted(song.items(), key=lambda x: x[1]['play'], reverse=True)
    
    answer = []
    
    # 각 장르마다 상위 2개 노래 선택
    for genre, _ in type:
        count = 0
        for idx, info in song:
            if info['genre'] == genre:
                answer.append(idx)
                count += 1
            if count == 2:
                break
    
    return answer
