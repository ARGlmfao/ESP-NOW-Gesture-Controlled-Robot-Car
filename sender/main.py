from machine import Pin, I2C
import network
import espnow
import time

# =========================
# MPU6050 SETUP
# =========================
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
MPU_ADDR = 0x68

i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')

def read_raw(addr):
    high = i2c.readfrom_mem(MPU_ADDR, addr, 1)[0]
    low = i2c.readfrom_mem(MPU_ADDR, addr + 1, 1)[0]
    value = (high << 8) | low
    if value > 32767:
        value -= 65536
    return value

def get_gesture():
    ax = read_raw(0x3B)
    ay = read_raw(0x3D)

    threshold = 6000

    if ax > threshold:
        return "FORWARD"
    elif ax < -threshold:
        return "BACKWARD"
    elif ay > threshold:
        return "LEFT"
    elif ay < -threshold:
        return "RIGHT"
    else:
        return "STOP"

# =========================
# ESPNOW SETUP
# =========================
sta = network.WLAN(network.STA_IF)
sta.active(True)

e = espnow.ESPNow()
e.active(True)

peer = #mac address of your receiver
e.add_peer(peer)

# =========================
# MAIN LOOP
# =========================
last = None

while True:
    gesture = get_gesture()
    data = gesture.encode()   # 🔥 FIX

    if gesture == "STOP":
        e.send(peer, data)
        if last != "STOP":
            print("Sending: STOP")
        last = "STOP"

    else:
        if gesture != last:
            print("Sending:", gesture)
            e.send(peer, data)
            last = gesture

    time.sleep(0.1)
