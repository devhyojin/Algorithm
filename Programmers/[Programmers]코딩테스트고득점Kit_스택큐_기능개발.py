def solution(progresses, speeds):
    answer = []
    day = 0
    feature_cnt = 0
    while progresses:
        if progresses[0] + day*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            feature_cnt += 1
        else:
            if feature_cnt:
                answer.append(feature_cnt)
                feature_cnt = 0
            day += 1
    answer.append(feature_cnt)
    return answer

def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        # 아직 아무 기능도 끝나지 않은 상태 or 이전 기능 끝나기 위해 필요한 날보다 지금 p 기능 끝나기 위해 필요한 날이 더 많을 때
        if not answer or answer[-1][0] < -((p-100)//s):
            # 100퍼센트를 넘기기 위해 필요한 최소 일 수를 추가한다.
            answer.append([-((p-100)//s), 1])
        else:
            answer[-1][1] += 1
    return [a[1] for a in answer]