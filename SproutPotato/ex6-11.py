'''
<성적이 낮은 순서로 학생 출력하기>
* 학생의 정보가 최대 100,000개 까지 입력될 수 있으므로 최악의 경우 O(NlogN)을 보장하는 알고리즘을 이용
'''

# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력 받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 무자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end = ' ')