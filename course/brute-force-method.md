# 브루트 포스법

: brutu는 무식한, force는 힘이라는 뜻이다. 무식하게 힘으로 해결하는 방법.
즉, 가장 간단한 알고리즘으로 가능한 모든 경우의 수를 검사하는 알고리즘이다.

<br>
<br>


## 문자열 검색 string searching 이란 ?
: 어떤 문자열 안에 다른 문자열이 포함되어 있는지 검사하고, 만약 포함되어 있다면 어디에 위치하는지 찾아내는 것. </br>

<br>
* 텍스트 text :  검색되는 쪽의 문자열 </br>
* 패턴 pattern : 찾아내는 문자열

<br>

ex. 문자열 'yena'에서 'na'를 검색하면 성공, 'bibi'에서 'na'를 검색하면 실패. 여기서 텍스트는 'yena', 'jiyun'이 되고, 패턴은 'na'가 된다.

<br>

## 브루트 포스법 brute force method
: 브루트 포스는 선형 검색을 단순하게 확장한 알고리즘이라서 **단순법** 이라고도 한다.

<br>
<br>


### 문제 해결 방법
1. 주어진 문제를 선형으로 구조화 한다.
2. 구조화된 문제 공간을 적절한 방법으로 해를 구성할 때 까지 탐색한다.
3. 구성된 해를 정리한다.

<br>
<br>

### 예제
브루트 포스법으로 문자열을 검색하는 과정은 다음과 같다.


<img width="400" alt="스크린샷 2022-02-12 오후 6 05 17" src="https://user-images.githubusercontent.com/54613024/153704928-eff21d05-1e98-4665-b7a0-ff4a041be853.png">


<img width="400" alt="스크린샷 2022-02-12 오후 6 04 40" src="https://user-images.githubusercontent.com/54613024/153704899-67438284-fe3d-486d-a9fc-c91b2667f2aa.png">


<br>
<br>

### 소스 코드
브루트 포스법으로 문자열을 검색하는 과정을 구현하면 다음과 같이 나타낼 수 있다.


```python
def bf_match(txt: str, pat: str) -> int:
    """브루트 포스법으로 문자열 검색"""
    pt = 0  # txt(텍스트)를 따라가는 커서
    pp = 0  # pat(패턴)를 따라가는 커서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트용 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴용 문자열

    idx = bf_match(s1, s2)  # 문자열 s1~s2를 브루트 포스법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')
```

<br>
<br>

## 시간 복잡도
: O(mn)이지만 일부러 꾸며 낸 패턴이 아니라면 O(n)이 된다.

* 단순한 알고리즘이지만 실제로는 아주 빠르게 동작한다 !

<br>
<br>


# 참고 자료
* Bohoyoh Shibata, 이지스퍼블리싱, Doit 자료구조와 함께 배우는 알고리즘 입문
* https://hcr3066.tistory.com/26