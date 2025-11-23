import pygame
import pygame.display
from pygame import Surface

from utils.settings import BLOCK_SIZE

class Block(Surface):
    def __init__(self, size : tuple = (BLOCK_SIZE, BLOCK_SIZE), position : tuple = (50, 50), image_path: str = None):
        super().__init__(size)
        self._position = position
        self._image = None
        self.__size = size

        self.__rotation = 0
        
        # Load image if provided
        if image_path:
            self.__image_path = image_path
            self.load_image(image_path, size)
        

    def setRotation(self, rotation: int):
        self.__rotation = rotation
        self.load_image(self.__image_path, self.__size)

    def load_image(self, image_path: str, size: tuple = None):
        """Load and scale an image for the block with optional rotation"""
        try:
            # Load the image
            original_image = pygame.image.load(image_path).convert_alpha()
            
            # Scale to desired size if provided, otherwise use original size
            if size:
                size = (size[0] * 2, size[1] * 2)
                scaled_image = pygame.transform.scale(original_image, size)
            else:
                scaled_image = original_image
            
            # Apply rotation if specified
            if self.__rotation != 0:
                
                self._image = pygame.transform.rotate(scaled_image, self.__rotation)
            else:
                #print(self.__rotation)
                self._image = scaled_image
            
            # Update the surface size to match the image
            super().__init__(self._image.get_size())
            
        except pygame.error as e:
            print(f"Unable to load image: {image_path}")
            print(e)
            self._image = None

    def fillColor(self, color : tuple):
        super().fill(color)

    def draw(self, display: pygame.display):
        """Draw the block - image takes priority over color"""
        if self._image:
            display.blit(self._image, (self._position[0]-5, self._position[1] -5))
        else:
            display.blit(self, self._position)
        

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position : tuple):
        self._position = position