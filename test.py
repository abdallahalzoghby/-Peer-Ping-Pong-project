from naoqi import ALProxy
from naoqi import ALProxy, ALBroker, ALModule
import time
###############################################################
nao_ip = "10.1.95.107"  # "10.1.95.39"
waiting = True
myBroker = ALBroker("myBroker", "0.0.0.0", 0, nao_ip, 9559)    
###############################################################
class TouchModule(ALModule):
    def __init__(self, name):
        ALModule.__init__(self, name)
        self.memory = ALProxy("ALMemory", nao_ip, 9559)
        self.memory.subscribeToEvent("TouchChanged", name, "on_head_touch")
    def on_head_touch(self, *_args):
        global waiting
        waiting = False
        print("TEST", waiting)
###############################################################
text = ALProxy("ALTextToSpeech", nao_ip, 9559)
motion_proxy = ALProxy("ALMotion", nao_ip, 9559)
touchModule = TouchModule("touchModule")
###############################################################
def throw_ball():
    motion_proxy.setAngles(
        ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"],
        [-1.2, 0.0, 0.7, -0.5, -1.4], 
        0.45
    )
    time.sleep(1.0)  
###############################################################
def raise_left_hand(x):
    joint_names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
    if x == 0:
        target_angles = [1.2, 0.0, 0.0, 0.0, 0.0]
    elif x == 1:
        target_angles = [0.8, 0.0, -1.3, -1.3, -2.8]     
    elif x == 2:
        target_angles =[-2.08, 0.0, 1.5, 1.9, -1.4]
    speed = 0.26
    motion_proxy.setAngles(joint_names, target_angles, speed)
    time.sleep(0.100)
###############################################################
if __name__ == "__main__":
    motion_proxy.setStiffnesses("Body", 1.0)
    successful_shots = 0
    while successful_shots < 7:
        waiting = True
        text.say("hello ")
        raise_left_hand(0)
        time.sleep(2.0)
        
        raise_left_hand(1)
        text.say("put the ball in my hand and tuch my head  ")
        motion_proxy.openHand("LHand")
        while waiting:
            raise_left_hand(1)
            time.sleep(0.010)
        motion_proxy.closeHand("LHand")
        
        raise_left_hand(2)
        time.sleep(1.5)
        motion_proxy.openHand("LHand")
        # Simulate grabbing and throwing a ball
        throw_ball()
        
        # Ask the user if the shot was successful
        text.say("If I hit the goal give me yes")
        user_input = raw_input("Did the shot succeed? (yes/no): ").lower()
        
        if user_input == "yes":
            successful_shots += 1
        
        raise_left_hand(0)