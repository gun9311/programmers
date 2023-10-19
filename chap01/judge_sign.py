#입력받은 정수의 부호 출력하기

n= int(input('정수를 입력하세요. : '))

if n > 0 :
    print("양의 정수입니다.")
elif n < 0:
    print("음의 정수입니다")
else :
    print("0입니다.")