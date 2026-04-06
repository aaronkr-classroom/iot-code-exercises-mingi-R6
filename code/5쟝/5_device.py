# device.py

import random

class Device:
    """
    Base IOT device
    기반의 사물 인터넷 장치
    """
    
    def __init__(self,name: str) -> None:
        self.name = name
        
    def connect(self) -> None:
        print(f"{self.name} connceting..")
        
    def status(self) -> str:
        return "Unknown"
    
class SensorDevice(Device):
    """
    A device that reads data
    데이터를 읽을 수 있는 장치
    """
    def status(self) -> str:
        return "Reading data..."
    
    def read(self) -> float:
        """센서 값을 반환"""
        return 0.0
    
class ActuatorDevice(Device):
    """
    A Device that performs actions.
    작동할수 있는 장치
    """
    def status(self) -> str:
        return "Performing actions..."
    
class TemperatureSensor(SensorDevice):
    """
    Simulated temperature sensor.
    온도 센서 시뮬레이션
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
        
    def read(self) -> float:
        """가짜 온도 값을 반환"""
        return round(random.uniform(20.0, 30.0), 2)
    
class LightSensor(SensorDevice):
    """
    Simulated light sensor
    빛 센서 시뮬레이션
    """
    def read(self) -> float:
        """
        가짜 빛 값을 반환
        """
        return round(random.uniform(0, 100), 2)
  
  
# main.py  
  
from device import SensorDevice, ActuatorDevice, TemperatureSensor, LightSensor

sensor = SensorDevice("Temp Sensor")
actuator = ActuatorDevice("LED Controller")

sensor.connect()
actuator.connect()

print(sensor.status())
print(actuator.status())
print()

temp = TemperatureSensor("Temp1")
light = LightSensor("Light1")

print("Temp: ", temp.read())
print("Light: ", light.read())