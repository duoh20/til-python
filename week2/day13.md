# Day13

**문제: [단어 순서 뒤집기](https://www.acmicpc.net/problem/12605)**

<br/>
<br/>

### 나의 풀이
```python
import sys

input = sys.stdin.readline
N = int(input())

for n in range(N):
    L = input().split()
    L.reverse()
    print(f"Case #{n+1}: {' '.join(L)}")
```

#### solution
- list[::-1]을 -1 간격으로 이동하며, 원소를 뒤로 뒤집을 수도 있다.
```python
for i in range(int(input())):
    c = input().split()
    print(f"Case #{i+1}: {' '.join(c[::-1])}")
```