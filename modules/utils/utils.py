import pyautogui
import pyscreeze
import numpy as np

def find_and_crop(image:np.ndarray, confidence:float = 0.7) -> pyscreeze.Box:
    """
        Function that receives a image and locate that image on screen, 
        then, it expands the coordinates to a larger box

        args:
            image: image that the function will locate on the screen
    
        returns:
            image: returns a image with only the pixels that are close 
            to the object
    """
    print("Procurando isca.")
    try:
        res = pyautogui.locateOnScreen(image, confidence=confidence)
        print("Isca encontrada.")
    except:
        raise ValueError("Isca não encontrada.")
    
    finally:
       return res 

def got_hook():
    # TODO
    pass