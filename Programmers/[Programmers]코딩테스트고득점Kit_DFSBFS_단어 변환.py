def calc(cur_word, word):
    diff_cnt = 0
    for c, w in zip(cur_word, word):
        if c != w: diff_cnt += 1
    if diff_cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    visited = [0 for _ in range(len(words))]
    path = [begin]

    while path:
        cur_word = path.pop()
        if cur_word == target:
            return answer
        for idx, word in enumerate(words):
            if not visited[idx] and calc(cur_word, word):
                visited[idx] = 1
                path.append(word)

        answer += 1
