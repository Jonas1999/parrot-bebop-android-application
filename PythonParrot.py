import keyboard
import olympe
import sys
import time
import os.path
from time import perf_counter
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
from termios import tcflush, TCIFLUSH

text = "stuff"
done = False#for main while loop
piloting = False#for piloting while loop
duration = 0.1
speed = 100
nspeed = speed - speed - speed
cMode = False#regular input or replay
recording = False
rewind = []
recCurrent = 0

# drone = olympe.Drone("192.168.42.1")#real bebop2 drone
drone = olympe.Drone("10.202.0.1")#simulated anafi4k drone
drone.connection()
# olympe.Drone.get_state(): get the current drone state

while(done == False):#numlock needs to be on
    tcflush(sys.stdin, TCIFLUSH)#flush input buffer
    text = keyboard.read_key()
    if text == 'c':#for reconnection
        #drone = olympe.Drone("192.168.42.1")#real bebop2 drone
        drone = olympe.Drone("10.202.0.1")#simulated anafi4k drone
        drone.connection()
    if text == 't':
        print("takeoff function")
        drone(TakeOff()).wait()
    elif text == 'l':
        print("landing function")
        drone(Landing()).wait()
    elif text == 'q':
        print("quitting")
        done = True
    elif text == 'p':
        drone.start_piloting()
        piloting = True
        while(piloting == True):
            if recording == True:
                stime = perf_counter()
            if cMode == False:#regular input
                text = keyboard.read_key()
                tcflush(sys.stdin, TCIFLUSH)#flush input buffer
            elif cMode == True:#playback
                time.sleep(rtime)
                if rewind[recCurrent] == ">":
                    temp = ""
                    recCurrent += 1
                    while rewind[recCurrent] != "<":
                        temp += rewind[recCurrent]
                        recCurrent += 1
                    rtime = float(temp)
                text = rewind[recCurrent]
                recCurrent += 1
                if recCurrent == len(rewind) or recCurrent > len(rewind):
                    cMode = False
            if text == "8":#numpad 8
                print("forward movement")
                drone.piloting_pcmd(0, speed, 0, 0, duration)#drone.piloting_pcmd(roll, pitch, yaw, gaz, duration(seconds)) ints between -100 and 100
                if(recording == True):
                    rec.write(text)
            elif text == "2":#numpad 2
                print("backward movement")
                drone.piloting_pcmd(0, nspeed, 0, 0, duration)
                if(recording == True):
                    rec.write(text)
            elif text == "4":#numpad 4
                print("going left")
                drone.piloting_pcmd(nspeed, 0, 0, 0, duration)
                if(recording == True):
                    rec.write(text)
            elif text == "6":#numpad 6
                print("going right")
                drone.piloting_pcmd(speed, 0, 0, 0, duration)
                if(recording == True):
                    rec.write(text)
            elif text == "7":#numpad 7
                print("turning left")
                drone.piloting_pcmd(0, 0, nspeed, 0, duration)
                if(recording == True):
                    rec.write(text)
            elif text == "9":#numpad 9
                print("turning right")
                drone.piloting_pcmd(0, 0, speed, 0, duration)
                if(recording == True):
                    rec.write(text)
            elif text == "1":#numpad 1
                print("going down")
                drone.piloting_pcmd(0, 0, 0, nspeed, duration)
                if(recording == True):
                    rec.write(text)
            elif text == "3":#numpad 3
                print("going up")
                drone.piloting_pcmd(0, 0, 0, speed, duration)
                if(recording == True):
                    rec.write(text)
            elif text == "5":#numpad 5
                print("stopping")
                drone.piloting_pcmd(0, 0, 0, 0, duration)
                if(recording == True):
                    rec.write(text)
            elif text == 'c':
                temp = input()
                if temp[0] == 'c':
                    temp = temp[1:]
                if temp.isdigit() == True:
                    speed = int(temp)
                    nspeed = speed - speed - speed
                else:
                    print("faulty input")
                print("the current speed is: " + str(speed))
            elif text == 'd':
                temp = input()
                if temp[0] == 'd':
                    temp = temp[1:]
                if type(duration == float):
                    duration = float(temp)
                else:
                    print("faulty input")
                print("the current duration is: " + str(duration))
            elif text == 'r':
                if recording == False:
                    recording = True
                    rec = open("recordedpath.txt", "w+")
                    print("recording on")
                    stime = perf_counter()
                elif recording == True:
                    recording = False
                    rec.close()
                    print("recording off")
            elif text == 'l':
                if recording == True:
                    rec.close()
                    recording = False
                if os.path.isfile("recordedpath.txt") == True:
                    rec = open("recordedpath.txt", "r")
                    rewind = list(rec.read())
                    recCurrent = 0
                    cMode = True
                    rtime = 0
                elif os.path.isfile("recordedpath.txt") == False:
                    print("no recorded path found")
            elif text == 'e':
                print("quitting pilot mode")
                drone.stop_piloting()
                piloting = False
            time.sleep(duration)
            if recording == True:
                etime = perf_counter()
                rec.write(">" + str(etime - stime - duration) + "<")
drone.disconnection()
tcflush(sys.stdin, TCIFLUSH)#flush input buffer