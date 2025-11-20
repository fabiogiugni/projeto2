from utils.settings import *
import time



class ScoreBoard:

    def __init__(self, screen:pygame.Surface):
        self.__apples = 0
        self.__startTime = int(time.perf_counter())
        self.__time = int(time.perf_counter()) - self.__startTime
        self.__score = 0
        self.__font = pygame.font.Font(None,32)
        self.__screen = screen
    
    def _updateScore(self, apples: int, time: int):
         self.__score = ((apples * APPLE_VALUE) + (time * TIME_VALUE))

    def draw(self):
        apples_text = self.__font.render(
             f"Apples: {self.__apples}",
             True,WHITE
        )
        time_text = self.__font.render(
             f"Time: {self.__time}",
             True,WHITE
        )
        score_text = self.__font.render(
             f"Score: {self.__score}",
             True,WHITE
        )

        self.__screen.blit(apples_text, (20, 20))
        self.__screen.blit(time_text,   (20, 55))
        self.__screen.blit(score_text,  (20, 90))
    
    def increaseApple(self):
         self.__apples += 1
         self._updateScore(self.__apples, self.__time)

    def updateTime(self):
        self.__time = int(time.perf_counter()) - self.__startTime
        self._updateScore(self.__apples, self.__time)

    def getInfo(self) -> tuple[int, int, int]:
            return self.__apples, self.__time, self.__score