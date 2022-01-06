def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    print(queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        print(cur)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            print(answer)
            if cur[0] == location:
                return answer



if __name__ == "__main__":
    ans = solution([1, 3, 2, 2], 0)
    print("출력 순서는 ===>", ans)