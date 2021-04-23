import board
import digitalio
import time
import analogio

from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control_code import ConsumerControlCode

import board

def range_map(x, in_min, in_max, out_min, out_max):
    if (((x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min) < 10) and (((x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min) > -10):
        return 0
    else:
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

class button():
    def __init__(self, oled=False):
        #Direction
        self.btn_up = digitalio.DigitalInOut(board.GP5)
        self.btn_left = digitalio.DigitalInOut(board.GP4)
        self.btn_right = digitalio.DigitalInOut(board.GP6)
        self.btn_down = digitalio.DigitalInOut(board.GP7)
        #Action
        self.btn_x = digitalio.DigitalInOut(board.GP13)
        self.btn_y = digitalio.DigitalInOut(board.GP12)
        self.btn_a = digitalio.DigitalInOut(board.GP10)
        self.btn_b = digitalio.DigitalInOut(board.GP11)
        #Sholder
        self.btn_sholder_left_trigger = digitalio.DigitalInOut(board.GP16)
        self.btn_sholder_left_fire = digitalio.DigitalInOut(board.GP15)
        self.btn_sholder_right_trigger = digitalio.DigitalInOut(board.GP14)
        self.btn_sholder_right_fire = digitalio.DigitalInOut(board.GP17)
        #Settings
        self.btn_start = digitalio.DigitalInOut(board.GP9)
        self.btn_select = digitalio.DigitalInOut(board.GP8)
        self.btn_mode = digitalio.DigitalInOut(board.GP18)
        self.btn_dpad = digitalio.DigitalInOut(board.GP19)

        pull_up_down = digitalio.Pull.UP
        self.btn_up.switch_to_input(pull=pull_up_down)
        self.btn_left.switch_to_input(pull=pull_up_down)
        self.btn_right.switch_to_input(pull=pull_up_down)
        self.btn_down.switch_to_input(pull=pull_up_down)
        self.btn_x.switch_to_input(pull=pull_up_down)
        self.btn_y.switch_to_input(pull=pull_up_down)
        self.btn_a.switch_to_input(pull=pull_up_down)
        self.btn_b.switch_to_input(pull=pull_up_down)
        self.btn_sholder_left_trigger.switch_to_input(pull=pull_up_down)
        self.btn_sholder_left_fire.switch_to_input(pull=pull_up_down)
        self.btn_sholder_right_trigger.switch_to_input(pull=pull_up_down)
        self.btn_sholder_right_fire.switch_to_input(pull=pull_up_down)
        self.btn_start.switch_to_input(pull=pull_up_down)
        self.btn_select.switch_to_input(pull=pull_up_down)
        self.btn_mode.switch_to_input(pull=pull_up_down)
        self.btn_dpad.switch_to_input(pull=pull_up_down)
        
        #Joy Stick
        self.ax = analogio.AnalogIn(board.GP27)
        self.ay = analogio.AnalogIn(board.GP26)
        self.oled = oled
        if(self.oled):
            import busio
            import adafruit_ssd1306
            #OLED Setup
            self.i2c = busio.I2C(board.GP3, board.GP2)
            self.display = adafruit_ssd1306.SSD1306_I2C(128, 64, self.i2c)

        
    def show_text(self, msg, x=45, y=30):
        if(self.oled):
            self.display.fill(0)
            self.display.show()
            self.display.text("IoT Connect",35,10,1)
            self.display.text(msg,x,y,1)
            self.display.show()

    def record(self, gp, consumer_control, m, mode=1):
        #print("Running Infinite Loop")
        while(True):
            if not self.btn_up.value:
                #print("btn_up")
                if mode==1:
                    gp.press_buttons(1)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(1)
                
            if not self.btn_left.value:
                #print("btn_left")
                if mode==1:
                    gp.press_buttons(2)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.SCAN_NEXT_TRACK)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(2)

            if not self.btn_right.value:
                #print("btn_right")
                if mode==1:
                    gp.press_buttons(3)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(3)
            
            if not self.btn_down.value:
                #print("btn_down")
                if mode==1:
                    gp.press_buttons(4)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(4)
            
            if not self.btn_x.value:
                #print("btn_x")
                if mode==1:
                    gp.press_buttons(5)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(5)
            
            if not self.btn_y.value:
                #print("btn_y")
                if mode==1:
                    gp.press_buttons(6)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.STOP)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(6)
            
            if not self.btn_a.value:
                #print("btn_a")
                if mode==1:
                    gp.press_buttons(7)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.REWIND)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(7)
            
            if not self.btn_b.value:
                #print("btn_b")
                if mode==1:
                    gp.press_buttons(8)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.RECORD)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(8)
            
            if not self.btn_sholder_left_trigger.value:
                #print("btn_sholder_left_trigger")
                if mode==1:
                    gp.press_buttons(9)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.EJECT)
                    time.sleep(0.5)
            else:
                if mode==1:
                    gp.release_buttons(9)
            
            if not self.btn_sholder_left_fire.value:
                #print("btn_sholder_left_fire")
                if mode==1:
                    gp.press_buttons(10)
            else:
                if mode==1:
                    gp.release_buttons(10)
            
            if not self.btn_sholder_right_trigger.value:
                #print("btn_sholder_right_trigger")
                if mode==1:
                    gp.press_buttons(11)
            else:
                if mode==1:
                    gp.release_buttons(11)
            
            if not self.btn_sholder_right_fire.value:
                #print("btn_sholder_right_fire")
                if mode==1:
                    gp.press_buttons(12)
            else:
                if mode==1:
                    gp.release_buttons(12)
            
            if not self.btn_start.value:
                #print("btn_start")
                if mode==1:
                    gp.press_buttons(13)
                elif mode==0:
                    consumer_control.send(ConsumerControlCode.MUTE)
                    time.sleep(0.5)
                elif mode==2:
                    m.press(Mouse.LEFT_BUTTON)
            else:
                if mode==1:
                    gp.release_buttons(13)
                elif mode==2:
                    m.release(Mouse.LEFT_BUTTON)
                    
            if not self.btn_select.value:
                #print("btn_select")
                if mode==1:
                    gp.press_buttons(14)
                elif mode==2:
                    m.press(Mouse.RIGHT_BUTTON)                
            else:
                if mode==1:
                    gp.release_buttons(14)
                elif mode==2:
                    m.release(Mouse.RIGHT_BUTTON)


            if not self.btn_mode.value:
                if mode==0:
                    mode = 1
                    self.show_text("Gamepad")
                elif mode==1:
                    mode = 2
                    self.show_text("Mouse")
                elif mode==2:
                    mode = 0
                    self.show_text("Media")
                #print("Mode : "+str(mode))
                time.sleep(0.5)
            
            if not self.btn_dpad.value:
                #print("btn_dpad")
                if mode==1:
                    gp.press_buttons(15)
            else:
                if mode==1:
                    gp.release_buttons(15)
            if mode==1:
                gp.move_joysticks(
                    x=range_map(self.ax.value, 0, 65535, 127, -127),
                    y=range_map(self.ay.value, 0, 65535, -127, 127),
                )
            elif mode==2:
                m.move(
                    x=range_map(self.ax.value, 384, 65520, 10, -10),
                    y=range_map(self.ay.value, 384, 65520, -10, 10),
                )
            time.sleep(0.01)

