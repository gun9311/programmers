N = int(input())

first_N = N
count = 0

while True:
    sip = N // 10
    il = N % 10
    total = sip + il
    new_N = (il * 10) + (total % 10)

    count += 1

    if new_N == first_N:
        break

    N = new_N

print (count)




