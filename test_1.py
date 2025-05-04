from naoqi import ALProxy
import time

# Replace with your NAO's IP address and port
nao_ip = "10.1.94.197"#"10.1.95.39"
nao_port = 9559
text = ALProxy("ALTextToSpeech",nao_ip,9559)
# Connect to the necessary proxies on the robot
motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)

def throw_ball():
    """
    Simulates NAO throwing a ball.
    """
    
    target_angles_grab = [-1.2, 0.0, 0.7, -0.5, -1.4]
    fraction_max_speed = 0.42
    motion_proxy.openHand("LHand")
    motion_proxy.setAngles(["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"], target_angles_grab, fraction_max_speed)
    #motion_proxy.openHand("LHand")
    time.sleep(1.0)  # Adjust the duration as needed
    
def raise_left_hand(x, f):
    # Define the joint names
    joint_names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
    
    # Define the target angles (in radians)
    if x == 0:
        target_angles = [1.2, 0.0, 0.0, 0.0, 0.0]
    elif x == 1:
        target_angles = [0.8, 0.0, -1.3, -1.3, -2.8]
    elif x == 2:
        target_angles =  [-2.08, 0.0, 1.5, 1.9, -1.4]

    # Define the fraction of maximum speed
    if f:
        fraction_max_speed = 0.26
    else:
        fraction_max_speed = 0.2
    
    # Command the motion
    motion_proxy.setAngles(joint_names, target_angles, fraction_max_speed)
    time.sleep(2.0)  # Adjust the duration as needed

def main():
    """
    Main function to control the NAO robot.
    """
    # Set stiffness on for the whole body
    motion_proxy.setStiffnesses("Body", 1.0)
    text.say("hello iiislam")
    raise_left_hand(0, 0.1)
    time.sleep(2.0)
    
    raise_left_hand(1, 0.1)
    
    motion_proxy.openHand("LHand")
    #time.sleep(2.0) 
    motion_proxy.closeHand("LHand")
    
    
    raise_left_hand(2, 0.1)
    
    
    
    # Simulate grabbing and throwing a ball
    throw_ball()
    
    raise_left_hand(0, 0.1)
if __name__ == "__main__":
    main()