from collections import defaultdict

def solution(genres, plays):
    music_dic = defaultdict(list)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        music_dic[genre].append((play, idx))

    for music in music_dic.values():
        music.sort(key=lambda x: (-x[0], x[1]))

    answer = []
    genre_cnt = sorted(music_dic.keys(), key=lambda x: -sum([cnt for cnt, _ in music_dic[x]]))
    for genre in genre_cnt:
        for _, idx in music_dic[genre][:2]:
            answer.append(idx)
    return answer