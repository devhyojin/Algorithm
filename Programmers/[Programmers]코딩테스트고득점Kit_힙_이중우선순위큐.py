import heapq
def solution(operations):
    answer = [0,0]
    num_dic = {}
    min_heap, max_heap = [], []
    io_status = 0
    for operation in operations:
        alph, num = operation.split()
        if alph == 'I':
            io_status += 1
            num = int(num)
            if num in num_dic:
                num_dic[num] += 1
            else:
                num_dic[num] = 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif io_status > 0:
            io_status -= 1
            if num == '1':
                while True:
                    max_num = heapq.heappop(max_heap)
                    if num_dic[-max_num] > 0:
                        num_dic[-max_num] -= 1
                        break
            else:
                while True:
                    min_num = heapq.heappop(min_heap)
                    if num_dic[min_num] > 0:
                        num_dic[min_num] -= 1
                        break
    if io_status > 0:
        max_num, min_num = 0, 100000000
        for num, cnt in num_dic.items():
            if cnt > 0:
                min_num = min(min_num, num)
                max_num = max(max_num, num)
        return [max_num, min_num]
    return answer