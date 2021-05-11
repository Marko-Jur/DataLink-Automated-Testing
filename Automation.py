#Importing relevant libraries
import keyboard
import time
import pyautogui
# Using time.sleep, we can dramatically decrease the amount of CPU our program
# uses.

#Globals:
MANUFACTURER = "DOMETIC"
PRODUCT_DESCRIPTION = "STANDARD DIAL CONTROLLER, MAIN STATION"
PRODUCT_SERIAL_PREFIX = "TTD1192101"
PRODUCT_PART_NUMBER = "CON0500"
PRODUCT_MANUFACTURING__DAY= PRODUCT_SERIAL_PREFIX[3] + PRODUCT_SERIAL_PREFIX[4] + PRODUCT_SERIAL_PREFIX[5]
PRODUCT_MANUFACTURING_YEAR = PRODUCT_SERIAL_PREFIX[6] + PRODUCT_SERIAL_PREFIX[7]
PRODUCT_MANUFACTURING_DATE = PRODUCT_MANUFACTURING__DAY + "/" + PRODUCT_MANUFACTURING_YEAR

#Hotkeys
hotKey_1 = "F1"
hotKey_2 = "F2"
hotKey_3 = "F3"


#Performs the LED test for the CON0500 EOL Controllers
def ledTest():
    #Testing the outer LEDS
    for i in range(16):
        time.sleep(0.01) #Sleep required in order to ensure data is inputted into DataLink
        keyboard.write("50") 
        pyautogui.press("enter")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        

    time.sleep(3) #Delay for human verification of LED quality
    
    #Cycle to the Analog outputs section in DataLink (76)
    for i in range(76):
        pyautogui.press("tab")

    #Testing Red central LED PWM
    keyboard.write("50") 
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
        
    time.sleep(2) # Delay for human verification of central LED quality

    #Testing Green central LED PWM
    keyboard.write("50") 
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
        
    time.sleep(2) # Delay for human verification of central LED quality

    #Testing Blue central LED PWM
    keyboard.write("50") 
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
        
    time.sleep(2) # Delay for human verification of central LED quality


#Inputs information into the CON0500 EOL Controller
def informationInput():
    keyboard.write(PRODUCT_PART_NUMBER) 
    pyautogui.press("tab")
    keyboard.write(PRODUCT_SERIAL_PREFIX) 
    pyautogui.press("tab")
    keyboard.write(PRODUCT_MANUFACTURING_DATE) 
    pyautogui.press("tab")
    keyboard.write(MANUFACTURER)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    keyboard.write(PRODUCT_DESCRIPTION)


def main():
    if keyboard.is_pressed(hotKey_1):
        informationInput()
        
    elif keyboard.is_pressed(hotKey_2):
        ledTest()


#Main loop scans for HotKeys and outputs text sequences based on HotKey input
while True:
    main()




    
    
           