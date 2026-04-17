# UART Initialization on Raspberry Pi

## Overview
UART (Universal Asynchronous Receiver Transmitter) allows serial communication using GPIO pins on the Raspberry Pi. It is commonly used to communicate with microcontrollers like Arduino, ESP32, GPS modules, etc.

---

## GPIO Pins Used for UART

| Function | GPIO Pin | Physical Pin |
|----------|--------|-------------|
| TXD      | GPIO14 | Pin 8       |
| RXD      | GPIO15 | Pin 10      |
| GND      | -      | Any GND Pin |

---

## Step 1: Enable UART

### Method 1: Using raspi-config

```bash
sudo raspi-config
```

Navigate to:
Interface Options → Serial Port

- Disable login shell over serial: No
- Enable serial port hardware: Yes

Reboot:
```bash
sudo reboot
```

---

### Method 2: Manual Configuration

Open the configuration file:

```bash
sudo nano /boot/firmware/config.txt
```

Add the following lines:

```bash
enable_uart=1
dtoverlay=disable-bt
```

Save and reboot:

```bash
sudo reboot
```

---

## Step 2: Verify UART

Check available serial devices:

```bash
ls /dev/serial*
```

Expected output:
/dev/serial0

Check mapping:

```bash
ls -l /dev/serial0
```

Possible outputs:
/dev/serial0 -> ttyAMA0  
or  
/dev/serial0 -> ttyS0  

---

## Step 3: UART Communication Using Python

### Install Required Library

```bash
pip install pyserial
```

---

### Example Code (Send + Receive)

```python
import serial
import time

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

time.sleep(2)

while True:
    ser.write(b'Hello from Raspberry Pi\n')

    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        print("Received:", data)

    time.sleep(1)
```

---

## Step 4: Wiring

| Raspberry Pi | External Device |
|--------------|----------------|
| GPIO14 (TX)  | RX             |
| GPIO15 (RX)  | TX             |
| GND          | GND            |

---

## Important Notes

- Raspberry Pi uses 3.3V logic
- Do NOT connect directly to 5V devices (like Arduino UNO) without level shifting
- Always ensure:
  - Common ground
  - Correct TX ↔ RX connection
  - Matching baud rate

---

## Troubleshooting

- No data received:
  - Check wiring (TX ↔ RX)
  - Verify baud rate
  - Ensure UART is enabled
- Wrong device:
  - Use /dev/serial0 instead of ttyAMA0 or ttyS0
- Unstable communication:
  - Disable Bluetooth (dtoverlay=disable-bt)

---

## Conclusion

UART on Raspberry Pi can be easily initialized and used through GPIO pins by enabling it via system configuration and accessing it using /dev/serial0. It is a reliable method for communication with embedded systems when proper voltage levels and wiring are maintained.
