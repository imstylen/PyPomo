import time
import os
from playsound import playsound

worked = 0;

def tick(i,length,type):
    os.system("cls")
    print("worked: {}".format(worked))
    print("")
    print(type)
    print(length - i)

    if i == length/2:
        playsound("2 beep.wav", block = False)
    if i == length - 5:
        playsound("1 beep.wav", block = False)

    if i == length:
        playsound("alarm.wav", block = False)
        return
    else:
        time.sleep(1)
        tick(i+1,length,type)

if __name__ == "__main__":

    work_length = 25*60;
    small_break_length = 5*60;
    long_break_length = 20*60;

    while True:
        tick(0,work_length,"Work")
        worked = worked + 1
        tick(0,small_break_length,"Small Break")
        tick(0,long_break_length,"Long Break")
