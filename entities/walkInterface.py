from abc import ABC, abstractmethod

class WalkInterface(ABC):
    
    @abstractmethod
    def turn(self, direction : str):
        pass

    @abstractmethod
    def walk(self):
        pass
