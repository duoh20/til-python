# Day19

**문제: [최소힙](https://www.acmicpc.net/problem/1927)**

<br/>
<br/>

### 나의 풀이
- 시간 초과가 발생한 코드
    ```python
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    heap = []
    
    for _ in range(N):
        num = int(input())
        
        if num < 1:
            if len(heap) > 0:
                last = min(heap)
                print(last)
                heap.remove(last)
            else:
                print(0)
        else:
            heap.append(num)
  ```
- heapq라는 모듈을 사용하여 시간초과 문제 해결
  ```python
  import sys, heapq
  input = sys.stdin.readline
  
  N = int(input())
  heap = []
  
  for _ in range(N):
      num = int(input())
          
      if num == 0:
          if not heap:
              print(0)
          else:
              print(heapq.heappop(heap))
      else:
        heapq.heappush(heap, num)
  ```