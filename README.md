# 🚀 ESP-NOW Gesture Controlled Car

> Control a robot car using just your hand — no WiFi, no internet, just pure ESP-NOW ⚡

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Project](https://img.shields.io/badge/Type-Robotics-blue)
![Latency](https://img.shields.io/badge/Latency-Ultra%20Low-red)
---
---

## 🎥 Demo

![Demo](images/demo.gif)

## 🧠 How It Works

1. **ESP32 + MPU6050 (Sender)** detects hand tilt  
2. Converts tilt → movement commands  
3. Sends commands via **ESP-NOW (ultra low latency)**  
4. **ESP8266 (Receiver)** controls motors via TB6612  

---

## 🎮 Controls

| Gesture | Action |
|--------|--------|
| Tilt Forward | 🚗 Forward |
| Tilt Backward | 🔙 Backward |
| Tilt Left | ⬅️ Left |
| Tilt Right | ➡️ Right |
| Neutral | 🛑 Stop |

---

## ⚡ Features

- 🔥 No WiFi router required (ESP-NOW)
- ⚡ Ultra low latency control
- 🧠 Gesture-based movement
- 🛑 Auto STOP failsafe if signal lost
- 💨 Max speed optimized (PWM tuned)
- 🔋 Stable power using buck converter
- 🎯 Clean and efficient code


## 🛠️ Tech Stack

![ESP32](https://img.shields.io/badge/ESP32-MCU-red)
![ESP8266](https://img.shields.io/badge/ESP8266-MCU-blue)
![MicroPython](https://img.shields.io/badge/MicroPython-Code-green)
![ESP-NOW](https://img.shields.io/badge/ESP--NOW-Protocol-orange)
![MPU6050](https://img.shields.io/badge/MPU6050-Sensor-yellow)
![TB6612](https://img.shields.io/badge/TB6612-MotorDriver-lightgrey)
![Li-ion](https://img.shields.io/badge/Li--ion-Battery-purple)
![LM2596](https://img.shields.io/badge/LM2596-BuckConverter-brightgreen)
---

## 🧩 Hardware Used

- ESP32 (Sender)
- ESP8266 NodeMCU (Receiver)
- MPU6050
- TB6612FNG Motor Driver
- 2x DC Motors (2WD)
- 2x 18650 Batteries
- LM2596 Buck Converter
- Robot Chassis

---

## 🔌 Wiring Overview

### Sender (ESP32 + MPU6050)
- SDA → GPIO21  
- SCL → GPIO22  
- VCC → 3.3V  
- GND → GND  

### Receiver (ESP8266 + TB6612)
- D1 → AIN1  
- D2 → AIN2  
- D5 → PWMA  
- D6 → BIN1  
- D7 → BIN2  
- D8 → PWMB  
- STBY → 3.3V  


---

## 🛠️ Setup

1. Flash `sender/main.py` → ESP32  
2. Flash `receiver/main.py` → ESP8266  
3. Update MAC address in sender code  
4. Power both boards  
5. Start moving your hand 😎  

---

## ⚠️ Important Notes

- All GND must be common  
- Use buck converter (5V) for ESP8266  
- Li-ion battery recommended for stable performance  
- Adjust threshold for sensitivity  

---

## 🧪 Future Improvements

- 🔋 Battery level monitoring  
- 📱 Mobile app control  
- 🤖 Autonomous mode  
- 🎯 Gesture smoothing (advanced filtering)  

---

## 🧑‍💻 Author

**Miles**  

---

## ⭐ Support

If you like this project:
- ⭐ Star the repo  
- 🍴 Fork it  
- 🔥 Build your own version  

---

## 💡 Inspiration

Built to explore real-time wireless control, embedded systems, and robotics using minimal hardware.

---

> “No wires. No WiFi. Just motion.” ⚡
