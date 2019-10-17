import keyboard
import olympe
import time
import cv2
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
from olympe.messages.ardrone3.PilotingSettingsState import MaxTiltChanged

# drone = olympe.Drone("192.168.42.1")#real bebop2 drone
text = "stuff"
done = False#for main while loop
piloting = False#for piloting while loop
speed = 100
nspeed = speed - speed - speed

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
    elif text == 'r':
        drone.start_video_streaming("live","DefaultVideo")
    elif text == 't':
        drone.stop_video_streaming()
    elif text == 'c':
        cam = cv.VideoCapture(0)
        ret, frame = cam.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    elif text == 'y':
        drone. set_streaming_callbacks(h264_cb=None, raw_cb=None, end_cb=None, flush_cb=None)
    elif text == 'p':
        drone.start_piloting()
        piloting = True
        while(piloting == True):
            text = keyboard.read_key()
            if text == "8":#numpad 8
                print("forward movement")
                drone.piloting_pcmd(0, speed, 0, 0, 1)#drone.piloting_pcmd(roll, pitch, yaw, gaz, duration(seconds)) ints between -100 and 100
            elif text == "2":#numpad 2
                print("backward movement")
                drone.piloting_pcmd(0, nspeed, 0, 0, 1)
            elif text == "4":#numpad 4
                print("going left")
                drone.piloting_pcmd(nspeed, 0, 0, 0, 1)
            elif text == "6":#numpad 6
                print("going right")
                drone.piloting_pcmd(speed, 0, 0, 0, 1)
            elif text == "7":#numpad 7
                print("turning left")
                drone.piloting_pcmd(0, 0, nspeed, 0, 1)
            elif text == "9":#numpad 9
                print("turning right")
                drone.piloting_pcmd(0, 0, speed, 0, 1)
            elif text == "1":#numpad 1
                print("going down")
                drone.piloting_pcmd(0, 0, 0, nspeed, 1)
            elif text == "3":#numpad 3
                print("going up")
                drone.piloting_pcmd(0, 0, 0, speed, 1)
            elif text == 'q':
                print("quitting pilot mode")
                drone.stop_piloting()
                piloting = False

#print(drone.get_state(MaxTiltChanged))
#drone(TakeOff()).wait()
#drone(Landing()).wait()
#print("Drone MaxTilt = ", drone.get_state(MaxTiltChanged)["current"])
drone.disconnection()
