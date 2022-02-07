# 재귀 recursion
## 재귀 알고리즘의 기본
* 재귀란 ?
    - 어떠한 이벤트에서 자기 자신을 포함하고 다시 자기 자신을 사용하여 정의되는 경우
    - 재귀를 사용하면 프로그램을 간결하고 효율성 좋게 작성할 수 있음

<br>

### **재귀 호출 recursive call**
  * '자기 자신과 똑같은 함수'를 호출한다.
  * ex - 팩토리얼 구하기 
    * factorial() 함수는 n - 1의 팩토리얼 값을 구하기 위해 다시 자기 자신과 똑같은 factorial() 함수를 호출한다.

```python
def factorial(n: int) -> int:
    """양의 정수 n의 팩토리얼을 구하는 과정"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
```

사실 팩토리얼은 재귀 함수로 정의하지 않는 것이 더 간단함

<br>

### 직접 재귀와 간접 재귀
  * 직접 재귀 : 자신과 똑같은 함수를 호출하는 방식
  * 간접 재귀 : a()함수가 b()를 호출하고 다시 b()함수가 a()를 호출하는 구조

<img width="846" alt="스크린샷 2022-02-08 오전 12 11 40" src="https://user-images.githubusercontent.com/54613024/152815191-ac2719c2-a2ad-49b0-bcae-402caa059e2f.png">


<br>
<br>

## 재귀 알고리즘 분석

아래와 같은 recur() 함수는 재귀 호출을 여러번 실행하는 순수한 genuinely 재귀이다. 다른 함수들과 달리 동작이 복잡하여 실행 결과를 예측하기 어렵다. 
recur()함수를 **하향식 top-down**과 **상향식 bottom-up**방식으로 분석해보자.


```python
def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('정숫값을 입력하세요.: '))

recur(x)
```

* 실행 결과

```bash
정수값을 입력하세요.: 4
1
2
3
1
4
1
2
```



<br>

### 하향식 분석 top-down analysis
: 가장 위쪽에 위치한 상자의 함수 호출부터 시작하여 계단식으로 자세히 조사해 나가는 분석 방법



<img width="600" alt="스크린샷 2022-02-08 오전 1 10 05" src="https://user-images.githubusercontent.com/54613024/152826386-e6e856a6-054b-4cbb-9d30-89d6f87087c7.png">

recur(4)는 recur(3)과 recur(2)를 호출하고, recur(3)은 다시 recur(2)와 recur(1)을 호출이다. 이 과정을 그림으로 표현하면 위와 같다.

<img width="600" alt="스크린샷 2022-02-08 오전 1 38 58" src="https://user-images.githubusercontent.com/54613024/152831628-d3aed530-9f60-4578-952b-03fba928a8d1.png">

recur(4)는 4를 출력하기 전에 recur(3)을 호출하고, <br>
recur(3)은 3을 출력하기 전에 recur(2)를 호출한다. <br>
recur(2)는 2를 출력하기 전에 recur(1)을 호출하고, <br>
recur(1)은 1을 출력하기 전에 recur(0)과 recur(-1)을 출력하는데 이 둘은 실행되지 않으므로 위로 올라간다.

따라서 출력 순서는 ```1 -> 2 -> 3 -> 1 -> 4 -> 1 -> 2```  이다.


<br>

### 상향식 분석 bottom-up analysis
: 아래쪽부터 쌓아 올리며 분석하는 방법


<img width="600" alt="스크린샷 2022-02-08 오전 1 47 14" src="https://user-images.githubusercontent.com/54613024/152833116-fe842523-545f-432f-a071-6f989322acf5.png">

recur(-1)부터 시작해서 recur(4)까지 어떤 일이 일어나는지 분석하는 방법이다. </br>
recur(-1)은 아무것도 일어나지 않는다. </br>
recur(0)도 아무것도 일어나지 않는다. </br>
recur(1)은 recur(0)과 recur(-1)을 호출하고, 1을 출력한다. </br>
recur(2)는 recur(1)과 recur(0)을 호출하고, 2를 출력한다. </br>
... </br>

<br>

이런식으로 반복해서 분석하다보면 구조가 보인다. 위 그림의 화살표처럼 이전의 출력이 이후의 출력 속에 들어있는 것을 볼 수 있다.

즉, 아래부터 차근 차근 키워가며 분석하는 방법이 상향식 분석이다.



<br>

### 재귀 알고리즘의 비재귀적 표현

* 꼬리 재귀 제거하기

```python
def recur(n: int) -> int:
    """꼬리 재귀를 제거한 함수 recur"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2
x = int(input('정수값을 입력하세요.: '))

recur(x)
```

꼬리 재귀인 recur(n-2)는 n의 값을 n-2로 업데이트하고 함수의 시작 지점으로 돌아가는 것으로 동작을 바꿀 수 있다.

* 재귀를 제거하기

맨 앞에서 재귀 호출 recur(n-1)을 하기 위해서는 n값을 n - 1로 업데이트하고 함수의 시작점으로 돌아가야한다.
n값을 임시로 저장할 필요가 있기 때문에 스택을 사용하면 다음과 같이 구현할 수 있다.

```python
from stack import Stack  # stack.py의 Stack 클래스를 임포트

def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)         # n 값을 푸시
            n = n - 1
            continue
        if not s.is_empty():  # 스택이 비어 있지 않으면
            n = s.pop()       # 저장하고 있는 값을 n에 팝
            print(n)
            n = n - 2
            continue
        break

x = int(input('정수값을 입력하세요.: '))

recur(x)

```

입력 값이 4일때의 과정을 나타내면</br>
4를 푸시 -> continue 문이 실행 -> while 문 첫번째로 </br>
-> 3을 푸시 ->  continue 문이 실행 -> while 문 첫번째로 </br>
-> 2를 푸시 -> continue 문이 실행 -> while 문 첫번째로 </br>
-> 1을 푸시 -> continue 문이 실행 -> while 문 첫번째로 </br>
-> n이 0이 되어 두번 째 if문 실행 -> 1을 pop -> continue 문이 실행 -> while 문 첫번째로 </br>
-> n이 -1이 되어 두번 째 if문 실행 -> 2를 pop -> continue 문이 실행 -> while 문 첫번째로 </br>
-> n이 0이 되어 두번 째 if문 실행 -> 3을 pop -> continue 문이 실행 -> while 문 첫번째로 </br>
-> n이 1이 되어 첫번 째 if문 실행 -> 1을 푸시 -> continue 문이 실행 -> while 문 첫번째로 </br>
... </br>

이 과정을 반복하면</br>
재귀를 사용하지 않고 재귀 알고리즘을 구현할 수 있다 ! 


<br>
<br>

## 예제
### 하노이의 탑 문제
### a퀸 문제





<br>
<br>

# 참고 자료
* Bohoyoh Shibata, 이지스퍼블리싱, Doit 자료구조와 함께 배우는 알고리즘 입문
