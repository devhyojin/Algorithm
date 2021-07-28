def solution(N, number):
    answer = -1
    ans_list = [set() for _ in range(9)]
    ans_list[1].add(N)

    for i in range(2, 9):
        ans_list[i].add(int(str(N) * i))
        for half in range(1, i // 2 + 1):
            for a in ans_list[half]:
                for b in ans_list[i - half]:
                    ans_list[i].add(a + b)
                    ans_list[i].add(a - b)
                    ans_list[i].add(b - a)
                    ans_list[i].add(a * b)
                    if b != 0:
                        ans_list[i].add(a // b)
                    if a != 0:
                        ans_list[i].add(b // a)
    for i in range(1, 9):
        if number in ans_list[i]:
            answer = i
            break
    return answer