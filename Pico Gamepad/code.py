import time
import usb_hid

from button import button

from adafruit_hid.mouse import Mouse
from adafruit_hid.gamepad import Gamepad
from adafruit_hid.consumer_control import ConsumerControl


gp = Gamepad(usb_hid.devices)
m = Mouse(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

gp.move_joysticks(0, 0, 0, 0)
btn = button(oled=True)
btn.show_text("Welcome")
btn.record(gp, cc, m)
