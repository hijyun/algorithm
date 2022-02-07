# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# - 순차 구조 sequential structure : 한 문장씩 순서대로 처리되는 구조
# - 선택 구조 select structure : 조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경되는 구조

# # 세 정수의 최댓값 구하기

# +
# 세 정수의 최댓값 구하기
print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요 : '))
b = int(input('정수 b의 값을 입력하세요 : '))
c = int(input('정수 c의 값을 입력하세요 : '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum}입니다.')

# -

def max3(a, b, c):
    """a,b,c의 최댓값을 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum


print(f'max(3,2,1) = {max3(3,2,1)}')

# # 문자열과 숫자 입력 받기

# 이름을 입력받아 인사하기
name = input('이름을 입력하세요 : ')
print(f'안녕하세요? {name}님')


# <PEP 8>
# * 클래스명은 카멜 케이스(CamelCase) 형식 : 대문자로 시작하고, 명사를 사용
# * 함수명은 스네이크(snake_case) 형식 : 모두 소문자로 표기하되, 단어 간에는 underscore(_)로 구

# # 세 정수의 중앙값 구하기

def med3(a, b, c):
    """a,b,c의 중앙값을 구하여 반환"""
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


# +
print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.'))
b = int(input('정수 b의 값을 입력하세요.'))
c = int(input('정수 c의 값을 입력하세요.'))

print(f'중앙값은 {med3(a, b, c)}입니다.')


# +
# 세 정수를 입력받아 중앙값 구하기 2

def med3(a, b, c):
    """a, b, c의 중앙값을 구하여 반환(다른 방법)"""
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < c and c > b):
        return b
    return c
# -


