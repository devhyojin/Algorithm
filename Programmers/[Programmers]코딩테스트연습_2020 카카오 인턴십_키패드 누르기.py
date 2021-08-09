def solution(numbers, hand):
    result = ''
    phone_dic = {0:(3,1),1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
    left, right = (3,0), (3,2)
    for number in numbers:
        if number in (1,4,7):
            left = phone_dic[number]
            result += 'L'
        elif number in (3,6,9):
            right = phone_dic[number]
            result += 'R'
        else:
            r, c = phone_dic[number]
            left_far = abs(left[0]-r)+abs(left[1]-c)
            right_far = abs(right[0]-r)+abs(right[1]-c)
            if left_far < right_far:
                left = (r,c)
                result += 'L'
            elif left_far > right_far:
                right = (r,c)
                result += 'R'
            else:
                if hand == 'left':
                    left = (r,c)
                    result += 'L'
                else:
                    right = (r,c)
                    result += 'R'
    return result