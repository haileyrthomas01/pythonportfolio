import time

secs = input('Enter time in seconds: ')

while True:
    try:
        secs = int(secs)
        break
    except:
        secs = input('Please enter a number: ')

while secs > 0:
    print(secs)
    secs -= 1
    time.sleep(1)

print('Time expired')
