import math
class Point:
    def __init__(self,x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'Координаты груза {self.x, self.y}'
    def total_path(self, other):
        x1=self.x
        y1=self.y
        x2=other.x
        y2=other.y
        path=math.hypot(x1-x2, y1-y2)+math.hypot(x1,y1)
        return f'Общий путь курьера равен {path}'

