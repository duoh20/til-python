# Day16

**문제: [카드1](https://www.acmicpc.net/problem/2161)**

<br/>
<br/>

### 나의 풀이
```python
nums = list(i+1 for i in range(int(input())))
while len(nums) > 1:
    print(nums.pop(0))
    nums.append(nums.pop(0))
print(nums[0])
```