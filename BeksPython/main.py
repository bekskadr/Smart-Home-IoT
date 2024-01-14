import tkinter as tk
import random
from thermostat import ClimateRegulator
from device_camera import SurveillanceDevice
from device_light import IlluminatedDevice


class HomeAutomationManager:
    def __init__(self):
        self.devices = {'illuminated_device': None, 'climate_regulator': None, 'surveillance_device': None}

    def add_device(self, device):
        if isinstance(device, IlluminatedDevice):
            self.devices['illuminated_device'] = device
        elif isinstance(device, ClimateRegulator):
            self.devices['climate_regulator'] = device
        elif isinstance(device, SurveillanceDevice):
            self.devices['surveillance_device'] = device

    def simulate_operations(self):
        for device in self.devices.values():
            if device:
                device.simulate_variation()


class SmartHomeUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Home IoT Simulator")

        self.illuminated_device = IlluminatedDevice(device_id='illuminated1')
        self.climate_regulator = ClimateRegulator(device_id='regulator1')
        self.surveillance_device = SurveillanceDevice(device_id='surveillance1')
        self.automation_manager = HomeAutomationManager()

        self.automation_manager.add_device(self.illuminated_device)
        self.automation_manager.add_device(self.climate_regulator)
        self.automation_manager.add_device(self.surveillance_device)

        self.setup_interface()

    def setup_interface(self):
        self.text_display = tk.Text(relief=tk.SUNKEN, borderwidth=1)
        self.text_display.pack()

        self.text_display.insert("1.0", "Living Room Illumination: IlluminatedDevice Status: OFF\n")

        self.device_brightness_slider = tk.Scale(self, from_=0, to=100, orient='horizontal',
                                                 command=self.modify_device_brightness)
        self.device_brightness_slider.pack()

        self.device_toggle_button = tk.Button(self, text="Toggle ON/OFF", command=self.toggle_illumination_device)
        self.device_toggle_button.pack()

        self.device_brightness_label = tk.Label(self, text="Living Room Illumination Device - off")
        self.device_brightness_label.pack()

        self.text_display.insert("2.0", "Living Room Climate Control: ClimateRegulator Status: OFF\n")

        self.regulator_temperature_slider = tk.Scale(self, from_=10, to_=25, orient='horizontal',
                                                    command=self.modify_climate_temperature)
        self.regulator_temperature_slider.pack()

        self.regulator_toggle_button = tk.Button(self, text="Toggle ON/OFF", command=self.toggle_climate_regulator)
        self.regulator_toggle_button.pack()

        self.regulator_temperature_label = tk.Label(self, text="Living Room Climate Control - off")
        self.regulator_temperature_label.pack()

        self.text_display.insert("3.0", "Main Area Surveillance Device: SurveillanceDevice Status: OFF")

        self.monitor_status_label = tk.Label(self, text="SurveillanceDevice Status: OFF")
        self.monitor_status_label.pack()

        self.monitor_motion_button = tk.Button(self, text="Random Detect Motion", command=self.simulate_monitor_motion)
        self.monitor_motion_button.pack()

        self.monitor_toggle_button = tk.Button(self, text="Toggle ON/OFF", command=self.toggle_surveillance_device)
        self.monitor_toggle_button.pack()

    def toggle_illumination_device(self):
        self.illuminated_device.switch_illumination()
        state = "ON" if self.illuminated_device.status else "OFF"
        self.text_display.delete("1.0", "1.end")
        self.text_display.insert("1.0", f"Living Room Illumination: IlluminatedDevice Status: {state}")
        self.device_brightness_label.config(
            text=f"Living Room Illumination Device - {self.illuminated_device.brightness}%" if self.illuminated_device.status else "Living Room Illumination Device - OFF")

        if not self.illuminated_device.status:
            self.device_brightness_label.config(text="Living Room Illumination Device - OFF")

    def modify_device_brightness(self, val):
        device_brightness = int(val)
        self.illuminated_device.adjust_brightness(device_brightness)
        if self.illuminated_device.status:
            self.device_brightness_label.config(text=f"Living Room Illumination Device - {device_brightness}%")

    def toggle_climate_regulator(self):
        self.climate_regulator.switch_climate_state()
        state = "ON" if self.climate_regulator.status else "OFF"
        self.text_display.delete("2.0", "2.end")
        self.text_display.insert("2.0", f"Living Room Climate Control: ClimateRegulator Status: {state}")

        if not self.climate_regulator.status:
            self.regulator_temperature_label.config(text="Living Room Climate Control - OFF")

    def modify_climate_temperature(self, val):
        climate_temperature = int(val)
        self.climate_regulator.set_temperature
        (climate_temperature)
        if self.climate_regulator.status:
            self.regulator_temperature_label.config(text=f"Living Room Climate Control - {climate_temperature}°C")

    def simulate_monitor_motion(self):
        if self.surveillance_device.status:
            self.surveillance_device.simulate_monitor_motion()
            motion = "YES" if self.surveillance_device.motion_detected else "NO"
            self.monitor_status_label.config(
                text=f"Main Area Surveillance Device: Motion: {motion}")
            if self.surveillance_device.motion_detected and not self.illuminated_device.status:
                self.toggle_illumination_device()
        else:
            self.monitor_status_label.config(text=f"Main Area Surveillance Device: Motion: NO")

    def toggle_surveillance_device(self):
        self.surveillance_device.toggle_device()
        state = "ON" if self.surveillance_device.status else "OFF"
        self.text_display.delete("3.0", "3.end")
        self.text_display.insert("3.0", f"Main Area Surveillance Device: SurveillanceDevice: {state}")

        if self.surveillance_device.status:
            self.simulate_monitor_motion()

    def update(self):
        self.automation_manager.simulate_operations()
        if self.illuminated_device.status:
            self.device_brightness_label.config(
                text=f"Living Room Illumination Device - {self.illuminated_device.brightness}%")
        if self.climate_regulator.status:
            self.regulator_temperature_label.config(
                text=f"Living Room Climate Control - {self.climate_regulator.temperature}°C")
        self.after(800, self.update)


if __name__ == "__main__":
    app = SmartHomeUI()
    app.after(800, app.update)
    app.mainloop()
