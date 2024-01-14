import tkinter as tk
import random
class IlluminatedDevice:
    def __init__(self, device_id, brightness=0):
        self.device_id = device_id
        self.status = False
        self.brightness = brightness

    def switch_illumination(self):
        self.status = not self.status

    def adjust_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level

    def simulate_variation(self):
        if self.status:
            self.brightness = random.randint(0, 100)
