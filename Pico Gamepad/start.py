import time
import usb_hid

from button import button

from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.gamepad import Gamepad

kbd = Keyboard(usb_hid.devices)
gp = Gamepad(usb_hid.devices)
m = Mouse(usb_hid.devices)

gp.move_joysticks(0, 0, 0, 0)
btn = button()
btn.record(gp, kbd, m)
