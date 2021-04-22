import board
import digitalio
import time
import analogio

from adafruit_hid.mouse import Mouse

def range_map(x, in_min, in_max, out_min, out_max):
    if (((x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min) < 10) and (((x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min) > -10):
        return 0
    else:
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

class button():
    def __init__(self):
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

    def record(self, gp, kbd, m, mode=1):
        print("Running Infinite Loop")
        while(True):
            if not self.btn_up.value:
                print("btn_up")
                if mode==1:
                    gp.press_buttons(1)
                elif mode==0:
                    kbd.send(89)
            else:
                if mode==1:
                    gp.release_buttons(1)
                
            if not self.btn_left.value:
                print("btn_left")
                if mode==1:
                    gp.press_buttons(2)
                elif mode==0:
                    kbd.send(90)
            else:
                if mode==1:
                    gp.release_buttons(2)

            if not self.btn_right.value:
                print("btn_right")
                if mode==1:
                    gp.press_buttons(3)
                elif mode==0:
                    kbd.send(91)
            else:
                if mode==1:
                    gp.release_buttons(3)
            
            if not self.btn_down.value:
                print("btn_down")
                if mode==1:
                    gp.press_buttons(4)
                elif mode==0:
                    kbd.send(92)
            else:
                if mode==1:
                    gp.release_buttons(4)
            
            if not self.btn_x.value:
                print("btn_x")
                if mode==1:
                    gp.press_buttons(5)
                elif mode==0:
                    kbd.send(93)
            else:
                if mode==1:
                    gp.release_buttons(5)
            
            if not self.btn_y.value:
                print("btn_y")
                if mode==1:
                    gp.press_buttons(6)
                elif mode==0:
                    kbd.send(94)
            else:
                if mode==1:
                    gp.release_buttons(6)
            
            if not self.btn_a.value:
                print("btn_a")
                if mode==1:
                    gp.press_buttons(7)
                elif mode==0:
                    kbd.send(95)
            else:
                if mode==1:
                    gp.release_buttons(7)
            
            if not self.btn_b.value:
                print("btn_b")
                if mode==1:
                    gp.press_buttons(8)
                elif mode==0:
                    kbd.send(96)
            else:
                if mode==1:
                    gp.release_buttons(8)
            
            if not self.btn_sholder_left_trigger.value:
                print("btn_sholder_left_trigger")
                if mode==1:
                    gp.press_buttons(9)
                elif mode==0:
                    kbd.send(97)
            else:
                if mode==1:
                    gp.release_buttons(9)
            
            if not self.btn_sholder_left_fire.value:
                print("btn_sholder_left_fire")
                if mode==1:
                    gp.press_buttons(10)
                elif mode==0:
                    kbd.send(4)
            else:
                if mode==1:
                    gp.release_buttons(10)
            
            if not self.btn_sholder_right_trigger.value:
                print("btn_sholder_right_trigger")
                if mode==1:
                    gp.press_buttons(11)
                elif mode==0:
                    kbd.send(5)
            else:
                if mode==1:
                    gp.release_buttons(11)
            
            if not self.btn_sholder_right_fire.value:
                print("btn_sholder_right_fire")
                if mode==1:
                    gp.press_buttons(12)
                elif mode==0:
                    kbd.send(6)
            else:
                if mode==1:
                    gp.release_buttons(12)
            
            if not self.btn_start.value:
                print("btn_start")
                if mode==1:
                    gp.press_buttons(13)
                elif mode==0:
                    kbd.send(7)
                elif mode==2:
                    m.press(Mouse.LEFT_BUTTON)
            else:
                if mode==1:
                    gp.release_buttons(13)
                elif mode==2:
                    m.release(Mouse.LEFT_BUTTON)
                    
            if not self.btn_select.value:
                print("btn_select")
                if mode==1:
                    gp.press_buttons(14)
                elif mode==0:
                    kbd.send(8)
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
                elif mode==1:
                    mode = 2
                elif mode==2:
                    mode = 0
                print("Mode : "+str(mode))
                time.sleep(1)
            
            if not self.btn_dpad.value:
                print("btn_dpad")
                if mode==1:
                    gp.press_buttons(15)
                elif mode==0:
                    kbd.send(9)
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

