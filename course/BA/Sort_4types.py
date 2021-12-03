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

def findMinIdx(ary) :
	minIdx = 0
	for i in range(1, len(ary)) :
		if (ary[minIdx] > ary[i] ) :
			minIdx = i
	return minIdx

testAry = [55, 88, 33, 77, 11]
minPos = findMinIdx(testAry)
print(minPos)
print('최솟값 -->', testAry[minPos])

## 전역 변수 선언 부분 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분 ##
print('정렬 전 -->', before)
for _ in range(len(before)) :
	minPos = findMinIdx(before)
	after.append(before[minPos])
	del(before[minPos])
print('정렬 후 -->', after)


## 함수 선언 부분 ##
def selectionSort(ary) :
	n = len(ary)
	for i in range(0, n-1) :
		minIdx = i
		for k in range(i+1, n) :
			if (ary[minIdx] > ary[k]) :
				minIdx = k
		tmp = ary[i]
		ary[i] = ary[minIdx]
		ary[minIdx] = tmp

	return ary

## 전역 변수 선언 부분 ##
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]


## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)


# +
def findInsertIdx(ary, data) :
	findIdx = -1			# 초깃값은 없는 위치로
	for i in range(0, len(ary)) :
		if (ary[i] > data ) :
			findIdx = i
			break
	if findIdx == -1 :			# 큰 값을 못찾음 == 제일 마지막 위치
		return len(ary)
	else :
		return findIdx

testAry = []
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 -->' , insPos)

testAry = [33, 77, 88]
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 -->' , insPos)

testAry = [33, 55, 77, 88]
insPos = findInsertIdx(testAry, 100)
print('삽입할 위치 -->' , insPos)


# -

## 함수 선언 부분 ##
def findInsertIdx(ary, data) :
	findIdx = -1			# 초깃값은 없는 위치로
	for i in range(0, len(ary)) :
		if (ary[i] > data ) :
			findIdx = i
			break
	if findIdx == -1 :			# 큰 값을 못찾음 == 제일 마지막 위치
		return len(ary)
	else :
		return findIdx

# +
## 전역 변수 선언 부분 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분 ##
print('정렬 전 -->', before)
for i in range(len(before)) :
	data = before[i]
	insPos = findInsertIdx(after, data)
	after.insert(insPos, data)
print('정렬 후 -->', after)


# -

## 함수 선언 부분 ##
def insertionSort(ary) :
	n = len(ary)
	for end in range(1, n) :
		for cur in range(end, 0, -1) :
			if ( ary[cur-1] > ary[cur] ) :
				ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
	return ary

# +
## 전역 변수 선언 부분 ##
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = insertionSort(dataAry)
print('정렬 후 -->', dataAry)


# -

## 함수 선언 부분 ##
def BubbleSort(ary) :
	n = len(ary)
	for end in range(n-1, 0, -1) :
		for cur in range(0, end) :
			if (ary[cur] > ary[cur+1]) :
				ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
	return ary

# +
## 전역 변수 선언 부분 ##
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = BubbleSort(dataAry)
print('정렬 후 -->', dataAry)


# -

## 함수 선언 부분 ##
def bubbleSort(ary) :
	n = len(ary)
	for end in range(n-1, 0, -1) :
		changeYN = False
		print('#사이클-->', ary)
		for cur in range(0, end) :
			if (ary[cur] > ary[cur+1]) :
				ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
				changeYN = True
		if not changeYN :
			break
	return ary

# +
## 전역 변수 선언 부분 ##
dataAry = [50, 105, 120, 188, 150, 162, 168, 177]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = bubbleSort(dataAry)
print('정렬 후 -->', dataAry)


# -

## 함수 선언 부분 ##
def quickSort(ary) :

	n = len(ary)
	if n <= 1 : # 정렬할 리스트의 개수가 1개 이하면
		return ary
	
	pivot = ary[n // 2]   # 기준값을 중간값으로 지정
	leftAry, rightAry = [], []

	for num in ary :
		if num < pivot :
			leftAry.append(num)
		elif num > pivot :
			rightAry.append(num)

	return quickSort(leftAry) + [pivot] + quickSort(rightAry)

# +
## 전역 변수 선언 부분 ##
dataAry = [188, 150, 168,  162, 105, 120,  177,  50]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)

# +
## 전역 변수 선언 부분 ##
dataAry = [188, 150, 168,  162, 105, 120,  177,  50, 150, 120]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)


# -

## 함수 선언 부분 ##
def quickSort(ary) :
	n = len(ary)
	if n <= 1 :		# 정렬할 리스트의 개수가 1개 이하면
		return ary

	pivot = ary[n // 2] 	# 기준값을 중간 값으로 지정
	leftAry, midAry, rightAry = [], [], []

	for num in ary :
		if num < pivot :
			leftAry.append(num)
		elif num > pivot :
			rightAry.append(num)
		else :
			midAry.append(num)

	return quickSort(leftAry) + midAry + quickSort(rightAry)

# +
## 전역 변수 선언 부분 ##
dataAry = [120, 120, 188, 150, 168, 50, 50, 162, 105, 120,  177,  50]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)


# +
## 함수 선언 부분 ##
def qSort(arr, start, end) :
	if end <= start :
		return

	low = start
	high = end

	pivot = arr[(low + high) // 2]  # 작은 값은 왼쪽, 큰 값은 오른쪽으로 분리한다.
	while low <= high :
		while arr[low] < pivot :
			low += 1
		while arr[high] > pivot :
			high -= 1
		if low <= high :
			arr[low], arr[high] = arr[high], arr[low]
			low, high = low + 1, high - 1

	mid = low

	qSort(arr, start, mid-1)
	qSort(arr, mid, end)

def quickSort(ary) :
	qSort(ary, 0, len(ary)-1)

# +
## 전역 변수 선언 부분 ##
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
quickSort(dataAry)
print('정렬 후 -->', dataAry)

# -


