import tkinter as tk
import random
class ClimateRegulator:
    def __init__(self, device_id, temperature=20):
        self.device_id = device_id
        self.status = False
        self.temperature = temperature

    def switch_climate_state(self):
        self.status = not self.status

    def set_temperature(self, temp):
        if 10 <= temp <= 25:
            self.temperature = temp

    def simulate_variation(self):
        if self.status:
            self.temperature = random.randint(10, 25)
