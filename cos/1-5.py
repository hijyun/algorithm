def solution(n):
	answer = 0
	point = 1
	if n % 2 != 0:
		answer += (n ** 2)
	while n > 1:
		answer += ((point * 2) + ((n-1) * 2))
		point += ((n-1) * 4)
		n -= 2
	return answer