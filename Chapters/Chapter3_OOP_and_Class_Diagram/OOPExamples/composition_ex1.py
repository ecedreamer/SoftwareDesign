"""
Composition: A relationship among objects, where one object is composed of several objects. It has stronger relationship since the components has no individual lifetime without the main object. 
The composed object is also called complex object. 

Example1: A Mobile object is composed of Battery, Camera, Speaker, Mic, Screen etc objects.
Example2:  
"""


class Battery:
    def __init__(self, mah, volt):
        self.mah = mah
        self.volt = volt

    def display_battery_detail(self):
        print("Battery MAH:", self.mah)
        print("Battery Voltage:", self.volt)
class Camera:
    def __init__(self, mega_pixel, shutter_speed, fps):
        self.mega_pixel = mega_pixel
        self.shutter_speed = shutter_speed
        self.fps = fps     
class Speaker:
    def __init__(self, watt):
        self.watt = watt
class MobilePhone:
    def __init__(self, brand, model, speaker, camera, battery):
        self.brand = brand
        self.model = model
        self.speaker = speaker
        self.camera = camera
        self.battery = battery

    def display_mobile_detail(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Speaker:", self.speaker.watt, "watt")
        print("Camera:")
        print("Mega pixel:", self.camera.mega_pixel)
        print("Shurter Speed:", self.camera.shutter_speed)
        print("Shurter FPS:", self.camera.fps)
        self.battery.display_battery_detail()


def main():
    s1 = Speaker(watt=500) 
    s2 = Speaker(watt=1000)

    b1 = Battery(mah=3000, volt=5.5)
    b2 = Battery(mah=5000, volt=12.0)

    c1 = Camera(mega_pixel=108, shutter_speed=0.01, fps=30)
    c2 = Camera(mega_pixel=64, shutter_speed=0.015, fps=26)

    m1 = MobilePhone("Nokia", "C50", speaker=s1, camera=c1, battery=b2)
    m2 = MobilePhone(
            "MI", "Note 10 Pro", speaker=s2, camera=c1, battery=b2
        )
    
    m1.display_mobile_detail()

main()

""" OUTPUT
Brand: Nokia
Model: C50
Speaker: 500 watt
Camera:
Mega pixel: 108
Shurter Speed: 0.01
Shurter FPS: 30
Battery MAH: 5000
Battery Voltage: 12.0
"""