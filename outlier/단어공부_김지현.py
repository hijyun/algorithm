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
# <a href="https://colab.research.google.com/github/hijyun/simple_coding/blob/master/%EB%8B%A8%EC%96%B4%EA%B3%B5%EB%B6%80_%EA%B9%80%EC%A7%80%ED%98%84.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="rl5DSqFF-jBG"
def solution():
  word = input('단어 : ').upper()
  word_count = []
  
  if len(word) > 1000000:
    word = input('1000000개 아래로 입력해주세요 : ')


  for r in set(word):
    word_count.append(word.count(r))
  
  if len(set(word_count)) != len(list(word_count)):
    print('?')
  else:
    max_word = [ r for r in set(word) if word.count(r) == max(word_count)]

    print(max_word[0])

# + colab={"base_uri": "https://localhost:8080/"} id="MILzaGSWD143" outputId="033157aa-fec5-43f1-b994-0317dbbca428"
solution()

# + colab={"base_uri": "https://localhost:8080/"} id="Y7v2C5PWE8yv" outputId="1df93a9a-df9a-4fd6-c855-4e0856b93e63"
solution()
