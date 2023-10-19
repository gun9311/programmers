#seq_search() 함수를 사용하여 실수 검색하기
from ssearch_while import seq_searchh

print('실수를 검색합니다')
print('End를 입력하면 종료합니다')

number = 0
x=[]

while True :
    s = input(f'x[{number}]:')
    if s == 'End' :
        break
    x.append(float(s))
    number += 1

ky = float(input('검색할 값:'))

idx = seq_searchh(x, ky)
if idx == -1 :
    print('없음')
else :
    print(f'검색값은 x[{idx}]')