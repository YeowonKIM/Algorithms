def solution(genres, plays):
    answer = []
    genre_plays = {}  # 장르별 총 재생횟수 내림차순 : {장르 : 총재생횟수}
    g_p_idx = {}  # 장르, 플레이 횟수, 고유번호 : {장르 : [(플레이횟수, 인덱스)]

    for i in range(len(genres)):
        genre_plays[genres[i]] = genre_plays.get(genres[i], 0) + plays[i]
        g_p_idx[genres[i]] = g_p_idx.get(genres[i], []) + [(plays[i], i)]

    # 재생횟수 내림차순으로 정렬
    g_plays_desc = sorted(genre_plays.items(), key=lambda x: x[1], reverse=True)

    # 재생횟수 내림차순, 인덱스 오름차순 정렬
    for genre, tot_plays in g_plays_desc:
        g_p_idx[genre] = sorted(g_p_idx[genre], key= lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in g_p_idx[genre][:2]]

    return answer