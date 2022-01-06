# 탐색
범위를 반씩 좁혀가는 탐색
## 순차 탐색 Sequential Search
: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

* 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용
* 리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 데이터를 찾을 수 있음.
* 순차 탐색 소스코드
```python
  # 순차 탐색 소스코드 구현
  def sequential_search(n, target, array):
      # 각 원소를 하나씩 확인하며
      for i in range(n):
          # 현재의 원소가 찾고자 하는 원소와 동일한 경우
          if array[i] == target:
              return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)
  
  print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
  input_data = input().split()
  n = int(input_data[0]) # 원소의 개수
  target = input_data[1] # 찾고자 하는 문자열
  
  print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
  array = input().split()
  
  # 순차 탐색 수행 결과 출력
  print(sequential_search(n, target, array))
```

### 순차 탐색의 시간 복잡도
: O(N)

## 이진 탐색 Binary Search
* 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
* 데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다는 특징.
* 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징.
* 이진 탐색은 위치를 나타내는 변수 3개-시작점, 끝점, 중간점 를 사용. 
* 찾으려는 데이터와 중간점 Middle 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는다.

* 재귀 함수로 구현한 이진 탐색 소스코드
```python
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)가 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

* 반복문으로 구현한 이진 탐색 소스코드
```python
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탬색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

### 이진 탐색 시간 복잡도
: O(logN)
* 이진 탐색은 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다.

# 참고자료
* 나동빈, 이것이 취업을 위한 코딩테스트다, 한빛 미디어