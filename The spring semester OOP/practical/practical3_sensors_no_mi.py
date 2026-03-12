#sensor for samrt city
class Sensor():
    __doc__ = 'Sensor Class'
    def __init__(self,range,accuracy,ID,**kwargs):
        super().__init__(**kwargs)
        self.range = range
        self.accuracy = accuracy
        self.ID = ID    
    def get_range(self):
        return self.range   
    def get_id(self):
        return self.ID
    
class InfraRedSensor(Sensor):
    def __init__(self,range,accuracy,ID,MOT,Ty,**kwargs):
        super().__init__(range,accuracy,ID,**kwargs)
        self.MaxOpTemp = MOT
        self.Type = Ty
    def detect_motion(self):
        return "Motion detected"
    def get_type(self):
        return self.Type
    
class UltraSonicSensor(Sensor):
    def __init__(self,range,accuracy,ID,OF,**kwargs):
        super().__init__(range,accuracy,ID,**kwargs)
        self.OperatingFreq = OF
    def get_distance(self):
        return 50

class SmartBin():
    def __init__(self,cp,**kwargs):
        super().__init__(**kwargs)
        self.Capacity = cp
        self.FillLevel = 2
        self.fr = InfraRedSensor()
        self.us = UltraSonicSensor()
    def get_capacity(self):
        return self.Capacity
    def get_filllevel(self):
        return self.FillLevel
    def update_fill_level(self):
        self.FillLevel = (100 - self.us.get_distance()) / 100
 
