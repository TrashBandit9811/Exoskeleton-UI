from kivy.app import App # pyright: ignore[reportMissingImports]
from kivy.uix.label import Label # pyright: ignore[reportMissingImports]
from kivy.uix.boxlayout import BoxLayout # pyright: ignore[reportMissingImports]
from kivy.properties import StringProperty # pyright: ignore[reportMissingImports]
from kivy.uix.button import Button # pyright: ignore[reportMissingImports]
import RPi.GPIO as GPIO # pyright: ignore[reportMissingModuleSource]
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# LEFT pins
LEFT_LEDS = [17,27,22]

# RIGHT pins
RIGHT_LEDS = [16,20,21]

class RokiScreen(BoxLayout):
    text = StringProperty("")
    battery_level = StringProperty("87%") # INVESTIGAR COMO OBTENER NIVEL DE BATERIA
    #ESTA BATERIA SE REFIERE AL NIVEL DE LA BATERÍA DEL ROKI, es de donde mismo que se alimenta el Raspberry

    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        GPIO.setmode(GPIO.BCM)
        for pin in LEFT_LEDS + RIGHT_LEDS:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin,GPIO.LOW)
    
    def ir_a_parado(self):
        self.text = "Ir a parado"
        GPIO.output(LEFT_LEDS[0], GPIO.HIGH)
    
    def ir_a_sentado(self):
        self.text = "Ir a sentado"
        GPIO.output(LEFT_LEDS[0], GPIO.HIGH)
    
    def caminar_paso_izquierdo(self):
        self.text = "Caminar paso izquierdo"
        GPIO.output(LEFT_LEDS[1], GPIO.HIGH)

    def caminar_paso_izquierdo(self):
        self.text = "Caminar paso derecho"
        GPIO.output(LEFT_LEDS[2], GPIO.HIGH)
    
    def reset_leds(self):
        self.text = "Resetear LEDs"
        for pin in LEFT_LEDS + RIGHT_LEDS:
            GPIO.output(pin, GPIO.LOW)

class RokiApp(App):
    def build(self):
        screen = RokiScreen()
        return screen
    
    """
    Inicio
    MODO 0
    cambiar modo a "INICIO"
    
    MODO C
    Si toca pantalla derecha:
        Selecciona acción derecha
        Cambia imagen derecha a "Ir a sentado rojo"
        Si toca botón derecho:
            Encender LED derecho 2
            Cambiar ambas acciones a "Preparado amarillo"
            Si toca botón derecho:
                Regresa a MODO C
    
    Si toca pantalla izquierda:
        Selecciona acción izquierda
        Cambiar imagen izquierda a parado azul
        
        MODO B
        Si toca botón derecho:
            Cambia modo a "PARADO"
            Enciende LED izquierdo 1
            Cambia imagen izquierda a "PRIMER PASO"
            Si toca pantalla izquierda:
                Selecciona "DAR PRIMER PASO"
                Cambia imagen izquierda a "DAR PRIMER PASO"
                Selecciona acción izquierda
                Si toca botón derecho:
                    Cambia modo a "CAMINANDO"
                    Apaga LED izquierdo 1
                    Enciende LED izquierdo 2
                    Cambia imagen izquierda a "DAR PASO IZQUIERDO"
                    Cambia imagen derecha a "Ir a sentado"
                
                MODO A
                Si toca botón derecho:
                    Apaga LED izquierdo 2
                    Enciende LED izquierdo 3
                    Cambia imagen izquierda a "DAR PASO DERECHO"
                    Si toca botón derecho:
                        Cambia imagen izquierda a "DAR PASO IZQUIERDO"
                        Apaga LED izquierdo 3
                        Enciende LED derecho 1
                        Si toca botón derecho:
                            Cambia a MODO A

        Si toca pantalla derecha:
            Selecciona acción derecha
            Cambia imagen derecha a "PARADO AZUL"
            Si toca botón derecho:
                Apaga LED derecho 1
                Regresa a MODO B
    
    """

    def on_stop(self):
        #Resetear LEDs al cerrar la aplicación
        GPIO.cleanup()

if __name__ == '__main__':
    RokiApp().run()
    GPIO.cleanup()
