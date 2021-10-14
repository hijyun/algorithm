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

# # 가장 큰 수 
# ### 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# ### 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# ### 입출력 예
# numbers	                return 
# * [6, 10, 2]	        6210 
# * [3, 30, 34, 5, 9]  	9534330 

# + id="glDgOt3OQoL7"
def mnum():
    a =[]
    nl = list(input('공백기준 숫자 input : ' ).split(' '))
    maxlen = max(list(map(len,nl)))
    for i,n in enumerate(nl):
        if len(n) == 1:
            n = n *(maxlen-len(n)+1)
        else:
            n = n + ('0'*(maxlen-len(n)))
        a.append((i,n))
        a.sort(key= lambda x : x[1], reverse=True)
    print('Output : ', ''.join([nl[k] for k,_ in a]))


# + colab={"base_uri": "https://localhost:8080/", "height": 0} id="yP2k4Y_66jZY" outputId="0a16035b-5b60-432c-cc8e-4d8884ea7440"
mnum()

# + colab={"base_uri": "https://localhost:8080/", "height": 0} id="QKw1xTVx6kqq" outputId="4be0b0c3-d6c2-48de-e472-433f8a599524"
mnum()
# -

mnum()


# # 더 나은 풀이

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


