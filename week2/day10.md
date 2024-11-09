# Day10

**문제: [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845)**

<br/>
<br/>

### 나의 풀이
```python
def solution(nums):
    # N마리 중 /2 가져갈 수 있음
    numbers_get = len(nums)/2
    kinds = set(nums)
    
    if numbers_get > len(kinds):
        return len(kinds)
    else:
        return numbers_get
```

#### solution
- 중복을 제거한 종류의 수와 가져갈 수 있는 수 min()을 사용해 표현할 수 있다.
```python
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
```

  
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>


---
## min(itrerable)
반복 가능한 매개 변수를 인수로 받아 이 중 최소값을 찾아서 반환    
1. min(itrerable)
    ```python
    test = [1,2,3]
    min(test)   # => 1
     
    test = 'Python'
    min(test)   # => P
    
    test = (1, 2, 'a', 'b')
    min(test)   # => error! str과 int 비교 불가
    ```
2. min(arg1, arg2)
    ```python
    a = [1, 2, 3]
    b = [4, 5, 6]
    min(a, b)   # => [1, 2, 3]
    ``` 

<br/>
<br/>

## max(iterable)
반복 가능한 매개 변수를 인수로 받아 이 중 최대값을 찾아서 반환   
1. max(itrerable)
    ```python
    test = [1,2,3]
    max(test)   # => 3
     
    test = 'Python'
    max(test)   # => y
    
    test = (1, 2, 'a', 'b')
    max(test)   # => error! str과 int 비교 불가
    ```
2. max(arg1, arg2)
    ```python
    a = [1, 2, 3]
    b = [4, 5, 6]
    max(a, b)   # => [4, 5, 6]
    ``` 
<br/>
<br/>
