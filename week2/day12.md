# Day12

**문제: [스택](https://www.acmicpc.net/problem/10828)**

<br/>
<br/>

### 나의 풀이
- 처음에 시간 초과로 실패했는데,  
읽기 속도가 빠른 readline을 사용하여 해결했다.
```python
import sys

input = sys.stdin.readline
N = int(input())
    
stack = []
for _ in range(N):
    req = input().split()
        
    if req[0] == "push":
        stack.append(req[1])
    elif req[0] == "pop":
        if len(stack) < 1:
            print(-1) 
        else:
            print(stack[-1])
            stack.pop(-1)
    elif req[0] == "size":
        print(len(stack))
    elif req[0] == "empty":
        print(1) if len(stack) < 1 else print(0)
    else:
        print(-1) if len(stack) < 1 else print(stack[-1])
```

#### solution
- pop()은 마지막 원소를 리턴하면서 제거하므로 바로 print해주어도 괜찮았다.
- if arr일 때, None 뿐만 아니라 length가 0이면 False로 평가한다.
```python
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    input_list = input().split()
    if input_list[0] == "push":
        arr.append(input_list[1])
    elif input_list[0] == "pop":
        print(arr.pop() if arr else -1)
    elif input_list[0] == "size":
        print(len(arr))
    elif input_list[0] == "empty":
        print(1 if not arr else 0)
    elif input_list[0] == "top":
        print(arr[-1] if arr else -1)
```

  
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>


---
## list 함수
1. append()
   리스트 마지막에 원소를 추가
   ```python
   test = ["a", "b"]
   test.append("c") 
   print(test) # => ["a", "b", "c"]
   ```
2. insert(idx, data)  
   리스트의 원하는 위치에 원소를 추가    
   idx에 위치 인덱스(0부터 시작),  
   data에 추가할 원소를 넣음
   ```python
   test = ["a", "b"]
   test.insert(1, "c")
   print(test) # => ["a", "c", "b"]
   ```
3. pop()    
   맨 마지막 원소 리턴 후 해당 원소 제거    
   pop(idx)는 idx 위치 인덱스(0부터 시작)를 리턴하고 제거함
   ```python
   test = ["a", "b", "c"]
   test.pop() # => "c"
   print(test) # => ["a", "b"]
   
   test.pop(0) # => "a"
   print(test) # => ["b"]
   ```
4. remove(x)  
   리스트에서 첫번째로 나오는 x를 삭제       
   원소가 리스트에 존재하지 않으면 ValueError 발생
   ```python
   test = ["a", "b", "c", "d", "a", "c", "e"]
    
   test.remove("c")
   print(test) # => ['a', 'b', 'd', 'a', 'c', 'e']
   
   test.remove("b")
   print(test) # => ['a', 'd', 'a', 'c', 'e']
   
   test.remove(3) # => error! ValueError: list.remove(x): x not in list
   ```
5. reverse()  
   리스트를 역순으로 뒤집음
   ```python
   test = ["a", "c", "d", "b"]
    
   test.reverse()
   print(test) # => ['b', 'd', 'c', 'a']
   ```
6. sort()  
   원소들을 오름차순으로 정렬         
   키의 우선순위가 같을 때 기존 list의 순서를 보존하는 stable 정렬임 
   ```python
   test = ["a", "d", "b", "c"]
    
   test.sort()
   print(test) # => ['a', 'b', 'c', 'd']
   ```
6. index(x)  
   리스트에 x의 인덱스를 반환           
   원소가 리스트에 존재하지 않으면 ValueError 발생 
   ```python
   test = ["a", "b", "c"]
   test.index("c") # => 2
   ```
7. count(x)  
   x의 원소가 몇 개 있는지를 반환           
   ```python
   test = ["a", "a", "a", "b", "b", "c"]
    
   test.count("a") # => 3
   test.count("c") # => 1
   ```
      