import time

timer = int(input("Enter the timer here: "))

while timer >= 0:
    print(timer)
    timer -= 1
    time.sleep(1)

print("Time's up")