'''
< 문제 분석 >
- 이 문제의 크기는 몇명이 마라톤 경기에 참여했는지에 따라 결정된다.
- 최대 10만명이기 때문에 n이나 nlogn에 비례하는 정도의 알고리즘을 착안하는게 좋을 것 같다.
- 동명이인이 있을 수 있으므로 이 경우를 처리하는게 문제가 될 수 있음 !
- 이름이 주어지면 몇 번이나 배열에 등장했는지 데이터를 저장할 수 있는 구조가 필요함. => '해시' !!
'''



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


# 4-6번째 줄에서 분기 처리로 dict[key]의 KeyError 를 방지하였는데
# 이 경우엔 dicts.get() 메소드를 사용하면 분기처리 없이 원하는 내용을 구현할 수 있음
'''<예시>
def solution(participant, completion):
    d = {}
    for x in participant:
    	d[x] = d.get(x, 0) + 1
    for x in completion:
    	d[x] -= 1
    dnf = [k for k, v in d.items() if v > 0]
    answer = dnf[0]
    return answer
'''