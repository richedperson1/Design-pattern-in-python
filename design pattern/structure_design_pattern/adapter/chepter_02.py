
# Medium-Level Assessment

class kiloMeterSensor:
    def get_distance(self,value:float):
        return value


class mileSensor:
    def get_distance(self,value:float):
        return value
    
class distanceAdapter:
    def __init__(self,kiloMeter):
        self.kilometerSensor = kiloMeter()
    def get_distance(self,value):
        return self.kilometerSensor.get_distance(value)*0.621371
    

distanceObj = distanceAdapter(kiloMeterSensor)

print(distanceObj.get_distance(5))