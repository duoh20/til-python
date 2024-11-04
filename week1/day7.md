# Day7

**문제: [전주 듣고 노래 맞히기](https://www.acmicpc.net/submit/31562/85997357)**

<br/>
<br/>



### 나의 풀이  
```python
n, m = map(int, input().split())

song_list = {}
for _ in range(n):
    song = input().split()
    sound = ''.join(song[2:5])

    if sound in song_list:
        song_list[sound] = '?'
    else:
        song_list[sound] = song[1]

for _ in range(m):
    sound = ''.join(input().split())

    if sound in song_list:
        print(song_list[sound])
    else:
        print('!')
```



<br/>
<br/>
