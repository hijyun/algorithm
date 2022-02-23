'''
<큰 수 만들기 - 원칙>
- 앞 자리에 큰 수가 오는 것이 전체를 크게 만든다.
    -> 따라서, 큰 것을 우선해서 골라 담고 싶다.

<큰 수 만들기 - 방법>
- 앞 자리에서 부터 하나씩 골라서 담되, 지금 담으려는 것 보다 작은 것들은 도로 뺀다 !
    단, 뺄 수 있는 수에 도달할 때 까지
- 큰 수가 앞자리에, 작은 수가 뒷자리에 놓이도록
    (제약 조건) : 뺄 수 있는 수가 k개

<구현>
- 주어진 숫 (number) 로 부터 하나씩 꺼내어 모으되
    - 이 때, 이미 모아둔 것 중 지금 등장한 것 보다 작은 것들을 빼낸다.
- 이렇게 모은 숫자들을 자릿수 맞추어 반환한다.
    - 아직 뺄 개수 (k)를 채우지 못한 경우를 고려해야함

<알고리즘의 복잡도>
- O(n)
'''

def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer