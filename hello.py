# 과제1ㅣ 1부터 10까지 반복하는 과정에서 3의 배수일 경우, year를 출력하시오.
# 나머지 모든 경우는 숫자 그대로 출력

for i in range(1,21):
    if i % 3 == 0 and i != 15:
        print('year')
    elif i % 5 == 0 and i != 15:
        print('dream')
    elif i % 15 == 0:
        print('yeardream')
    else:
        print(i)
