from max import max_of

print('배열의 최댓값을 구합니다.')
print('End를 입력하면 종료됩니다')

number = 0
x = []

while True:
    s = (input(f"x[{number}]입력 : "))
    if s == 'End' :
        break
    x.append(int(s)) 
    number += 1

print(f'배열의 갯수는 {number}')
print(f'배열의 최댓값은 {max_of(x)}입니다')