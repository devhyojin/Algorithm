#sol1
from collections import defaultdict
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

def solution(arrows):
    visit_dic = defaultdict(set)
    cr,cc = 0,0
    room = 0
    for arrow in arrows:
        for _ in range(2): #대각선 판별을 위해 점, 선이 해당하는 부분 모두를 기록하자. ex)점선점
            nr, nc = cr+dr[arrow], cc+dc[arrow]
            if (nr, nc) not in visit_dic:
                visit_dic[(cr,cc)].add((nr,nc))
                visit_dic[(nr,nc)].add((cr,cc))
            elif (nr, nc) not in visit_dic[(cr,cc)]:
                room += 1
                visit_dic[(cr,cc)].add((nr,nc))
                visit_dic[(nr,nc)].add((cr,cc))
            cr, cc = nr, nc
    return room

#sol2 (오일러)
def solution(arrows):
    v = set()
    e = set()
    cr, cc = 0, 0
    v.add((cr, cc))

    for arrow in arrows:
        for _ in range(2):  # 대각선 판별을 위해 점, 선이 해당하는 부분 모두를 기록하자. ex)점선점
            nr, nc = cr + dr[arrow], cc + dc[arrow]
            v.add((nr, nc))

            start = (cr, cc)
            end = (nr, nc)

            if start > end:
                start = (nr, nc)
                end = (cr, cc)
            e.add((start, end))

            cr, cc = nr, nc
    return len(e) - len(v) + 1