# Day15

**문제: [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906)**

<br/>
<br/>

### 나의 풀이
```python
def solution(arr):
    answer = []
    prev = ''
    for a in arr:
        if prev != a:
            answer.append(a)
            prev = a

    return answer
```


#### solution
- a 리스트에 담긴 가장 마지막 원소와 같은 값이 아니면 되니  
list[-1]으로 마지막 원소를 가져와 가져와 비교하는 방법이 있었다..!
```python
def solution(arr):
    result = []
    for c in arr:
        if len(result) == 0 or result[-1] != c:
            result.append(c)

    return result
```
