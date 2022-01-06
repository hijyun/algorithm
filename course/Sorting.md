# 정렬 sorting
: 데이터를 특정한 기준에 따라서 순서대로 나열하는 것.

* 정렬 알고리즘으로 데이터를 정렬하면 이진 탐색 Binary Search가 가능해진다. 정렬은 이진탐색의 전처리 과정이기도 하다.
* '알고리즘의 효율성' 측면에서 정렬은 중요하다.

## 선택 정렬 selection sort

: 매번 '가장 작은 것을 선택'한다. 데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복한다.

* 선택 정렬은 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하여 정렬이 완료되는 것을 알 수 있다.
* **스와프(Swap)**: 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업. 파이썬에선 간단.
* 선택 정렬 소스 코드
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
```

### 선택 정렬의 시간 복잡도
: O(N^2)

## 삽입 정렬 insertion sort
: 삽입 정렬은 특정한 데이터를 적절한 위치에 '삽입'한다.

* 선택 정렬은 현재 데이터의 상태와 상관없이 무조건 모든 원소를 비교하고 위치를 바꾸는 반면, 삽입 정렬은 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적이다.
* 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
* 정렬이 이루어진 원소는 항상 오름차순을 유지.
* 삽입정렬 소스 코드

```python
array = [7, 5, 9 , 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
```

### 삽입정렬 시간 복잡도
* 최악의 경우 : O(N^2)
* 최선의 경우 : O(N)
* 현재 배열의 데이터가 거의 정렬이 되어 있는 상태라면 매우 빠르게 동작한다. 거의 정렬이 되어 있는 상황에서는 퀵 정렬 보다 강력.

## 퀵 정렬 quick sorting
: '기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까?' 퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다. 

* **피벗 Pivot** : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'
* 퀵 정렬을 수행하기 전에 피벗을 어떻게 설정할 것인지 미리 명시해야한다.
* 피벗을 설정하고 리스트를 분할하는 방법에 따라서 여러가지 퀵 정렬을 구분하는데, 대표적인 방식은 호어 분할 Hoare partition방식.
* **호어 분할 Hoare partition** : 리스트에서 첫 번째 데이터를 피벗으로 정한다.
* **분할Divide / 파티션 Partition** : 피벗의 왼쪽에는 피벗보다 작은 데이터가 위치하고, 피벗의 오른쪽에는 피벗보다 큰 데이터가 위치하도록 하는 작업.
* 퀵정렬 재귀함수 종료 조건 : 현재 리스트의 데이터 개수가 1개인 경우

* 퀵 정렬 소스 코드
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) - 1)
print(array)
```

* 파이썬의 장점을 살린 퀵 정렬 코드
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1: 
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

### 퀵 정렬의 시간 복잡도
* 최악의 경우 : O(N^2)
* 평균 : O(NlogN)

* 데이터가 무작위로 입력되는 경우 퀵정렬은 빠르게 동작할 확률이 높음.
* 퀵 정렬은 일반적인 경우에서 평귱적으로 빠르게 동하므로 데이터의 특성을 파악하기 어려운 경우에는 퀵정렬을 사용하는 것이 유리.
* 리스트의 가장 왼쪽 데이터를 피벗으로 삼을 때, '이미 데이터가 정렬되어 있는 경우'에는 매우 느리게 동작. (삽입 정렬과 반대)

## 계수 정렬 Count Sort
: 특정한 조건이 부합될 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘.

* 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용
* 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적
* 계수 정렬을 이용할 때는 '모든 범위를 담을 수 있는 크기의 리스트(배열)를 선언해야하기 때문
* 계수 정렬 소스코드

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분하고 등장한 횟수만큼 인덱스 출력
```

### 계수 정렬의 시간 복잡도
* 모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최댓값의 크기를 K라고 할 때,
* O(N+K)
* 최악의 경우에도 O(N+K) 보장
* 현존하는 정렬 알고리즘 중 가장 빠르다고 볼 수 있음

### 계수 정렬의 공간 복잡도
* 때에 따라서 심각한 비효율성을 초래. 
    * 데이터의 범위가 0과 999,999 단 2개가 존재할 때 -> 리스크의 크기가 100만개가 되도록 선언해야함.

## 파이썬의 정렬 라이브러리
* sorted() : 병합 정렬과 삽입 정렬의 아이디어를 더한 하이브리드 방식 사용
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 8]
result = sorted(array)
print(result)
```
* 리스트 객체 내장 함수 sort()
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 8]

array.sort()
print(array)
```
### 정렬 라이브러리의 시간 복잡도
* 최악의 경우에도 O(NlogN)을 보장

# 참고자료
* 나동빈, 이것이 취업을 위한 코딩테스트다, 한빛 미디어