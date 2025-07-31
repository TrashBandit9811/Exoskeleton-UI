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

## Instructiones de instalación

#### Hardware necesario
- Raspberry Pi 4 Modelo B
- Display oficial Raspberry de 7"
- Una computdora (Windows, macOS o Linux)
- Marco para sostener el Raspberry Pi
- Tarjeta microSD (32GB minimo)
- Lector de tarjetas microSD
- 4 cables (hembra a hembra) YA incluidos en el paquete de la pantalla táctil
- Cable plano DSI 
- Fuente de poder oficial de Raspberry (5V 3A)
- Destornillador de cruz
- Toalla antiestática
- Un teclado con USB
- Un mouse con USB

### 1.  Preparando el Raspberry

#### Conexión física inicial  

- Pon tu toalla antiestática sobre tu mesa de trabajo, y encima la pantalla táctil con la pantalla hacia abajo
- Inserta los cuatro cables de corriente, y el cable plano DSI (lado azul hacia abajo). Asegurate de escuchar un clic al cerrarel compartimento del DSI. Debería verse como la foto a continuación:  
![texto de prueba](assets/images/touchscreen-connection.jpg)
Esta es la simbología de los colores:  
*negro* para GND  
*amarillo* para SCL  
*verde* para SDA  
*rojo* para 5V  

- Coloca el Raspberry Pi encima de los agujeros para atornillar de la pantalla. Asegurate de que queden correctamente alineados
![texto de prueba 2](assets/images/raspberry-on-top-of-touchscreen.jpg)

- Usa los tornillos incluidos en tu paquete de pantalla tactil y con el destornillador en cruz asegura Raspberry Pi en su lugar. Después, conecta los cables en el orden correcto de la pantalla al Raspberry, y el cable plano DSI (de nuevo, lado azul hacia abajo), asegúrate de usar el orden adecuado.  
![texto de prueba 3](assets/images/raspberry-and-touchscreen-connection.jpg)
Este es el orden correcto de colocar los cables:  
ASEGURATE DE USAR LA GUIA EN assets/images/raspberrypinout.jpg, se habla de los cables FÍSICOS, NO los BCM
*negro* para el pin físico 6 (GND)  
*amarillo* para el pin físico 5 (GPIO/SCL1) **I2C**  
*verde* para el pin físico 3 (GPIO/SDA1) **I2C**  
*rojo* para el pin físico 4 (5V)  

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
