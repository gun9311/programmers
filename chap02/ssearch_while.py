#While문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_searchh(a:Sequence, key:Any) -> int:

    i = 0

    while True :
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i+= 1

if __name__ == "__main__" :
    num =int(input("원소 수 :"))
    x = [None] * num

    for i in range(num) :
        x[i] = int(input(f'x[{i}]:'))
ky = int(input('검색할 값:'))
idx = seq_searchh(x, ky)

if idx == -1:
    print('찾기 실패')
else :
    print(f'검색값은 x[{idx}]')
