# your code goes here!
import time

def countdown(num):
    x=num
    while x>0:
        print(f"{ x } SECOND(S)!")
        x-=1
    print("HAPPY NEW YEAR!")

print(countdown(10))

def countdown_with_sleep(num):
    x=num
    while x>0:
        print(f"{x} SECOND(S)!")
        time.sleep(1)
        x-=1
    print("HAPPY NEW YEAR!")

print(countdown_with_sleep(10))
