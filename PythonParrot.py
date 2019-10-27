import keyboard
import olympe
import time
from olympe.messages.ardrone3.Piloting import TakeOff, Landing

text = "stuff"
done = False#for main while loop
piloting = False#for piloting while loop
duration = 0.1
speed = 50
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
    text = keyboard.read_key()
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
            if cMode == False:
                text = keyboard.read_key()
            elif cMode == True:
                print("load mode here")
                text = rewind[recCurrent]
                recCurrent += 1
                if recCurrent == len(rewind):
                    cMode = False
            if text == "8":#numpad 8
                print("forward movement")
                drone.piloting_pcmd(0, speed, 0, 0, duration)#drone.piloting_pcmd(roll, pitch, yaw, gaz, duration(seconds)) ints between -100 and 100
                if(recording == True):
                    rec.write(text)
            elif text == "2":#numpad 2
                print("backward movement")
                drone.piloting_pcmd(0, nspeed, 0, 0, duration)#.wait()
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
                stoi:speed = input
            elif text == 'd':
                stoi:duration = input
            elif text == 'r':
                if recording == False:
                    recording = True
                    rec = open("recordedpath.txt", "w+")
                    print("recording on")
                elif recording == True:
                    recording = False
                    rec.close()
                    print("recording off")

            elif text == 'l':
                if recording == True:
                    rec.close()
                    recording = False
                rec = open("recordedpath.txt", "r")
                rewind = list(rec.read())
                recCurrent = 0
                cMode = True
                
            elif text == 'e':
                print("quitting pilot mode")
                drone.stop_piloting()
                piloting = False
            time.sleep(duration)

drone.disconnection()