print('a부터 b까지 정수의 합을 구합니다')
a= int(input('첫 수 입력하세요 :  '))
b= int(input('끝 수 입력하세요 :  '))

if a>b :
    a,b = b,a

total_sum =0
for i in range(a,b+1) : 
    total_sum += i

print(f'{a}부터 {b}까지의 합은 {total_sum} 입니다.')
