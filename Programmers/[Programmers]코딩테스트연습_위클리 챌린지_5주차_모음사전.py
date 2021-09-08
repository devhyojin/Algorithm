def solution(word):
    alph_dic = {'A':0, 'E': 1, 'I':2, 'O':3, 'U':4}
    def gs_sum(x):
        return (5**x) // (5-1)

    answer = len(word)
    for idx, char in enumerate(word):
        if char == 'A':
            continue
        answer +=  alph_dic[char] * gs_sum(5-idx)

    return answer