import time
import sys
from naoqi import ALProxy, ALBroker, ALModule

robotIP = "10.1.94.197"  
PORT = 9559

class TouchModule(ALModule):
    def __init__(self, name):
        ALModule.__init__(self, name)
        self.memory = ALProxy("ALMemory", robotIP, PORT)
        self.memory.subscribeToEvent("TouchChanged", name, "on_head_touch")

    def on_head_touch(self, *_args):
        print("TEST")

if __name__ == "__main__":
    
    myBroker = ALBroker("myBroker", "0.0.0.0", 0, robotIP, PORT)    
    
    touchModule = TouchModule("touchModule")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        myBroker.shutdown()
        sys.exit(0)
