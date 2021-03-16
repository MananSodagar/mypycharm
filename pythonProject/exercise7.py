from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def mylog(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} on {datetime.now()}\n")
if __name__=="__main__":
    # musicloop("water.mp3","drank")
    int_water = time()
    int_eye = time()
    int_exercise = time()

    watsec=5
    eyesec=10
    excsec=15
while True:
    if (time()-int_water>5):
        print("water drinking time. enter stop to deactivate")
        musicloop("water.mp3","stop")
        int_water = time()
        mylog("i drank water ")
    if (time() - int_eye > 10):
        print("eye blinking time. enter stop to deactivate")
        musicloop("eating.mp3", "stop")
        int_eye = time()
        mylog("i blink ")
    if (time() - int_exercise > 15):
        print("exercising time. enter stop to deactivate")
        musicloop("exercise.mp3", "stop")
        int_exercise = time()
        mylog("i excercise ")