from .block import Block

class SnakeBlock(Block):
    def __init__(self, position : tuple = (45, 45), image_path: str = None):
        super().__init__(size = (15, 15), position = position, image_path=image_path)

        self.__direction = ""

    @property
    def direction(self):
        return self.__direction
    
    def turn(self, direction : str):
        self.__direction = direction

    def walk(self):
        if self.__direction == "LEFT":
            self._position = (self._position[0]-15, self._position[1])
        if self.__direction == "RIGHT":
            self._position = (self._position[0]+15, self._position[1])
        if self.__direction == "UP":
            self._position = (self._position[0], self._position[1]-15)
        if self.__direction == "DOWN":
            self._position = (self._position[0], self._position[1]+15)