import random
import time

def intro():
    print('''
    용으로 가득한 땅에 도착했습니다. 당신 앞에 두개의 동굴이 보입니다.
    한 동굴에서 용은 당신에게 우호적이며 보물을 줄 것입니다.
    하지만 다른 용은 탐욕스럽고 배고파서 당신을 보자마자 잡아먹을 것입니다.
    ''')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('어느 동굴로 들어가고 싶습니까? (1 또는 2)')
        cave = input()
    return cave

def checkCave(cave):

    print('동굴에 들어가고 있습니다...')
    time.sleep(2)
    print('어두컴컴하고, 이상합니다...')
    time.sleep(2)
    print("커다란 용이 당신앞에 나타났습니다! 용이 입을 벌리고...")
    print('\n')
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    if cave == str(friendlyCave): # input으로 입력받은 입력값은 문자이다.
        print('용이 당신에게 보물을 줬습니다!')
    else:
        print('용이 당신을 밀치고 깨물었습니다!')
    
# 게임 시작
play = 'yes'
while True:
    if play == 'yes' or play == 'y':
        intro()
        cave = chooseCave()
        checkCave(cave)

        print('다시 플레이 하시겠습니까? (yes or no)')
        play = input()
    else:
        break
