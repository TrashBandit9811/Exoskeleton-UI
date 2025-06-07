# 🦾 Interfaz gráfica para Exoesqueleto 
# Interfaz gráfica con Raspberry Pi y pantalla táctil

Este proyecto es un sistema de menú creado con **Python** y **Kivy** y diseñado para correr en un **Raspberry Pi 4** con una pantalla táctil oficial de Raspberry de 7".

Este proyecto está diseñado para cambio de modos en tiempo real, configuración y control intuitivo.

## Características

-Interfaz de usuario a pantalla completa de 800x480 con pantalla táctil y botones físicos
-Modo operativo con retroalimentación visual
-Sistema de retroalimentación mediante buzzer
-Integración limpia entre hardware y software

## Hardware

| Componente                  | Detalles                         |
| ----------------------------|----------------------------------|
| Raspberry Pi                | 4 Modelo B (2GB RAM)             |
| Touchscreen display         | 7" Official Raspberry Pi Display |
| Botones                     | 2 botones externos por GPIO      |
| Retroalimentación auditiva  | Buzzer en GPIO                   |
| Fuente de alimentación      | ???                              |
| Tarjeta micro SD            | 32GB mínimo, A1 o A2             |
------------------------------------------------------------------

## Instructiones de instalación

#### Hardware necesario
- Raspberry Pi 4 Modelo B
- Pantalla táctil oficial Raspberry de 7"
- Una computadora (Windows, macOS o Linux)
- Marco para pantalla táctil de Raspberry
- Tarjeta micro SD(32GB mínimo)
- Lector de tarjetas micro SD
- 4 cables puente (hembra a hembra)
- Cinta DSI (incluida en el paquete de pantalla táctil) 
- Fuente oficial altamente recomendada o en su defecto regulador (5V 3A)
- Destornillador de cruz
- Toalla antiestática

### 1.  Conexión Física de Raspberry a Pantalla Táctil

#### Conexión física inicial
Puedes seguir los pasos en [este video](https://www.youtube.com/watch?v=SIUfAIiSzJA&ab_channel=MakeUseOf)

- Extiende la toalla antiestatica en tu mesa de trabajo, y coloca la pantalla táctil boca abajo.
- Inserta los cuatro cables puente y la cinta DSI (lado azul por abajo), como la foto. Asegurate de que el seguro de la cinta haga click antes de seguir con otro paso. Debería verse como la siguiente foto:  
![texto de prueba](assets/images/touchscreen-connection.jpg)
Los colores deben ser los siguientes:  
*Negro* para GND  
*Amarillo* para SCL  
*Verde* para SDA  
*Rojo* para 5V  

- Una vez conectados los cables, monta el Raspberry arriba de la placa de la pantalla táctil, con los agujeros para atornillar correctamente posicionados  
![texto de prueba 2](assets/images/raspberry-on-top-of-touchscreen.jpg)

Usa el destornillador y los tornillos incluidos en la caja para asegurar la Raspberry Pi. Luego, conecta los cables puente a la Raspberry en el orden correcto, y el cable plano DSI (nuevamente, con el lado azul hacia abajo). Asegúrate de que quede bien asegurado en su lugar.  
![texto de prueba 3](assets/images/raspberry-and-touchscreen-connection.jpg)
Este es el orden correcto para conectar los PINS físicos:
Recomendación: consulta la tabla de Raspberry Pi disponible en este repositorio en assets/images/raspberry-pinout.
TEN CUIDADO DE USAR LOS PINS FISICOS, NO LOS BCM
*Negro* en el pin físico 6 (GND)  
*yellow* en el pin físico 5 (GPIO/SCL1) **I2C**  
*green* en el pin físico 3 (GPIO/SDA1) **I2C**  
*red* en el pin físico 4 (5V)  

### 2. Grabar y configurar la tarjeta SD
- En tu computadora, ve a [este link](https://www.raspberrypi.com/software/) para el sistema operativo de Raspberry Pi más reciente.
- Descarga la versión para tu sistema operativo , abre el archivo y sigue el proceso de instalación
- Inserta tu tarjeta Micro SD en tu lector. Respalda tu información, ya que todos los datos serán **borrados**.
- En Raspberry Pi Imager, haz click en **Choose OS**, y después busca **Raspberry Pi OS (32-Bit)** y haz click.
- Busca **Choose Storage** y haz click, después, selecciona tu tarjeta SD
- *Opcionalment* da click en **Settings** para configurar el nombre del host, el SSH, y otras configuraciones.
- Da click en **Write** y espera al programa para que baje el sistema opeativo y lo instale en la tarjeta. Debería tomar aproximadamente 10 minutos.
- Una vez que la grabación esté completada, expulsa seguramente la tarjeta de tu computadora e insertala en la ranura de tu Raspberry Pi.

- Once these steps are completed, mount your Raspberry touchscreen and Raspberry Pi to your frame. Be careful not to damage the jumper cables or the DSI ribbon. Use a screwdriver to hold it in place

NOTE: if your Raspberry Pi screen is upside down, you will need to complete the following steps
- Go to the terminal and run
```bash
sudo nano /boot/config.txt
```
At the top of the file, add the following text:
```bash
lcd_rotate=2
```

### 3. Enable Interfaces
```bash
sudo raspi-config
```
- Use your arrow keys to navigate
- Go to **Interface Options**
- ??? Enable SSH
- Enable I2C
- Go back and go to **Advanced Options**, then select **Expand Filesystem**


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
