import tkinter as tk
import random
class SurveillanceDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False
        self.motion_detected = False

    def toggle_device(self):  # Corrected method name
        self.status = not self.status

    def simulate_variation(self):
        if self.status:
            self.motion_detected = random.choice([True, False])

    def simulate_change(self):
        if self.status:
            self.simulate_variation()

    def simulate_monitor_motion(self):
        # Implementing basic logic for monitoring motion
        if self.status and self.motion_detected:
            print(f"Motion detected! Device {self.device_id} is monitoring motion.")
        else:
            print(f"No motion detected or device {self.device_id} is turned off.")
