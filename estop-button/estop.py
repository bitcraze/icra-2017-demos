from cflib.drivers import crazyradio
import time
import sys

from linuxjsdev import Joystick

CMD_ESTOP_STOP = 0x03
CMD_ESTOP_WD_RESET = 0x04

CF_DATA_CHANNEL = 110

try:
    js = Joystick()
    js.open(0)
except KeyError:
    print("Joystick not found!")
    sys.exit(1)

try:
    cr = crazyradio.Crazyradio(devid=0)
except Exception:
    print("Crazyradio not found!")
    sys.exit(1)

cr.set_channel(CF_DATA_CHANNEL)
cr.set_data_rate(cr.DR_2MPS)
cr.set_address(b'\xff\xe7\xe7\xe7\xe7')
cr.set_ack_enable(False)

while True:
    jsdata = js.read(0)
    cmd_byte = CMD_ESTOP_WD_RESET
    if jsdata[1][0] == 1:
        cmd_byte = CMD_ESTOP_STOP
    cr.handle.write(endpoint=1, data=(0x61, cmd_byte), timeout=1000)
    time.sleep(0.1)
