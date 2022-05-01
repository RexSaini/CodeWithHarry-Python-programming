#Exercise7
#Healthy Programmer
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    w_sec = 40*60
    ex_sec = 30*60
    eyes_sec = 45*60

    while True:
        if time() - init_water > w_sec:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at:")

        if time() - init_eyes >eyes_sec:
            print("Eye exercise time. Enter 'done' to stop the alarm.")
            musiconloop('eyes.mp3', 'done')
            init_eyes = time()
            log_now("Eyes Relaxed at:")

        if time() - init_exercise > ex_sec:
            print("Physical Activity Time. Enter 'done' to stop the alarm.")
            musiconloop('physical.mp3', 'done')
            init_exercise = time()
            log_now("Physical Activity done at:")