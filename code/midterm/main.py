# main.py

from lib.sensor_module import RoomSensor

sensor1 = RoomSensor("Kitchen", 32, 72, 180)
sensor2 = RoomSensor("Bedroom", 24, 50, 300)
sensor3 = RoomSensor("Balcony", 18, 65, 100)

sensors = [sensor1, sensor2, sensor3]

comfortable_count = 0
normal_count = 0
warning_count = 0

for sensor in sensors:
    sensor.show_info()
    
    level = sensor.comfort_level()
    print(f"Comfort Level: {level}")
    
    light = sensor.light_status()
    print(f"Light Status: {light}")
    
    print()

    if level == "Comfortable":
        comfortable_count += 1
    elif level == "Normal":
        normal_count += 1
    elif level == "Warning":
        warning_count += 1

print(f"Comfortable: {comfortable_count}")
print(f"Normal: {normal_count}")
print(f"Warning: {warning_count}")
