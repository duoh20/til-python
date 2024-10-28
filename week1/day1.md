# Day1

**문제: [문자열 내 p와 y의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/12916)**

<br/>
<br/>

### 나의 풀이
```python
def solution(s):
    test = s.lower()
    count_p = test.count('p')
    count_y = test.count('y')
    return True if count_p == count_y else False
```

#### solution_1 
return True if count_p == count_y else False 
대신 return count_p == count_y로 줄일 수 있었음

#### solution_2 
return s.lower().count('p') == s.lower().count('y')로 축약 가능

  
<br/>
<br/>
<br/>


## 함수
### count()
문자열의 개수 혹은 list 원소의 개수를 세는 함수  
튜플, 리스트와 같은 iterable한 자료형에서도 사용 가능함  

```python
# 문자열
'ppython'.count('py')  # => 1

# 리스트
['pp', 'py', 'p y', 'thon'].count('py') # => 1
```