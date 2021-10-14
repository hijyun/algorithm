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
# <a href="https://colab.research.google.com/github/hijyun/Python/blob/master/elice/elice_pretrack.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + [markdown] id="6GGoyO1MdGcV"
# Q.몇 번째 동물이 동물의 왕이 되었을까요?
# 하트여왕의 생일 파티장에 코더랜드 동물 100마리가 모였습니다. 사회자 도도새가 말합니다.
#
#
# “친애하는 동물 여러분! 여기 모인 100마리의 동물들이 대회를 가질 것입니다. 대회에서 이기는 동물은 동물의 왕으로 선발됩니다!”
#
# 높이 날기 대회, 땅굴 속으로 빨리 숨기 대회, 망고 열매 따기 대회, 물 속에서 숨 참기 대회 등 어떤 대회로 동물의 왕을 뽑을지를 두고서 실랑이가 벌어졌어요.
#
# 그러자 싸움을 말리기 위해서 도도새가 이렇게 제안합니다.
#
# “여러분, 제가 아주 공평한 제안을 하겠습니다. 먼저 여러분께 1번부터 100번까지 무작위로 번호를 나눠드릴 테니 모두 순서대로 원 위에 서주세요. 저는 1번 동물에게 막대기를 드리겠습니다. 막대기를 받은 동물이 다음 동물(2번)을 막대기로 찌르면 그 동물은 원 밖으로 나가고, 막대기는 그다음 동물(3번)에게 전달됩니다. 그렇게 마지막 한 분이 남을 때까지 반복하는 거죠.
# 자, 그럼 2번분은 나가주세요. 그리고 4번분…”
#
#

# + id="PZR6BTM7X4RZ" colab={"base_uri": "https://localhost:8080/"} outputId="ebc2bcc0-2d3e-496a-8bbe-72eaddbc1011"
num = list(range(1,101,1))
print(num)

while len(num) != 1 :

  num.append(num[0])
  del num[0]
  del num[0]

print(num)

# + [markdown] id="K0eW0keTdOQo"
#  정답 : https://blog.naver.com/elicer/221474267403
