import time
import cv2 as cv
import numpy as np
import pyautogui


CONFIDENCE = 0.7
FISHING_WATCH_TIME = 20
SHIFT = 75
WATCHING_BAIT_TIME = 5

class FishingAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent
        self.fishing_target = cv.imread("modules/fishing/assets/crop_raridade_roxa.jpg")
        if self.fishing_target is None:
            print("Couldn't load fishing target\nExiting program...")
            exit()
        self.fishing_thread = None
        self.cropped_image = None
        self.res = (0, 0, 0, 0)

    
    def cast_lure(self):
        print("Casting...")
        pyautogui.press("e")
        time.sleep(3)
        self.find_lure()

    def find_lure(self):
        self.watch_time_bait = time.time()
        while True:
            if time.time() - self.watch_time_bait >= WATCHING_BAIT_TIME:
                print("Time out, pulling the line...")
                self.pull_line()
                break
            else: 
                if self.main_agent.cur_img is not None:
                    # print("entering this function again")
                    try:
                        self.res = pyautogui.locate(self.fishing_target, 
                                            self.main_agent.cur_img, 
                                            confidence=CONFIDENCE)
                        if self.res != (0, 0, 0, 0):
                            print("Lure found!")
                            self.crop_and_watch_lure(self.res)
                            break

                        
                    except Exception as e:
                        print(f"Couldn't find the bait...")

    def crop_and_watch_lure(self, res):
        print("Watching lure")
        watch_time = time.time()

        while True:
            self.watch_time_bait = time.time()
            print("still looking...")
            try: 
                # Define the res
                x, y, w, h = res 
                # Crop the image
                image = np.array(self.main_agent.curr_img)[(y - SHIFT):y + (h - (int(SHIFT / 2))), (x - SHIFT):x +(w + SHIFT)]

                # Convert the image to hsv
                image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
                lower_yellow = np.array([14, 75, 207])
                upper_yellow = np.array([34, 107, 227])

                # Define the mask for the threshold
                mask = cv.inRange(image_hsv, lower_yellow, upper_yellow)

                # Apply the mask using the and operation
                yellow_regions = cv.bitwise_and(image_hsv, image_hsv, mask=mask)

                if (yellow_regions != 0).any():
                    print("Fish hooked!")
                    self.pull_line()
                    time.sleep(1)
                    break
                if time.time() - watch_time >= FISHING_WATCH_TIME:
                    print("Time out")
                    break
                # time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")

    def pull_line(self):
        print("Pulling line!")
        pyautogui.press("e")
        print("Restarting the program...")

    def run(self):
        while True:
            self.cast_lure()
            time.sleep(5)