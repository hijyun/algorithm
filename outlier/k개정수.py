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
# <a href="https://colab.research.google.com/github/hijyun/Python/blob/master/%EC%BD%94%EB%94%A9%EB%AC%B8%EC%A0%9C/k%EA%B0%9C%EC%A0%95%EC%88%98.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + [markdown] id="jgIPrh2ZwKHH"
# # k 개의 정수

# + [markdown] id="evyQYmmXL4p4"
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=53&sca=1090

# + [markdown] id="nUIWmO5sL68X"
# 100개의 정수를 입력받을 수 있는 배열을 선언한 후 정수를 차례로 입력 받다가 -1이 입력되면 입력을 중단하고 -1을 제외한 마지막 세 개의 정수를 출력하는 프로그램을 작성하시오. (입력받은 정수가 -1을 제외하고 3개 미만일 경우에는 -1을 제외하고 입력받은 정수를 모두 출력한다.)

# + id="g400ws9_n27j"
def k_int():
  num_list = []

  while len(num_list)<100:
    num_list.append(int(input()))

    if num_list[-1] == -1:
      break

  #  프린트
  for n in num_list[-num_list[0]-1:-1]:
    print(n,end=' ')


# + colab={"base_uri": "https://localhost:8080/", "height": 0} id="FEnpd2n8pWMw" outputId="57dffba7-2d64-408e-f026-97a07047c030"
k_int()

# + colab={"base_uri": "https://localhost:8080/", "height": 0} id="0uUjM0TyqVrB" outputId="adb0f8a2-3a47-4e03-83e8-d59d0b8464c1"
k_int()
