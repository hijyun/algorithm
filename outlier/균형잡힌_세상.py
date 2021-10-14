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

# + [markdown] id="view-in-github" colab_type="text"
# <a href="https://colab.research.google.com/github/hijyun/Python/blob/master/%EC%BD%94%EB%94%A9%EB%AC%B8%EC%A0%9C/%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C_%EC%84%B8%EC%83%81.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + [markdown] id="r8NWse_XLbxJ"
# # 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

# + [markdown] id="3itCLAZfLl7M"
# 세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
#
# 정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
#
# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
#
# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

# + [markdown] id="z3O2pdAdLn2c"
# ## 입력
# 하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.
#
# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

# + [markdown] id="ZlnnSesILrHh"
# # 출력
# 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

# + id="tsmc5Vk1LbF-"
def solution():
  while True:
    texts = input()

    if texts=='.':
      break

    stack = []
    answer = True

    table = {')':'(', ']':'[','}':'{'}

    for char in texts:
      if char in ('(','[','{',')',']','}'):
          if char not in table :
            stack.append(char)
          elif not stack or table[char] != stack.pop():
            answer = False

    if len(stack) != 0:
      answer = False

    if answer :
      print('yes')
    else:
      print('no')


# + colab={"base_uri": "https://localhost:8080/"} id="o5l5qlPWLdRu" outputId="16001aa8-91d8-4083-bd9b-c24c96968b6a"
solution().
