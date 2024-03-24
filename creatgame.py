import random
number = random.randint(1, 1000)
tries = 0
n = 10

print("1~1000 사이의 숫자를 맞춰보세요")

while tries <= n:
    guess = int(input("숫자를 입력하세요: "))
    tries += 1
    if guess == number:
        print("정답입니다. 총 시도 횟수는 {}입니다".format(tries))
        break
    elif guess < number:
        print("더 큰 수를 입력하세요")
    elif guess > number:
        print("더 작은 수를 입력하세요")
if tries > n:
    print("총 시도 횟수를 증가하였습니다. 정답은 {}입니다".format(number))