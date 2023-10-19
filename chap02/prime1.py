#1000이하의 소수 나열하기

counter = 0
number = 0

for n in range(2, 1001) :
    for i in range(2, n) :
        number += 1
        if n %i == 0 :
            break
    else :
        counter += 1

print(counter)
print(number)
            