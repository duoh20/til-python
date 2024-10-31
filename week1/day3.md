# Day3

**문제: [문자열 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/140108)**

<br/>
<br/>

### 나의 풀이
```python
def solution(s):
    xcnt = None
    other_cnt = 0
    word = ""
    words = list()
    
    for s in list(s):
        if not xcnt:
            xcnt = 0
            x = s
        
        word += s
        if x is s:
            xcnt += 1 
        else: 
            other_cnt += 1
        
        if xcnt == other_cnt:
            words.append(word)
            xcnt = None
            other_cnt = 0
            word = ""
    
    if word:
        words.append(word)
        
    return len(words)
```

#### solution_1
```python
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer
```

#### solution_2
Queue를 사용한 접근
```python
from collections import deque
def solution(s):

    ans = 0

    q = deque(s)    
    while q:
        a, b = 1, 0
        x = q.popleft()    

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return ans
```

  
<br/>
<br/>
<br/>
