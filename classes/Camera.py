from classes.Maths import Vec2D


class Camera:
    def __init__(self, pos, entity, levelLength = 50):
        self.pos = Vec2D(pos.x, pos.y)
        self.entity = entity
        self.levelLength = levelLength
        self.x = self.pos.x * 32
        self.y = self.pos.y * 32

    def move(self):
        xPosFloat = self.entity.getPosIndexAsFloat().x
        if 10 < xPosFloat < self.levelLength-10:
            self.pos.x = -xPosFloat + 10
        self.x = self.pos.x * 32
        self.y = self.pos.y * 32
