'''
<두 배열의 원소 교체>
* 문제의 기본 idea : 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체하는 것
                 * 단, 배열 A에서 가장 작은 원소가 배열 B에서 가장 큰 원소보다 작을 때에만 교체를 수행
                 * 이 과정을 K번 반복
'''

n, k = map(int, input().split()) # N과 K를 입력받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
        # 두 원소를 교체
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break
print(sum(a))
