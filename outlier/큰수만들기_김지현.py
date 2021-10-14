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

# + id="Wgw22cCbhLqP"
def max_num(k):
    a =[]
    num = input('Input : ')

    for i, n in enumerate(num):
      a.append((i,n))
    a.sort(key= lambda x : x[1])
    a = a[k:]
    a.sort(key = lambda x : x[0])
    print('Output :',''.join([n for _,n in a]))


# + colab={"base_uri": "https://localhost:8080/"} id="pX1ecbcSowqD" outputId="46559ee5-10d4-4e18-b6e7-acf33726188e"
max_num(2)

# + colab={"base_uri": "https://localhost:8080/"} id="54btUJSZoxk2" outputId="11c1a9c7-c85b-4397-9f24-e8a7ce4e8380"
max_num(3)

# + id="WdRUAGo1tYC5"

