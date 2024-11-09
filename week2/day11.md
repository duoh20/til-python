# Day11

**문제: [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)**

<br/>
<br/>

### 나의 풀이
```python
def solution(participant, completion):
    dict = {}
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
            
    for c in completion:
        if c in dict:
            dict[c] -= 1
    
    for d in dict:
        if dict[d] == 1:
            return d
```