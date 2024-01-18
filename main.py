from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time
from threading import Thread
from modules.fishing.fishing_agent import FishingAgent

class MainAgent:
    def __init__(self) -> None:
        # A list that contain all the agents (responsible for different tasks)
        self.agents = []

        # A variable for the thread
        self.fishing_thread = None
        
        # Variable for the screenshot
        self.cur_img = None
        self.cur_imgHSV = None

        # Defines the quality of fishing tool (they have different colors)
        self.fishing_tool = "Purple"

        # print("Main Agent setup complete...")



def update_screen(agent):

    t0 = time.time()
    fps_report_delay = 5
    fps_report_time = time.time()
    while True: 
        # Grab the screenshot
        agent.cur_img = ImageGrab.grab(all_screens=True)

        # Save it as a numpy array
        agent.cur_img = np.array(agent.cur_img)
        
        # Turn to bgr
        agent.cur_img = cv.cvtColor(agent.cur_img, cv.COLOR_RGB2BGR)
        
        # Turn it to hsv
        agent.cur_imgHSV = cv.cvtColor(agent.cur_img, cv.COLOR_BGR2HSV)
        # Show the screen
        # cv.imshow("Screen", agent.cur_img)
        
        # Wait for the Q to quit
        key = cv.waitKey(1)
        if key == ord('q'):
            break

        # Calculate and show FPS
        ex_time = time.time() - t0
        if time.time() - fps_report_time >= fps_report_delay:
            print(f"FPS:{1 / (ex_time):.2f} " + str(), end="\r")
            fps_report_time = time.time()
        t0 = time.time()
        time.sleep(0.005)

def print_menu():
    print("Enter a command: ")
    print("\tS\tStart the main agent.")
    print("\tZ\tSet rarity of fishing rod.")
    print("\tF\tStart the fishing agent.")
    print("\tQ\tQuit fishing.")


if __name__ == "__main__":
    # Instantiate the main class
    main_agent = MainAgent()


    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()

        if user_input == "s":
            # Create the thread that reads the screen
            update_screen_thread = Thread(target=update_screen, 
                                          args=([main_agent]),
                                          name="update screen thread",
                                          daemon=True) # Setting daemon to true, makes that the function doesn't get stuck on the loop
            update_screen_thread.start()
            print("Thread Started")
        
        elif user_input == "z":
            pass
        elif user_input == "f":
            fishing_agent = FishingAgent(main_agent)
            fishing_agent.run()
        elif user_input == "q":
            cv.destroyAllWindows()
            break
        else:
            print("Input error.")
            print_menu()    
        
    print("Done application")