import random
from max import max_of

print('난수의 최댓값을 구합니다')
num =int(input("난수의 개수:"))
lo =int(input("최소:"))
hi   =int(input("최대:"))

x = [None] * num

for i in range(num) :
    x[i] = random.randint(lo, hi)
    # s = random.randint(lo, hi)
    # x.append(s)

print(f'최댓값은 {max_of(x)}')