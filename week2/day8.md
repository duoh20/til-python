# Day8

**문제: [근무 지옥에 빠진 푸앙이 (Small)](https://www.acmicpc.net/problem/25593)**

<br/>
<br/>



### 나의 풀이  
```python
weeks = int(input())
hours = [4, 6, 4, 10]
  
workers = {}
for _ in range(weeks):
    for hour in range(4):
        row = input().split()
        for worker in row:
          if worker != '-':
            if worker in workers:
                workers[worker] += hours[hour]
            else:
                workers[worker] = hours[hour]
  
if len(workers) == 0 or max(workers.values()) - min(workers.values()) <= 12:
    print('YES')
else:
    print('NO')
```



<br/>
<br/>
