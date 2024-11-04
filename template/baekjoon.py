import sys
from io import StringIO


def inputIO():
    # 입력 데이터 추가
    test = """ {add input} """
    sys.stdin = StringIO(test)


def solution():
    # 답안 작성
    num = int(input())


inputIO()
solution()