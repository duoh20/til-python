# Day9

**문제: [민균이의 비밀번호](https://www.acmicpc.net/problem/9933)**

<br/>
<br/>

### 나의 풀이
```python
import sys, math

N = int(input())
passwords = sys.stdin.read().splitlines()
        
for password in passwords:
    if password[::-1] in passwords:
        num = len(password)
        idx = math.floor(num/2)+1
        mid = password[idx-1:idx]
        print(f"{num} {mid}")
        exit()
```

#### solution
- input을 하나씩 읽어들이며 list에 넣고 뒤집은 값이 존재하는지 비교하는 방법도 있었다.
- //로 연산하게 되면 나눗셈 후 floor 연산이 이루어진다.
```python
n=int(input())
l=list()

for i in range(n):
    p=input()     
    l.append(p)
    if p[::-1] in l:
        print(len(p), p[len(p)//2])
```

  
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>


---
## 문자열 뒤집기
1. For문 사용하기  
    ```python
    test = "abcd"
    result = ""
    for t in test:
        result += t
    # => "dcba"
    ```
2. list의 reverse() 사용  
   str을 list로 변환한 후 list의 reverse() 함수를 사용해 뒤집는다.  
   ```python
    test = "abcd"
    
    revered_test = list(test)
    revered_test.reverse()
    
    result = ''.join(revered_test)
    # => "dcba"
    ```
3. [::-1] 문자열 슬라이싱  
   str[시작:끝:규칙]에서 기본 값은 1인데, -1을 넣게되면 뒤로부터 하나씩 슬라이스하여 새 문자열을 만든다.
   ```python
   test = "abcd"
   
   revered_test = list(test)
   revered_test.reverse()
   
   result = ''.join(revered_test)
   # => "dcba"
   ```

<br/>
<br/>


## / vs // 연산자
/로 연산하면 일반적인 나눗셈,
//로 연산하면 floor 나눗셈이 된다.
```python
test1 = 5/2     # => 2.5
test1 = 5//2    # => 2
```

<br/>
<br/>


## 올림, 내림, 버림 함수
1round(n, ndigits)  
   인자로 받은 n을 지정한 소수점 자리에 맞춰 반올림함    
   n은 반올림할 숫자, ndigits는 소숫점 이하 자릿수  
   ```python
   round(3.1)           # => 3
   round(3.5)           # => 4
   round(3.141592)      # => 3
   round(3.141592, 2)   # => 3.14
   round(3.141592, 3)   # => 3.142
   ```
2. ceil(n)  
   인자로 받은 n의 올림을 구함, 정수(int)를 반환함
   ```python
   import math
   math.ceil(1.0)    # => 1
   math.ceil(1.1)    # => 2 
   math.ceil(2.5)    # => 3
   math.ceil(-2.2)   # => -2
   math.ceil(-3.0)   # => -3
   ```
3. floor(n)  
   인자로 받은 n의 내림을 구함, 정수(int)를 반환함
   ```python
   import math
   math.floor(1.0)   # => 1
   math.ceil(1.1)    # => 1 
   math.ceil(2.5)    # => 2
   math.ceil(-2.0)   # => -2
   math.ceil(-2.6)   # => -3
   ```
4. trunc(n)  
   인자로 받은 n을 0에 가까운 정수로 반환     
   ```python
   import math
   math.trunc(3.1)           # => 3
   math.trunc(-3.1)          # => -3
   math.trunc(-4.6)          # => -4
   ```