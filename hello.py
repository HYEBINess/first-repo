# 과제1ㅣ 1부터 10까지 반복하는 과정에서 3의 배수일 경우, year를 출력하시오.
# 나머지 모든 경우는 숫자 그대로 출력
# 3의 배수를 먼저 해주는 것이 효율이 좋음
# 읽어야 하는 라인의 수를 줄이는 것이 중요
# 배수 갯수가 많은 순서대로 쳐주는게 구문을 빨리 탈출하는 방법 
for i in range(1,21):
    if i % 3 == 0 and i != 15:
        print('year')
    elif i % 5 == 0 and i != 15:
        print('dream')
    elif i % 15 == 0:
        print('yeardream')
    else:
        print(i)
