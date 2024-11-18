# Day20

**문제: [N번째 큰 수](https://www.acmicpc.net/problem/2075)**

<br/>
<br/>

### 나의 풀이
- 최소힙은 작은 값부터 정렬하므로 -1을 곱하여 정렬한다.
- 메모리 제한으로 실패하므로 힙 사이즈를 N으로 제한한다.
    ```python
    import sys, heapq
    input = sys.stdin.readline
    
    N = int(input())
    hq = []
    for _ in range(N):
        for a in map(int, input().split()):
            if len(hq) < N:
                heapq.heappush(hq, a)
            else:
                if a > hq[0]:
                    heapq.heappushpop(hq, a)
        
    print(hq[0]) 
    ```