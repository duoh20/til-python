# Day14

**문제: [큐](https://www.acmicpc.net/problem/10845)**

<br/>
<br/>

### 나의 풀이
```python
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    operation = input().rstrip()
    
    if operation == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif operation == "size":
        print(len(queue))
    elif operation == "empty":
        if len(queue) == 0:
            print('1')
        else:
            print('0')
    elif operation == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif operation == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        val = operation.split(' ')[1]
        queue.append(val)
```
