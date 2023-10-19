from typing import Any, Sequence
import copy

def seq_search (seq:Sequence, key) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True :
        if a[i] == key :
            break
        i+= 1

    return -1 if i==len(seq) else i

if __name__ == '__main__' :
    num = int(input('원소 수:'))
    x =[]

    for i in range(num) :
        s= int(input(f'x[{i}] : '))
        x.append(s)


ky = int(input('검색할 값:'))

idx = seq_search(x,ky)

if idx == -1 :
    print('없음')
else :
    print(f'검색값의 위치는 x[{idx}]')
        