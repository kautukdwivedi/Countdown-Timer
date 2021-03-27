import time

def countdown(t):
    while t:
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(2)
        t-=1
    print("Timer Completed")

t = input("Enter amount of time :- ")

countdown(int(t))
