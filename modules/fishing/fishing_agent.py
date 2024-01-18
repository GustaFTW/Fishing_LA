import time
import cv2 as cv
import numpy as np
import pyautogui


CONFIDENCE = 0.7
FISHING_WATCH_TIME = 8
SHIFT = 75

class FishingAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent
        self.fishing_target = cv.imread("modules/fishing/assets/imagem_isca_crop.jpg")
        if self.fishing_target is None:
            print("Couldn't load fishing target\nExiting program...")
            exit()
        self.fishing_thread = None
        self.cropped_image = None
        self.res = (0, 0, 0, 0)

    
    def cast_lure(self):
        print("Casting...")
        pyautogui.press("e")
        time.sleep(0.5)
        self.find_lure()

    def find_lure(self):
        if self.main_agent.cur_img is not None:
            # print("entering this function again")
            try:
                self.res = pyautogui.locate(self.fishing_target, 
                                       self.main_agent.cur_img, 
                                       confidence=CONFIDENCE)
                if self.res != (0, 0, 0, 0):
                    print("Lure found!")
                    self.crop_and_watch_lure(self.res)
            except Exception as e:
                print(f"Couldn't find the bait...")
    
    # def crop_on_lure(self, aoi):
    #     # print("Starting the crop...")

    #     # Define the SHIFT
    #     SHIFT = 75
        
    #     # Define the res
    #     x, y, w, h = aoi 
    #     # Crop the image
    #     cropped_image = self.main_agent.cur_img[(y - SHIFT):y+(h + SHIFT), (x - SHIFT):x +(w + SHIFT)]

    #     self.cropped_image = cropped_image

    def crop_and_watch_lure(self, res):
        print("Watching lure")
        watch_time = time.time()

        while True:
            print("still looking...")
            try: 
                # Define the res
                x, y, w, h = res 
                # Crop the image
                image = np.array(self.main_agent.cur_img)[(y - SHIFT):y+(h + SHIFT), (x - SHIFT):x +(w + SHIFT)]

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
                    time.sleep(1)
                    self.pull_line()
                    break
                if time.time() - watch_time >= FISHING_WATCH_TIME:
                    print("Time out")
                    break
                time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")

        self.pull_line()

    def pull_line(self):
        print("Pulling line!")
        pyautogui.press("e")
        print("Restarting the program...")

    def run(self):
        while True:
            self.cast_lure()
            time.sleep(5)