# count down timer
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # divmod() returns (minutes, seconds)
        timeformat = f'{mins:02d}:{secs:02d}'  # f-string used here

        print(timeformat, end='\r')  # print the time in the same line
        time.sleep(1)
        seconds -= 1
    print("Time's up!")  # print when the time is up

countdown = int(input("Enter the time in seconds: "))  # take input from user
countdown_timer(countdown)  # call the countdown timer function
