# Day6

**문제: [할리갈리](https://www.acmicpc.net/problem/27160)**

<br/>
<br/>



### 나의 풀이  
```python
N = int(input())
fruits = {}

for i in range(N):
    fruit, cnt = input().split()
    if fruit in fruits:
        fruits[fruit] += int(cnt)
    else:
        fruits[fruit] = int(cnt)

print('YES') if 5 in fruits.values() else print ('NO')
```
- n번씩 인풋이 따로 들어오기 때문에 처음 주어진 인풋의 총량만큼 순회하여 과일을 셀 수 있도록 했어야했다.
- 과일의 종류가 정해져있는 상태이므로 fruits를 미리 정의하여 코스트를 줄일 수 있었다.


#### solution_1
- readline을 사용하여 빠르게 읽어왔다.
- 정해진 과일을 미리 정의한 후 set을 사용해 5가 있는지 확인했다.
```python
import sys

input = sys.stdin.readline
dic = dict(zip(("STRAWBERRY", "BANANA", "LIME", "PLUM"), (0, 0, 0, 0)))
for i in range(int(input())) :
    inp = input().split()
    dic[inp[0]] += int(inp[1])

print(["NO", "YES"][5 in set(dic.values())])
```

<br/>
<br/>
