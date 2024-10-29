# Day2

**문제: [크기가 작은 부분 문자열](https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3)**

<br/>
<br/>

### 나의 풀이
```python
def solution(t, p):
    idx = 0
    step = len(p)
    answer = 0
    while idx + step <= len(t):
        answer += 1 if int(t[idx:idx+step]) <= int(p) else 0
        idx += 1
    return answer
```

#### solution
문자열 대비 순회 가능한 횟수 만큼 for ... range 구문을 사용해 반복했다면    
불필요한 index 변수 선언을 하지 않고 가독성도 개선되었을 것이다.
```python
# best answer
answer = 0
for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1
```

  
<br/>
<br/>
<br/>


## string slice
파이썬에서 제공하는 부분 문자열로 slicing하는 방법을 알아본다.

#### 1. str[start:end:step]
start: 0부터 시작하는 부분 문자열의 시작 인덱스  
end: 부분 문자열의 마지막 인덱스 (이 인덱스에서 -1한 만큼 추출함)  
step: 특정 간격으로 문자 추출

```python
test = 'apple computer'

test[:3] #   => ap      (test[0:3]과 동일)
test[-1] #   => r       (마지막 문자 추출)
test[6:-3] # => compu   (6번째 문자 부터 마지막 3개 제외한 문자 추출)
test[::2]  # => alcpe   (두 칸 간격 추출)
```