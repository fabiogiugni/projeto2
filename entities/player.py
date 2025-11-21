from ..utils.database import Database
from ..ui.scoreBoard import ScoreBoard

class Player:

    def __init__(self, name: str):
        self.__name = name
    
    def gameOver(self, sb: ScoreBoard, db: Database):
        db.insertScore(self.__name, sb.apples, sb.time, sb.score)
    

        