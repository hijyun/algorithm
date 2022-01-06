'''
< 빠르게 입력 받기 >
: 입력 데이터의 개수가 많은 문제에 input() 함수를 이용하면 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있다.
입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.
'''

import sys
# 하나의 문자열 데이터 입력 받기
input_data = sys.stdin.readline().rstrip()

# 입력 받은 문자 그대로 출력
print(input_data)

