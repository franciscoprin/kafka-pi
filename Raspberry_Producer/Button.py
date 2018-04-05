import RPi.GPIO as GPIO
import time
import threading

class Button (threading.Thread):
    def __init__(self,semaphore):
    # setting thread
        threading.Thread.__init__(self)
        self.semaphore = semaphore
    # Those pings are in the category ...
        self.allowPings = [7,12,11,13,15,16,18,22,29,31,32,33,35,36,37,38,40]
    # setting button variables.
        self.buttonPing = 12
        self.power = 7
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.buttonPing , GPIO.IN)
        GPIO.setup(self.power, GPIO.OUT)
        self.pwm = GPIO.PWM(self.power, 50)  # Initialize PWM on pwmPin 100Hz frequency
        self.dc = 95  # duty cycle (0-100) for PWM pin

    def setButtonPing(self, buttonPing):
        if (buttonPing in self.buttonPing) and buttonPing != self.power:
            self.buttonPing = buttonPing

    def setPowerPing(self, powerPing):
        if (powerPing in self.buttonPing) and self.buttonPing != powerPing:
            self.power = powerPing

    def getButtonPing(self):
        return self.buttonPing

    def getGroundPing(self):
        return self.power

    def run(self):
        GPIO.setup(self.buttonPing, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.pwm.start(self.dc)
        try:
            while True:
                self.semaphore.acquire()
                if GPIO.input(self.buttonPing):  # button is released
                   #
                   self.pwm.ChangeDutyCycle(self.dc)
                else:  # button is pressed:
                    self.pwm.ChangeDutyCycle(100 - self.dc)
                    # Changing to random graph. (just add random buttons)
                    print("Down")
                    time.sleep(10)
                    # time.sleep(0.075)
                self.semaphore.release()
        except KeyboardInterrupt:  # If CTRL+Z is pressed, exit cleanly:
            print("You pressed CTRL+Z sdasdasdd")
            self.pwm.stop()  # stop PWM
            GPIO.cleanup()  # cleanup all GPIO



