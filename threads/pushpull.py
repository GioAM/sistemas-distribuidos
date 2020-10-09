import time
import random
import sys


def push():
    tempo = time.time()
    time.sleep(random.randint(0, 5))
    if int(time.time() - tempo) >= 5:
        print("Processo com erro")
        sys.exit()
    print("I am alive")


def pull():
    print("Are you alive??")
    push()
    time.sleep(1)


while True:
    pull()