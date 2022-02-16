def solution(participant, completion):
    dict = {}
    # 참가자 이름과 수를 딕셔너리에 저장
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    # 완주한 이름을 딕셔너리에서 제거
    for i in completion:
        if dict[i] == 1:
            del dict[i]
        else:
            dict[i] -= 1

    return list(dict)[0]