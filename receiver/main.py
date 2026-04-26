from machine import Pin, PWM
import network
import espnow

# =========================
# MOTOR PINS
# =========================
AIN1 = Pin(5, Pin.OUT)   #D1
AIN2 = Pin(4, Pin.OUT)   #D2
PWMA = PWM(Pin(14))      #D5

BIN1 = Pin(12, Pin.OUT)  #D6
BIN2 = Pin(13, Pin.OUT)  #D7
PWMB = PWM(Pin(15))      #D8

PWMA.freq(500)
PWMB.freq(500)

speed = 1023

# =========================
# FUNCTIONS 
# =========================
def forward():
    AIN1.on(); AIN2.off()
    BIN1.on(); BIN2.off()
    PWMA.duty(speed)
    PWMB.duty(speed)

def backward():
    AIN1.off(); AIN2.on()
    BIN1.off(); BIN2.on()
    PWMA.duty(speed)
    PWMB.duty(speed)

def left():   # 🔥 FIXED
    AIN1.on(); AIN2.off()
    BIN1.off(); BIN2.on()
    PWMA.duty(speed)
    PWMB.duty(speed)

def right():  # 🔥 FIXED
    AIN1.off(); AIN2.on()
    BIN1.on(); BIN2.off()
    PWMA.duty(speed)
    PWMB.duty(speed)

def stop():
    PWMA.duty(0)
    PWMB.duty(0)

# =========================
# ESPNOW SETUP
# =========================
sta = network.WLAN(network.STA_IF)
sta.active(True)

e = espnow.ESPNow()
e.active(True)

# =========================
# MAIN LOOP
# =========================
last_cmd = ""

while True:
    host, msg = e.recv()

    if msg:
        cmd = msg.decode()
        print("Received:", cmd)

        if cmd == last_cmd and cmd != "STOP":
            continue

        last_cmd = cmd

        if cmd == "FORWARD":
            forward()
        elif cmd == "BACKWARD":
            backward()
        elif cmd == "LEFT":
            left()
        elif cmd == "RIGHT":
            right()
        else:
            stop()



