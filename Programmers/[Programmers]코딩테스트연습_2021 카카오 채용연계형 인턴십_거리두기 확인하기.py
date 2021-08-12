# sol1
def distancing(area):
    #row
    for row in area:
        for j in range(3):
            temp = row[j:j+3]
            table_cnt, ppl_cnt = temp.count('O'), temp.count('P')
            if ppl_cnt > 1:
                if temp  == 'PXP':
                    continue
                return 0
    #col
    for j in range(5):
        for i in range(3):
            temp = area[i][j] + area[i+1][j] + area[i+2][j]
            table_cnt, ppl_cnt = temp.count('O'), temp.count('P')
            if ppl_cnt > 1:
                if temp  == 'PXP':
                    continue
                return 0
    #square
    for i in range(4):
        for j in range(4):
            temp = area[i][j] + area[i][j+1] + area[i+1][j] + area[i+1][j+1]
            table_cnt, ppl_cnt = temp.count('O'), temp.count('P')
            if ppl_cnt > 1:
                if temp in ("PXXP","XPPX"):
                    continue
                return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(distancing(place))
    return answer


#sol2
dr1=(-1,0,1,0)
dc1=(0,-1,0,1)

dr2=(-2,0,2,0)
dc2=(0,-2,0,2)

dr3=(-1,-1)
dc3=(-1,1)

def oob(y,x):
    if y<0 or y>4 or x<0 or x>4:
        return False
    return True

def distancing(area):
    for i in range(5):
        for j in range(5):
            if area[i][j] != 'P':
                continue
            #row
            for dir in range(4):
                nr1, nc1 = i+dr1[dir], j+dc1[dir]
                if oob(nr1, nc1) and area[nr1][nc1] == 'P':
                    return 0
            #col
            for dir in range(4):
                nr2, nc2 = i+dr2[dir], j+dc2[dir]
                if oob(nr2, nc2) and area[nr2][nc2] == 'P':
                    if area[i+dr1[dir]][j+dc1[dir]] == 'O':
                        return 0
            #square
            for dir in range(2):
                nr3, nc3 = i+dr3[dir], j+dc3[dir]
                if oob(nr3,nc3) and area[nr3][nc3] == 'P':
                    if area[i][nc3] == 'O' or area[nr3][j] == 'O':
                        return 0
    return 1
def solution (places):
    return [distancing(place) for place in places]