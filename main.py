from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
import RPi.GPIO as GPIO

# LEFT pins
LEFT_LEDS = [17,27,22]

# RIGHT pins
RIGHT_LEDS = [16,20,21]

class RokiScreen(BoxLayout):
    text = StringProperty("")
    battery_level = StringProperty("87%") # INVESTIGAR COMO OBTENER NIVEL DE BATERIA

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
    

    def on_stop(self):
        #Resetear LEDs al cerrar la aplicación
        GPIO.cleanup()

if __name__ == '__main__':
    RokiApp().run()
    GPIO.cleanup()
