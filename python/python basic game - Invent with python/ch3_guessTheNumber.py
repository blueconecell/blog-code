# 랜덤으로 숫자를 만들어주기 위해서 random을 불러오고 1~20사이의 숫자를 변수에 저장한다.
import random
guessNum = random.randint(1, 20)

# 인트로 부분이다.
print('Hello! What is your name?')
name = input()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')

# while무한 반복문으로 추측하는 과정을 만든다. 
limit = 0
while True:

    # 6회안에 맞추도록 반복문을 제한한다.    
    if limit==6:
        break
    limit+=1    

    print('Take a guess.')
    num = int(input())
    if num == guessNum:
        print(f'Good job, {name}! You guessed my number in {limit} guesses')
        break
    elif num > guessNum:
        print('Your guess is too high')
    else:
        print('Your guess is too low')