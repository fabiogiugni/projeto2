from abc import ABC, abstractmethod

class ScreenInterface(ABC):
    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def hover(self):
        pass

    @abstractmethod
    def draw(self, display):
        pass
