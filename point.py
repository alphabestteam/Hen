class Point:
    def __init__(self,x,y) -> None:
        self._x = x
        self._y = y
    def __str__(self) -> str:
        return f'x:{self._x} y:{self._y}'
    def __eq__(self, point2) -> bool:
        if self._x == point2._x and self._y == point2._y:
            return True
        return False
    def __add__(self,point2):
        return f'x:{self._x+point2._x} y:{self._y+point2._y}'