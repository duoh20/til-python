# Day3

**문제: [모스 부호](https://www.acmicpc.net/problem/29701)**

<br/>
<br/>



### 나의 풀이
백준 문제 input 처리하는 방법을 몰라서 해맸다..  
인풋을 받아서 전처리하는 방법을 몇가지 익혀두어야할 것 같다.
```python
morse_code = {
  '.-': 'A',
  '-...': 'B',
  '-.-.': 'C',
  '-..': 'D',
  '.': 'E',
  '..-.': 'F',
  '--.': 'G',
  '....': 'H',
  '..': 'I',
  '.---': 'J',
  '-.-': 'K',
  '.-..': 'L',
  '--': 'M',
  '-.': 'N',
  '---': 'O',
  '.--.': 'P',
  '--.-': 'Q',
  '.-.': 'R',
  '...': 'S',
  '-': 'T',
  '..-': 'U',
  '...-': 'V',
  '.--': 'W',
  '-..-': 'X',
  '-.--': 'Y',
  '--..': 'Z',
  '.----': '1',
  '..---': '2',
  '...--': '3',
  '....-': '4',
  '.....': '5',
  '-....': '6',
  '--...': '7',
  '---..': '8',
  '----.': '9',
  '-----': '0',
  '--..--': ',',
  '.-.-.-': '.',
  '..--..': '?',
  '---...': ':',
  '-....-': '-',
  '.--.-.': '@'
}

N = int(input())
morse = input().split(' ')

answer = ''
for code in morse:
    answer += morse_code[code]

print(answer)
```

#### solution_1
- 첫번째 input이 숫자이므로 n에 할당하여 이 인풋을 거르고 for문을 순회함
- split()은 기본적으로 공백을 기준으로 나누므로 따로 인자를 주지 않아도 됨
- 숫자만 조합되는 케이스가 있을 수 있으므로 print시 end에 ''를 포함함
```python
x = {...모스부호...}
n = int(input())
for c in input().split():
    print(x[c], end='')
```

<br/>
<br/>

---
## 백준 사이트에서 input() 처리
```python
# 정수 받기
N = int(input())

# 문자열 받기
S = input()

# 한 줄로 넘겨진 정수를 리스트로 받기
N = list(map(int, input().split()))


# 빠르게 입력 받기
# input() 대신 sys 모듈의 readline을 사용한다.
import sys
n = int(sys.stdin.readline()) 
```

<br/>

## split()
str.split(separator, maxsplit)
- separator는 문자열을 나눌 구분자, 생략하면 공백을 기준으로 나눔
  ```python
  test = "ABC DEFG  HIJK   LMNOP"
  test.split() # => ['ABC', 'DEFG', 'HIJK', 'LMNOP']
  test.split('') # => ['ABC', 'DEFG', '', 'HIJK', '', '', 'LMNOP']
  ```
- maxsplit는 구분자로 분할할 횟수이며 생략 가능  
  ```python
  test = "1,2,3,4"
  test.split(",", 1) # => ["1", "2,3,4"]   
  ```

<br/>

## map
- 리스트, 튜플 등의 iterable한 데이터를 받아서 각각 처리하는 내장 함수이다.
- `map(function, iterable)`과 같이 인자를 받을 수 있다.  
- `map(function, iterable1, iterable2, ...)` 처럼 한 번에 여러 객체를 받아 순차적으로 처리할 수 있다.  

**특징**
- map 함수는 내부적으로 C로 구현되어 있으므로, 파이썬 반복문보다 빠르다.
- function의 인자로 람다를 사용할 수 있다.
    ```python
    test = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))
    # => [2, 4, 6, 8, 10]
    ```

