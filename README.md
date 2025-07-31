# 🦾 Exoskeleton UI
# Raspberry Pi Touchscreen Interface
This project is a graphical menu system built with Python and Kivy, designed to run on a Raspberry Pi 4 with the official 7" touchscreen.

This project is designed for real-time mode switching, configuration, and intuitive control of the exoskeleton.

## Features
- Full-screen 800x400px graphical interface with physical buttons

- Visual feedback of physical operations

- Buzzer-based feedback

- Clean software-hardware integration

## Hardware
| Component            | Details                          |
| ---------------------|----------------------------------|
| Raspberry Pi         | 4 Model B (2GB RAM)              |
| Touchscreen          | Official Raspberry 7" screen     |
| External buttons     | GPIO-connected buttons           |
| Audio                | GPIO passive buzzer              |
| Power Supply         | Official Raspberry supply        |
| microSD Card         | 32GB minimum, A1 or A2           |
-----------------------------------------------------------

## Installation instructions

#### Needed hardware
- Raspberry Pi 4 Model B
- Official Raspberry 7" screen
- A computer (Windows, macOS or Linux)
- Raspberry Pi Frame
- MicroSD Card (32GB minimum)
- MicroSD card reader
- 4 (already included in the Touchscreen) jumper cables Socket to Socket
- Ribbon cable DSI 
- Official Raspberry Power Supply (5V 3A)
- Screwdriver
- Antistatic Towel
- Keyboard with USB
- Mouse with USB

### 1. Raspberry Preparation

#### Initial physical connection  

- Place your anti-static towel on your work surface, and lay the touchscreen face down on it.
- Insert the four power cables and the DSI ribbon cable (blue side facing down). Make sure you hear a click when closing the DSI connector. It should look like the photo below:

![texto de prueba](assets/images/touchscreen-connection.jpg)
This is the color coding:
*black* for GND
*yellow* for SCL
*green* for SDA
*red* for 5V


- Place the Raspberry Pi over the screw holes on the screen. Make sure they are properly aligned.

![texto de prueba 2](assets/images/raspberry-on-top-of-touchscreen.jpg)

- Use the screws included in your touchscreen package and secure the Raspberry Pi in place using the Phillips screwdriver. Then, connect the cables from the screen to the Raspberry Pi in the correct order, and the DSI ribbon cable (again, blue side down). Make sure you follow the proper order.

![texto de prueba 3](assets/images/raspberry-and-touchscreen-connection.jpg)
Here is the correct order to connect the cables:
**MAKE SURE TO USE THE GUIDE IN** `assets/images/raspberrypinout.jpg` — this refers to the **PHYSICAL pins**, NOT the BCM numbering.

* *Black* → Physical pin 6 (**GND**)
* *Yellow* → Physical pin 5 (**GPIO/SCL1**) **I2C**
* *Green* → Physical pin 3 (**GPIO/SDA1**) **I2C**
* *Red* → Physical pin 4 (**5V**)


### 2. Flashear y configurar la tarjeta SD
- En tu computadora, ve a [este link](https://www.raspberrypi.com/software/) para la última versión estable de Raspberry Pi OS
- Descarga la versión correcta para tu sistema operativo
- Inserta tu tarjeta microSD en tu computadora. Respalda tu información, todo en la tarjeta será **borrado**
- En Raspberry Pi Imager, haz clic en **Choose OS**, después selecciona **Raspberry Pi OS (32-Bit)**
- Haz clic **Choose Storage** y selecciona tu tarjeta microSD.
- *Opcionalmente* haz clic en **Settings** para configurar el hostname, activar SSH, y otras configuraciones.
- Haz clic en **Write** y espera a que el programa descargue el sistema y lo instale en tu tarjeta microSD. Debería tomar 10 min en promedio.
- Una vez que la instalación se complete, inserta la tarjeta en tu Raspberry Pi.

- Ya que se completen estos pasos, coloca todo en tu marco. Asegurate de manejar con cuidado los cables y el DSI. Usa el destornillador para cerrarlo.

NOTA: Hay un error común que muestra la pantalla dada vuelta, si este es el caso para tí, necesitarás completar estos pasos adicionales al encender tu dispositivo.
- Ve a la terminal y corre el comando
```bash
sudo nano /boot/config.txt
```
Se abrirá un archivo de texto, hasta arribla coloca las líneas:
```bash
lcd_rotate=2
```
RECORDAR AÑADIR UNA CAPTURA DE ESTO PARA QUE SE ENTIENDA MEJOR

### 3. Enable Interfaces
Con tu raspberry encendido, ve a la terminal en AÑADIR UBICACIÓN DE LA TERMINAL, y corre los comandos
```bash
sudo raspi-config
```
- Usa las flechas del teclado para navegar
- Ve a **Interface Options**
- ??? Activa SSH <-VER SI ES NECESARIO
- Activa I2C
- Regresa a **Advanced Options**, y después selecciona **Expand Filesystem**

### 4.  la interfaz gráfica en el Raspberry
- Ve a [esta pagina](https://github.com/TrashBandit9811/Exoskeleton-UI)
- Haz clic en el botón azul "Code"
- Selecciona **Download ZIP**
- En tu navegador de archivos, busca la carpeta y extrae su contenido
- descargar AÑADIR PASOS
- pasar a la USB DESCRIBIR MEJOR
- Expulsar de manera segura la USB
- Insertar la USB en el Raspberry Pi
- AÑADIR PASOS A HACER EN EL RASPBERRY PI

### 5. Instalar Dependencias
- ???
- ???

### 6. Make App Run Automatically
- ???
- ???

## Other important files
For additional documentation, refer to:
- **wiring.md**: GPIO pinout and button/buzzer connections
- **ui-layout.md**
- **setup.md**


## Notes
This project is actively under development
