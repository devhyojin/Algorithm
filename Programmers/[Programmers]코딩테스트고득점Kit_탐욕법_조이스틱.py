def solution(name):
    s, e = ord('A'), ord('Z') + 1
    ascii_name = [min(ord(char) - s, e - ord(char)) for char in name]

    idx, answer = 0, 0
    while True:
        answer += ascii_name[idx]
        ascii_name[idx] = 0

        if sum(ascii_name) == 0:
            break

        l, r = 1, 1
        while ascii_name[idx - l] == 0:
            l += 1
        while ascii_name[idx + r] == 0:
            r += 1

        answer += l if l < r else r
        idx += -l if l < r else r

    return answer