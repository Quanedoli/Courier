import math
class Point:
    def __init__(self,x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'Координаты груза {self.x, self.y}'
    def get_distance_to_courier(self, other):
        x1=self.x
        y1=self.y
        x2=other.x
        y2=other.y
        dist=math.hypot(x1-x2, y1-y2)
        return f'Координаты курьера {x2, y2}\nРасстояние между грузом и курьером {dist}'
    def distance_to_dest(self):
        x1=self.x
        y1=self.y
        Routetodest = math.hypot(x1, y1)
        return f'Расстояние до точки назначения {Routetodest}'
Cargo1=Point(8,6,)
Courier1=Point(9,0)
Route_to_cargo=Cargo1.get_distance_to_courier(Courier1)
Route_to_destination=Cargo1.distance_to_dest()
print(Cargo1)
print(Route_to_cargo)
print(Route_to_destination)