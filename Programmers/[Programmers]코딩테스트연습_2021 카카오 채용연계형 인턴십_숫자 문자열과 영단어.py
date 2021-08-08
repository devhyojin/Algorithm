# sol1
num_dic={'zer':['0',1],'one':['1',0],'two':['2',0],'thr':['3',2],'fou':['4',1],'fiv':['5',1], 'six':['6',0], 'sev':['7',2], 'eig':['8',2], 'nin':['9',1]}
def solution(given):
    nums=[str(i) for i in range(0,10)]
    answer = ""
    p = 0
    while p != len(given):
        number=""
        temp = given[p]
        if temp in nums:
            answer += temp
            p+=1
        else:
            number += given[p:p+3]
            answer += num_dic[number][0]
            p += num_dic[number][1] + 3
    return int(answer)


#sol2
nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def solution(given):
    for idx, word in enumerate(nums):
        given = given.replace(word, str(idx))
    return int(given)