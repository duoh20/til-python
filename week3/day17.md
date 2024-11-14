# Day17

**문제: [기술 연계마스터 임스](https://www.acmicpc.net/problem/25497)**

<br/>
<br/>

### 나의 풀이
```python
N = int(input())

answer = 0
skills = []

for skill in input():
    if skill in ['L','S']:
        skills.append(skill)
    elif skill == 'R':
        if 'L' in skills:
            skills.remove('L')
            answer += 1
        else:
            break
    elif skill == 'K':
        if 'S' in skills:
            skills.remove('S')
            answer += 1
        else:
            break
    else:
        answer += 1
```