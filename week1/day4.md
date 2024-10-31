# Day3

**[문제1](#숫자-문자열과-영단어-): [숫자 문자열과 영단어](https://school.programmers.co.kr/learn/courses/30/lessons/81301)**  
**[문제2](#의상-): [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)**

<br/>
<br/>


## 숫자 문자열과 영단어: 
### 나의 풀이
- s를 순환하면서 문자열을 바꾸는 것보다는 matches.items()를 사용해 순환하면서  
단어에 대응하는 문자열을 숫자로 replace() 해주는 편이 좋았을텐데... 생각을 못했다.
```python
def solution(s):
    matches = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    
    answer = '' 
    word = ''
    for alpha in s:
        if alpha.isdigit():
            answer += alpha
        else:
            word += alpha
            if word in matches:
                answer += matches[word]
                word = ''
        
    return int(answer)
```

#### solution_1
- 단어와 숫자를 리스트에 넣고 index를 사용해 숫자로 치환하는 방법이 있었다..!
- replace 함수를 사용해 단어에 대응하는 숫자로 문자열을 대치할 수 있었다..!.
```python
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
```

  
<br/>
<br/>
<br/>


---
## 의상: 
### 나의 풀이
```python
def solution(clothes):
    c_list = {}
    for clothe in clothes:
        if clothe[1] in c_list:
            c_list[clothe[1]].append(clothe[0])
        else:
            c_list[clothe[1]] = [clothe[0]]
    
    answer = 1
    for item in c_list.values():
        answer *= (len(item) + 1)
    
    return answer - 1
    # 옷을 입지 않는 경우가 있어 -1
```
- 연속된 배열의 숫자를 곱하는 방법: 초기값을 1로 셋팅하여 배열의 원소를 순차적으로 곱한다.

### solution
```python
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
```
