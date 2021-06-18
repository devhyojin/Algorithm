#sol1
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        leng = len(columnTitle)
        char_dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                    'X': 24, 'Y': 25, 'Z': 26}

        answer = 0
        for i in range(leng):
            answer += char_dic[columnTitle[i]] * (26 ** (leng - 1 - i))
        return answer
# 44ms 14.3MB.... 아스키 관련 함수가 기억나지 않아서 적용한 풀이이다.

#sol2
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        leng = len(columnTitle)
        for i in columnTitle:
            answer = answer*26 + ord(i) - ord('A') + 1
        return answer
# 40ms 14.2MB 아스키코드 관련 함수를 사용했다.