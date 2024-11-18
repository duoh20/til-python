# Day17

**문제: [식당 입구 대기 줄](https://www.acmicpc.net/problem/26042)**

<br/>
<br/>

### 나의 풀이
- 아래 코드로 시간 초과 발생
```python
max_line, min_id = 0, 0
students = []
for i in range(N):
    item = input()
        
    if item == "2":
        students.pop(0)
    else:
        students.append(int(item.split()[1]))
            
        if max_line < len(students):
            max_line = len(students)
            min_id = students[-1]
        elif max_line == len(students):
            min_id = min(min_id, students[-1])
            
print(f"{max_line} {min_id}")
```