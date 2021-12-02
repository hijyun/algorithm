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

def isQueueFull() :
	global SIZE, queue, front, rear
	if ( rear == SIZE-1) :
		return True
	else :
		return False


def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False


def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		print("큐가 꽉 찼습니다.")
		return
	rear += 1
	queue[rear] = data


def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None
	return data


def peek() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	return queue[front + 1]

## 전역 변수 선언 부분 ##
SIZE = int(input("큐의 크기를 입력하세요 ==> "))
queue = [ None for _ in range(SIZE) ]
front = rear = 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
	select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	while (select != 'X' and select != 'x') :
		if select=='I' or select =='i' :
			data = input("입력할 데이터 ==> ")
			enQueue(data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		elif select=='E' or select =='e' :
			data = deQueue()
			print("추출된 데이터 ==> ", data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		elif select=='V' or select =='v' :
			data = peek()
			print("확인된 데이터 ==> ", data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		else :
			print("입력이 잘못됨")

		select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	print("프로그램 종료!")



