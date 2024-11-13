import time 

def countdownTimer():
    seconds = int(input("Enter the number for the countdown:"))

    while seconds >0:
        print(f"Time Left: {seconds} sec")
        time.sleep(1)
        seconds -= 1
    print("Time's UPP!")

countdownTimer()
