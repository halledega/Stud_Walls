from Joist_and_Plank import Joist_and_Plank as jp 

class Section():
    def __init__(self, Width: float, Depth: float, Material: jp):
        self._width = Width
        self._depth = Depth
        self._material = Material
        self._lu = {'Width': 0, 'Depth': 0}
        self._area = 0
        self._plys = 1

    @property
    def Plys(self):
        return self._plys
    @Plys.setter
    def Plys(self, val):
        self._plys = val

    @property
    def Width(self):
        return self._width
    @Width.setter
    def Width(self, val):
        self._width = val
        
    @property
    def Depth(self):
        return self._depth
    @Depth.setter
    def Depth(self, val):
        self._depth = val
        
    @property
    def Lu(self):
        return self._lu
    @Lu.setter
    def Lu(self, val):
        self._lu['width'] = val['Width']
        self._lu['Depth'] = val['Depth']
        
    @property
    def Area(self):
        return self._width * self._depth
    
    @property
    def Material(self):
        return self._material
    
    @property
    def Name(self):
        return f"{self._width}x{self._depth}"