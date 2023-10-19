#1000 이하의 소수를 나열하기 (개선1)

couter = 0
prt = 0
prime = [None]*500

prime[prt] = 2
prt += 1

for n in range(3, 1001, 2) :
    for i in range(1,prt) :
        couter+=1
        if n%prime[i] == 0 :
            break
    else :
        # prime.append(n)
        prime[prt] = n
        prt +=1

for i in range(prt) :
    print(prime[i], end='')

