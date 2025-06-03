# 🦾 Exoskeleton UI - Raspberry Pi Touchscreen Interface 🦾

This project is a graphical menu system created with **Python** and **Kivy** and designed to run on a **Raspberry Pi 4**, with a 7" touchscreen.

This project is designed for real-time mode switching, configuration and intuitive control

## Features

- Full-screen 800x480 UI with touch and physical buttons
- Operational mode for visual feedback
- Buzzer-based feedback system
- Clean hardware-software integration

## Hardware
| Component            | Details                          |
| ---------------------|----------------------------------|
| Raspberry Pi         | 4 Model B (2GB RAM)              |
| Touchscreen display  | 7" Official Raspberry Pi Display |
| External Buttons     | GPIO-connected tactile switches  |
| Audio Feedback       | Passive buzzer on GPIO           |
| Power Supply         | ?????????????????????????????????|
---

## Setup Instructions

### 1.  Setup Raspberry Pi
#### Needed Hardware
- Raspberry Pi 4 Model B
- Official 7" Raspberry Pi Touschreen display
- 4 jumper cables (female to female)
- DSI ribbon cable 
- Official power supply highly recommended (5V 3A)
- Screwdriver
- Antistatic towel

#### Physical Connection
You can follow the steps in [this video](https://www.youtube.com/watch?v=SIUfAIiSzJA&ab_channel=MakeUseOf)
- Place your towel on your working table, then the touchscreen display facing down
- Insert the four power wires, and the DSI ribbon cable (blue side down). Ensure it is securely locked with the catch. It should look as it is shown in the following image:
![texto de prueba](assets/images/touchscreen-connection.jpg)
The following colors are used:
*black* for GND
*yellow* for SCL
*green* for SDA
*red* for 5V

- Mount the raspberry on top of the touchscreen, make sure the screw holes are correcly aligned.
![texto de prueba 2](assets/images/raspberry-on-top-of-touchscreen.jpg)

- Use the screwdriver and the screws included in the box to secure the Raspberry Pi. Next, connect the jumper cables to the Raspberry in the correct order
![texto de prueba 3](assets/images/raspberry-and-touchscreen-connection.jpg)
*black* to pin 6 (GND)
*yellow* to pin 5 (GPIO/SCL1) **I2C**
*green* to pin 3 (GPIO/SDA1) **I2C**
*red* to pin 4 (5V)

### 2. Flash & Configure SD Card
- ???
- ???

### 3. Enable Interfaces
- ???
- ???

### 4. Install Dependencies
- ???
- ???

### 5. Make App Run Automatically
- ???
- ???

## Other important files
For additional documentation, refer to:
- **wiring.md**: GPIO pinout and button/buzzer connections
- **ui-layout.md**
- **setup.md**


## Notes
This project is actively under development
